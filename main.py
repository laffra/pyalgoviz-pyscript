"""
PyAlgoViz - A Python Algorithm Visualizer
Copyright (c) 2024 laffra - All Rights Reserved.
"""

# pylint: disable=invalid-name
# pylint: disable=global-statement
# pylint: disable=exec-used
# pylint: disable=broad-except
# pylint: disable=unused-argument
# pylint: disable=too-many-arguments
# pylint: disable=too-many-positional-arguments

import asyncio
from polyscript import XWorker # type: ignore   pylint: disable=import-error
import ltk
import editor
import worker_files

ALGORITHM = "# Your algorithm goes here."
CLICK_LOAD = "# Your algorithm goes here.\n\n# Click Load... for an existing example."
VISUALIZATION = "# Your visualization logic goes here."

class State(ltk.Model):
    """ The state for the algorithm visualization """
    step: int = 0
    steps = []
    step_count = 0
    choices = {}

    def changed(self, name, value):
        if name == "step":
            try:
                render_current()
            except Exception:
                pass


state = State()
editor_algo = editor.Editor(ALGORITHM)
editor_viz = editor.Editor(VISUALIZATION)
progress = ltk.Slider(state.step, 0, 3000)

progress.on("slide", ltk.proxy(lambda *args: progress.trigger("change")))

@ltk.callback
def run(_event=None):
    """ Run the current algorithm """
    clear_steps()
    ltk.publish(
        "Main",
        "Worker",
        "run",
        [editor_algo.get(), editor_viz.get()]
    )
    ltk.window.clear()
    ltk.window.text(15, 125, "Running...", 20, "Arial", "green")

def render_current():
    """ Render the current step """
    step = state.steps[state.step]
    lineno, viz = step
    ltk.window.clear()
    ltk.window.render(viz)
    editor_algo.mark_line(lineno - 1)

def trace(data):
    """ Add one trace step for the current algorithm """
    state.steps.append(data)
    state.step_count += 1
    render_current()
    state.step += 1
    progress.element.slider("option", "max", str(max(3000, state.step_count)))


def clear_steps():
    """ Clear the trace steps """
    state.steps.clear()
    state.step = 0
    state.step_count = 0
    ltk.find(".log-algo .log-line").empty()
    ltk.window.init()
    ltk.window.text(15, 125, "Loading...", 20, "Arial", "green")
    

def log(data):
    """ Show the print statements made by the algorithm """
    progress.element.slider("option", "max", str(state.step_count))
    for line in data:
        ltk.find(".log-algo").append(
            ltk.Div(line)
                .addClass("log-line")
        )


def show_error(data):
    """ Show any errors generated by the current algorithm """
    lineno, error = data
    ltk.find(".log-algo").append(
        ltk.Div(f"Error at line {lineno}: {error}")
            .addClass("log-line log-error")
    )
    editor_algo.mark_line(lineno - 1)


def previous_step(_event=None):
    """ Show the previous step """
    state.step = max(0, state.step - 1)


def next_step(_event=None):
    """ Show the next step """
    state.step = min(len(state.steps.value) - 1, state.step + 1)


def visit(category, name):
    """ Switch to another algorithm """
    ltk.window.location = f"?name={category}/{name}"


@ltk.callback
def load_algo(event):
    """ Load an algorithm """
    button = ltk.find(event.target)
    category = button.attr("category")
    ltk.find(".ui-dialog").remove()
    ltk.find("body").animate(
        {
            "opacity": 0
        },
        lambda: visit(category, button.attr("name"))
    )


def load(_event=None):
    """ Load an existing algorithm """
    ltk.Div([
        ltk.VBox(ltk.Heading3(category), [
            ltk.Button(choice, load_algo)
                .attr("category", category)
                .attr("name", choice)
                .addClass("choice-button")
            for choice in sorted(choices)
        ]).addClass("choice-category")
        for category, choices in sorted(state.choices.value.items(), key=lambda x: -len(x[1]))
    ]).attr("title", "Load...").addClass("choice-dialog").dialog(ltk.to_js({
        "width": 900,
    }))


