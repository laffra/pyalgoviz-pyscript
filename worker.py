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

import ast
import json
import os
import random
import textwrap
import traceback
import sys
import time

import polyscript
import pyscript

class Runner():
    """ Runner class for running Python code. """

    def __init__(self, script, visualization):
        """ Runs the script. """
        self.viz = []
        self.log = []
        self.last_lineno = 0
        self.lineno = 0
        self.global_state = self.get_state(self.algo_print)
        self.viz_state = self.get_state(self.viz_print)
        self.start = time.time()
        self.script = script
        self.visualization = visualization
        self.run()

    def run(self):
        """ Runs the script. """
        try:
            sys.settrace(self.step)
            exec(self.script, self.global_state, self.global_state)
        except Exception as e:
            print(e)
            self.exec_error(e)
        finally:
            sys.settrace(None)
        publish("log", self.log[::])

    def step(self, frame, event, arg):
        """ Step function for the tracer. """
        self.viz.clear()
        if self.update(frame):
            try:
                exec(self.visualization, self.viz_state, self.viz_state)
            except Exception as e:
                self.viz_error(e)
            publish("trace", [ self.lineno, "\n".join(self.viz) ])
        return self.step
                

    def update(self, frame):
        """ Updates the runner. """
        if time.time() - self.start > 30:
            raise TimeoutError("Ran more than 30 seconds.")
        if frame.f_code.co_filename != "<string>":
            return False
        self.lineno = frame.f_lineno
        if self.lineno == self.last_lineno:
            return False
        self.last_lineno = self.lineno
        self.viz_state.update(frame.f_locals)
        self.viz_state["__lineno__"] = self.lineno
        return True
    
    def viz_error(self, e):
        """ Handle a visualization error. """
        tb = traceback.extract_tb(sys.exc_info()[2])
        error_lineno = tb[-1].lineno
        self.viz.append(f"error(\"Visualization error at line {error_lineno}: {e}\")")
    
    def exec_error(self, e):
        """ Handle an exec error. """
        tb = traceback.extract_tb(sys.exc_info()[2])
        error_lineno = tb[-1].lineno
        publish("error", [error_lineno, str(e)])

    def line(self, x1, y1, x2, y2, color="black", width=1):
        """ Draw a line """
        self.viz.append(f"l({x1},{y1},{x2},{y2},{repr(color)},{width})")

    def text(self, x, y, txt, size=12, font="Arial", color="black"):
        """ Draw a text """
        self.viz.append(f"t({x},{y},{repr(txt)},{size},{repr(font)},{repr(color)})")

    def circle(self, x, y, radius, fill="white", border="gray"):
        """ Draw a circle """
        self.viz.append(f"c({x},{y},{radius},{repr(fill)},{repr(border)})")

    def arc(self, x, y, radius, start_angle, end_angle, color='black', width=1):
        """ Draw an arc """
        self.viz.append(f"a({x},{y},{radius},{start_angle},{end_angle},{repr(color)},{width})")

    def rect(self, x, y, w, h, fill="white", border="gray"):
        """ Draw a rectangle """
        self.viz.append(f"r({x},{y},{w},{h},{repr(fill)},{repr(border)})")

    def viz_print(self, *args):
        """ The visualization script prints something """
        self.viz.append(f"p(\"{' '.join(map(str, args))}\")")

    def algo_print(self, *args):
        """ The algorithm script prints something """
        msg = " ".join(map(str, args))
        line_msg = f"Line {self.lineno}: {msg}"
        self.log.append(line_msg)

    def barchart(self, x, y, w, h, data, highlight=None, fill="black", scale=1):
        """ Draw a barchart """
        assert isinstance(data, list), f"Expected a list of numbers, not {type(data)}"
        self.viz.append(f"b({x},{y},{w},{h},{repr(data)},{highlight},{repr(fill)},{scale})")

    def beep(self, frequency=440, duration=10):
        """ Sound a beep """
        self.viz.append(f"s({frequency},{duration})")

    def get_state(self, print_function):
        """ Returns a state to pass to exec. """
        state = {}
        state.update(globals())
        state.update({
            "line": self.line,
            "text": self.text,
            "rect": self.rect,
            "barchart": self.barchart,
            "circle": self.circle,
            "arc": self.arc,
            "beep": self.beep,
            "print": print_function,
        })
        return state


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
        return [ filename, name, author, algorithm, visualization ]


def load_related(name):
    """ Loads the algorithm. """
    category = name.split("/")[0]
    dirname = os.path.dirname(f"visualizations/{name}.py")
    names = [f"{category}/{name.replace(".py", "")}" for name in os.listdir(dirname)]
    try:
        return random.sample(names, 5)
    except Exception:
        return names


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
    polyscript.xworker.sync.publish("Worker", "Main", topic, data)


def load(name):
    """" Loads the algorithm with the given name. """
    try:
        publish("source", load_algorithm(name))
        publish("related", load_related(name))
    except Exception:
        tip = "Press the <b>Load...</b> button to try any of the built-in algorithms."
        msg = f"Cannot load {name}<p>{tip}"
        publish("error", [ 1, msg ])
        traceback.print_exc()


def handle_request(sender, topic, request):
    """
    Handles requests received by the worker process.
    """
    if topic == "run":
        script, visualization = json.loads(request)
        Runner(script, visualization)
    elif topic == "load":
        load(json.loads(request))
    else:
        publish("error", json.dumps(f"Unknown topic: {topic}"))


polyscript.xworker.sync.handler = handle_request
polyscript.xworker.sync.subscribe("Worker", "run", "pyodide-worker")
polyscript.xworker.sync.subscribe("Worker", "load", "pyodide-worker")

sys.path.append("/home/pyodide/visualizations")
load_choices()

publish("ready", "")
