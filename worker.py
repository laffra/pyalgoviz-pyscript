"""
CopyRight (c) 2024 - Chris Laffra - All Rights Reserved.

This module provides a worker for a PyScript-based application to run Python
code, find dependencies, and perform code completion.
"""

# pylint: disable=import-error
# pylint: disable=global-statement
# pylint: disable=exec-used
# pylint: disable=broad-except
# pylint: disable=unused-argument
# pylint: disable=too-many-arguments
# pylint: disable=too-many-positional-arguments

from builtins import *

import ast
import inspect
import importlib
import json
import math
import os
import random
import textwrap
import traceback
import types
import sys
import time

import polyscript


viz = []
log = []
lineno = 0


def line(x1, y1, x2, y2, color="black", width=1):
    """ Draw a line """
    viz.append(f"l({x1},{y1},{x2},{y2},{repr(color)},{width})")


def text(x, y, txt, size=12, font="Arial", color="black"):
    """ Draw a text """
    viz.append(f"t({x},{y},{repr(txt)},{size},{repr(font)},{repr(color)})")


def circle(x, y, radius, fill="white", border="gray"):
    """ Draw a circle """
    viz.append(f"c({x},{y},{radius},{repr(fill)},{repr(border)})")


def arc(x, y, radius, startAngle, endAngle, color='black'):
    """ Draw an arc """
    viz.append(f"a({x},{y},{radius},{startAngle},{endAngle},{repr(color)})")


def rect(x, y, w, h, fill="white", border="gray"):
    """ Draw a rectangle """
    viz.append(f"r({x},{y},{w},{h},{repr(fill)},{repr(border)})")


def viz_print(*args):
    """ The visualization script prints something """
    viz.append(f"p(\"{' '.join(map(str, args))}\")")

orig_print = print

def algo_print(*args):
    """ The algorithm script prints something """
    msg = " ".join(map(str, args))
    line_msg = f"Line {lineno}: {msg}"
    log.append(line_msg)
    orig_print(line_msg)


def barchart(x, y, w, h, data, highlight=None, fill="black", scale=1):
    """ Draw a barchart """
    assert isinstance(data, list), f"Expected a list of numbers, not {type(data)}"
    viz.append(f"b({x},{y},{w},{h},{repr(data)},{highlight},{repr(fill)},{scale})")


def beep(frequency=440, duration=10):
    """ Sound a beep """
    viz.append(f"s({frequency},{duration})")


def getsource(function, lines):
    """ Returns the source code of a function. """
    code = "\n".join(lines[function.lineno:function.end_lineno])
    return textwrap.dedent(code)


def load_algorithm(name):
    """ Loads the algorithm. """
    filename = f"visualizations/{name}.py"
    with open(filename, encoding="utf-8") as f:
        source = f.read()
        lines = source.split("\n")
        mod = ast.parse(source)
        name = mod.body[1].value.value
        author = mod.body[2].value.value
        algorithm = getsource(mod.body[3], lines)
        visualization = getsource(mod.body[4], lines)
        return [ name, author, algorithm, visualization ]


def load_related(name):
    """ Loads the algorithm. """
    category = name.split("/")[0]
    dirname = os.path.dirname(f"visualizations/{name}.py")
    names = [f"{category}/{name.replace(".py", "")}" for name in os.listdir(dirname)]
    return random.sample(names, 5)


def load_choices():
    """ Loads the algorithm choices. """
    choices = {
        category: [
            os.path.splitext(f)[0]
            for f in os.listdir(f"/home/pyodide/visualizations/{category}")
            if f.endswith('.py') and not f.startswith('__')
        ]
        for category in os.listdir("/home/pyodide/visualizations/")
    }
    publish("choices", choices)

def publish(topic, data):
    """ Publishes data to the main process. """
    polyscript.xworker.sync.publish(
        "Worker",
        "Main",
        topic,
        data
    )

def handle_request(sender, topic, request):
    """
    Handles requests received by the worker process.
    """
    global log
    if topic == "run":
        script, visualization = json.loads(request)
        try:
            start = time.time()
            state = globals()
            state.update({
                "line": line,
                "text": text,
                "rect": rect,
                "barchart": barchart,
                "circle": circle,
                "arc": arc,
                "beep": beep,
                "print": algo_print,
            })

            def step(frame, event, arg):
                global viz, lineno
                viz = []
                filename = frame.f_code.co_filename
                if filename != "<string>":
                    return step
                lineno = frame.f_lineno
                if time.time() - start > 10:
                    raise TimeoutError("Ran more than 10 seconds")
                state.update(frame.f_locals)
                state.update(globals())
                state["__lineno__"] = lineno
                try:
                    state["print"] = viz_print
                    exec(visualization, state, state)
                except Exception as e:
                    tb = traceback.extract_tb(sys.exc_info()[2])
                    error_lineno = tb[-1].lineno
                    viz.append(f"error(\"Visualization error at line {error_lineno}: {e}\")")
                finally:
                    state["print"] = algo_print
                publish("trace", [ lineno, "\n".join(viz) ])
                return step

            log = []
            try:
                sys.settrace(step)
                exec(script, state, state)
            finally:
                sys.settrace(None)
            publish("log", log[::])
        except Exception as e:
            tb = traceback.extract_tb(sys.exc_info()[2])
            error_lineno = tb[-1].lineno
            publish("error", [error_lineno, str(e)])
    elif topic == "load":
        try:
            name = json.loads(request)
            publish("source", load_algorithm(name))
            publish("related", load_related(name))
        except Exception:
            tip = "Press the <b>Load...</b> button to try any of the built-in algorithms."
            msg = f"Cannot load {request}<p>{tip}"
            publish("error", [ 1, msg ])
            traceback.print_exc()
    else:
        publish("error", json.dumps(f"Unknown topic: {topic}"))

polyscript.xworker.sync.handler = handle_request
polyscript.xworker.sync.subscribe("Worker", "run", "pyodide-worker")
polyscript.xworker.sync.subscribe("Worker", "load", "pyodide-worker")

sys.path.append("/home/pyodide/visualizations")
load_choices()

publish("ready", "")