def load_source(sources):
    """ Load the algorithm and visualization """
    name, author, algo, viz = sources
    editor_algo.set(algo)
    editor_viz.set(viz)
    ltk.find(".log-algo").append(
        ltk.Heading1(name.replace("_", " "))
            .addClass("name"),
        ltk.Text(f"Author: {author}")
            .addClass("author"),
    )
    run()


def show_related(names):
    """ Show the related scripts the user can choose from """
    ltk.find(".related").empty().append(
        ltk.HBox(
            ltk.Label("Related Scripts:"),
            [
                ltk.Button(name.replace("-"," ").replace("_", " "), load_algo)
                    .attr("category", category)
                    .attr("name", name)
                    .addClass("choice-button")
                for category, name in [entry.split("/") for entry in names]
            ],
            ltk.Button("More...", load)
                .addClass("choice-button")
        ).addClass("related-container")
    )
    

def save_choices(choices):
    """ Save the algorithms the user can choose from """
    state.choices = ltk.to_py(choices)
    ltk.find("#load-button").attr("disabled", False)
    if "name=" not in ltk.window.location.href:
        editor_algo.set(CLICK_LOAD)


def setup_ui():
    """ Create the UI """
    ltk.find("body").append(
        ltk.HorizontalSplitPane(
            ltk.VerticalSplitPane(
                ltk.VBox(
                    editor_algo,
                    ltk.HBox(
                        ltk.Button("run", run),
                        ltk.Button("Prev", previous_step),
                        progress.addClass("progress"),
                        ltk.Label(state.step).addClass("step-label"),
                        ltk.Button("Next", next_step),
                        ltk.Button("Load...", load)
                            .attr("id", "load-button")
                            .attr("disabled", True),
                    ).addClass("controls"),
                ).addClass("top-left"),
                editor_viz,
                "editors",
            ).addClass("column"),
            ltk.VerticalSplitPane(
                ltk.Div(
                    ltk.Div()
                        .addClass("drawing"),
                    ltk.Div().addClass("related"),
                ).addClass("top-right"),
                ltk.Div(
                    ltk.Tabs(
                        ltk.Div()
                            .addClass("log-algo")
                            .attr("name", "Algorithm Log"),
                        ltk.Div()
                            .addClass("log-viz")
                            .attr("name", "Visualization Log"),
                    ).addClass("log"),
                ),
                "result",
            ).addClass("column"),
            "main",
        )
        .addClass("main")
    )


def worker_ready(request):
    """ Worker is ready """
    ltk.publish(
        "Main",
        "Worker",
        "load",
        ltk.get_url_parameter("name")
    )


def setup_worker():
    """ Setup the worker """
    ltk.subscribe("Main", "trace", trace)
    ltk.subscribe("Main", "log", log)
    ltk.subscribe("Main", "error", show_error)
    ltk.subscribe("Main", "ready", worker_ready)
    ltk.subscribe("Main", "source", load_source)
    ltk.subscribe("Main", "choices", save_choices)
    ltk.subscribe("Main", "related", show_related)
    files = worker_files.files
    files["primitives.py"] = "primitives.py"
    config = {
        "interpreter": "pyodide/pyodide.js",
        "packages": [ 
        ],
        "files": files,
    }
    worker = XWorker("worker.py", config=ltk.to_js(config), type="pyodide")
    ltk.register_worker("pyodide-worker", worker)


def show_loading():
    """ Show the loading screen """
    if "name=" in ltk.window.location.href:
        editor_algo.set("Loading...")
        editor_viz.set("Loading...")


def setup():
    """ Setup the application """
    setup_ui()
    setup_worker()
    show_loading()
    ltk.window.init()


setup()
