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

import inspect
import json
import textwrap
import sys

import polyscript

import visualizations

viz = []

def line(x1, y1, x2, y2, color, w):
    """ Draw a line """
    viz.append(f"line({x1}, {y1}, {x2}, {y2}, {repr(color)}, {w})")


def text(x, y, txt, size=14, font="Courier", color="black"):
    """ Draw a text """
    viz.append(f"text({x}, {y}, {repr(txt)}, {size}, {repr(font)}, {repr(color)})")


def rect(x, y, w, h, color):
    """ Draw a rectangle """
    viz.append(f"rect({x}, {y}, {w}, {h}, {repr(color)})")


def barchart(x, y, w, h, data, highlight, scale=1):
    """ Draw a barchart """
    viz.append(f"barchart({x}, {y}, {w}, {h}, {repr(data)}, {highlight}, {scale})")


def getsource(function):
    """ Returns the source code of a function. """
    lines = inspect.getsource(function).split("\n")
    return textwrap.dedent("\n".join(lines[1:]))


def load_algorithm(name):
    """ Loads the algorithm. """
    module = getattr(visualizations, name)
    return [
        "source",
        [
            getsource(module.algorithm),
            getsource(module.visualization),
        ]
    ]


def load_choices():
    """ Loads the algorithm choices. """
    polyscript.xworker.sync.publish(
        "Worker",
        "Main",
        "choices",
        [
            key
            for key, value in visualizations.__dict__.items()
            if inspect.ismodule(value)
        ]
    )


def handle_request(sender, topic, request):
    """
    Handles requests received by the worker process.
    """
    if topic == "run":
        script, visualization = json.loads(request)
        try:
            result = []
            state = {
                "line": line,
                "text": text,
                "rect": rect,
                "barchart": barchart,
            }

            def step(frame, event, arg):
                global viz
                viz = []
                lineno = frame.f_lineno
                filename = frame.f_code.co_filename
                if filename != "<string>":
                    return step
                state.update(frame.f_locals)
                try:
                    exec(visualization, state, state)
                except Exception as e:
                    viz.append(f"error(\"{e}\")")
                result.append([ lineno, viz ])
                return step

            sys.settrace(step)
            exec(script, state, state)
            response = "visualize"
        except Exception as e:
            result = str(e)
            response = "error"
    elif topic == "load":
        response, result = load_algorithm(json.loads(request))
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
