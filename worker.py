"""
CopyRight (c) 2024 - Chris Laffra - All Rights Reserved.

This module provides a worker for a PyScript-based application to run Python
code, find dependencies, and perform code completion.
"""

# pylint: disable=import-error
# pylint: disable=exec-used
# pylint: disable=broad-except
# pylint: disable=unused-argument
# pylint: disable=too-many-arguments
# pylint: disable=too-many-positional-arguments

import json
import sys

import polyscript

viz = []

def line(x1, y1, x2, y2, color, w):
    """ Draw a line """
    viz.append(f"line({x1}, {y1}, {x2}, {y2}, {repr(color)}, {w})")


def text(x, y, s, size=14, font="Courier", style="normal", color="black"):
    """ Draw a text """
    viz.append(f"text({x}, {y}, {repr(s)}, {size}, {repr(font)}, {repr(style)}, {repr(color)})")


def rect(x, y, w, h, color):
    """ Draw a rectangle """
    viz.append(f"rect({x}, {y}, {w}, {h}, {repr(color)})")


def barchart(x, y, w, h, data, highlight, scale=1):
    """ Draw a barchart """
    print("barchart", data)
    viz.append(f"barchart({x}, {y}, {w}, {h}, {repr(data)}, {highlight}, {scale})")



def handle_request(sender, topic, request):
    """
    Handles requests received by the worker process.
    """
    if topic == "run":
        script, visualization = json.loads(request)
        print("Worker run")
        try:
            result = []
            state = {
                "line": line,
                "text": text,
                "rect": rect,
                "barchart": barchart,
            }

            def step(frame, event, arg):
                viz.clear()
                lineno = frame.f_lineno
                state.update(frame.f_locals)
                try:
                    exec(visualization, state, state)
                except Exception as e:
                    viz.append(f"error('''{e}''')")
                result.append([ lineno, viz ])

            sys.setprofile(step)
            exec(script, state, state)
            response = "visualize"
        except Exception as e:
            result = str(e)
            response = "error"
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
polyscript.xworker.sync.publish(
    "Worker",
    "Main",
    "ready",
    ""
)
