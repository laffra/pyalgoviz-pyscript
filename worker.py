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

import inspect
import importlib
import json
import math
import os
import textwrap
import traceback
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


def getsource(func):
    """ Returns the source code of a function. """
    lines = inspect.getsource(func).split("\n")
    return textwrap.dedent("\n".join(lines[1:]))


def load_algorithm(name):
    """ Loads the algorithm. """
    mod = importlib.import_module(f"visualizations.{name}")
    return [
        "source",
        [
            mod.__name,       # pylint: disable=protected-access
            mod.__author,       # pylint: disable=protected-access
            getsource(mod.__algorithm),       # pylint: disable=protected-access
            getsource(mod.__visualization),   # pylint: disable=protected-access
        ]
    ]

def load_choices():
    """ Loads the algorithm choices. """
    choices = [
        os.path.splitext(f)[0]
        for f in os.listdir("/home/pyodide/visualizations/")
        if f.endswith('.py') and not f.startswith('__')
    ]
    polyscript.xworker.sync.publish(
        "Worker",
        "Main",
        "choices",
        choices,
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
            result = {
                "viz": [],
                "log": [],
            }
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
                result["viz"].append([ lineno, "\n".join(viz) ])
                return step

            log = []
            try:
                sys.settrace(step)
                exec(script, state, state)
            finally:
                sys.settrace(None)
            result["log"] = log[::]
            response = "visualize"
        except Exception as e:
            tb = traceback.extract_tb(sys.exc_info()[2])
            error_lineno = tb[-1].lineno
            result = [error_lineno, str(e)]
            response = "error"
    elif topic == "load":
        try:
            response, result = load_algorithm(json.loads(request))
        except Exception:
            tip = "Press the <b>Load...</b> button to try any of the built-in algorithms."
            msg = f"Cannot load {request}<p>{tip}"
            response, result = "error", [ 1, msg ]
    else:
        result = f"Unknown topic: {topic}"
        response = "error"

    polyscript.xworker.sync.publish(
        "Worker",
        "Main",
        response,
        json.dumps(result),
    )

polyscript.xworker.sync.handler = handle_request
polyscript.xworker.sync.subscribe("Worker", "run", "pyodide-worker")
polyscript.xworker.sync.subscribe("Worker", "load", "pyodide-worker")

load_choices()

polyscript.xworker.sync.publish(
    "Worker",
    "Main",
    "ready",
    ""
)