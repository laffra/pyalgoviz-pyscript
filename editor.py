"""
Copyright (c) 2024 laffra - All Rights Reserved. 

A wrapper for the CodeMirror editor.
"""

import ltk


class Editor(ltk.Div):
    """
    A wrapper for the CodeMirror editor that provides a convenient interface for
    interacting with a code editor.
    
    The `Editor` class is responsible for creating and managing a CodeMirror
    editor instance. It provides methods for setting the editor's value, getting
    the current cursor position, focusing the editor, refreshing the editor, and
    handling code completion.
    
    The class also sets up event listeners for the "blur" and "change" events, which 
    trigger the "change" event and clear any marks on the editor, respectively.
    """

    classes = [ "editor" ] # The CSS classes to apply to this ltk.Widget subclass

    def __init__(self, value=""):
        ltk.Div.__init__(self)
        self.editor = None
        self.marker = None
        self.code_completor = None
        self.value = value
        ltk.schedule(lambda: self.set(self.value), f"set value {id(self)}")
        ltk.schedule(self.refresh, f"force editor redraw {id(self)}")

    def create_editor(self):
        """
        Creates a CodeMirror editor instance and sets up event listeners for the editor.
        """
        if self.editor is None:
            self.editor = ltk.window.CodeMirror.new(self.element[0], ltk.to_js({
                "mode": {
                    "name": "python",
                    "version": 3,
                    "singleLineStringErrors": False
                },
                "lineNumbers": True,
                "indentUnit": 4,
                "matchBrackets": True,
            }))
            self.editor.setSize("100%", "calc(100% - 35px)")
            self.editor.on("blur", ltk.proxy(lambda *args: self.trigger("change")))
            self.editor.on("change", ltk.proxy(lambda *args: self.clear_mark()))
            self.editor.on("keyup", ltk.proxy(lambda *args: self.trigger("change")))

    def get(self):
        """
        Returns the current value of the CodeMirror editor instance.
        """
        return self.editor.getValue()

    def get_cursor(self):
        """
        Returns the current cursor position of the CodeMirror editor instance.
        """
        return self.editor.getCursor()

    def set(self, value):
        """
        Sets the value of the CodeMirror editor instance.
        
        Args:
            value (str): The new value to set for the editor.
        """
        self.value = value
        if self.editor and self.editor.hasFocus():
            return self
        self.create_editor()
        self.editor.setValue(str(value))
        return self

    def focus(self):
        """
        Focuses the CodeMirror editor instance. Browser keyboard events will be sent to the editor.
        
        Returns:
            self: The current instance of the editor object.
        """
        self.editor.focus()
        return self

    def refresh(self):
        """
        Refreshes the CodeMirror editor instance. This is needed to redraw the
        editor after the window has been resized.
        
        Returns:
            self: The current instance of the editor object.
        """
        self.editor.refresh()
        return self

    def handle_code_completion(self, completions):
        """
        Handles the code completion functionality for the editor computed by the worker.
        
        Args:
            completions (list): A list of code completion suggestions.
        """
        if self.code_completor:
            self.code_completor.handle_code_completion(completions)

    def clear_mark(self):
        """
        Clears the current line marker from the editor. Used to show the location of syntax errors.
        """
        if self.marker:
            self.marker.clear()

    def mark_line(self, lineno):
        """
        Marks the specified line number in the editor with a visual indicator. 
        Used to show the location of syntax errors.
        
        Args:
            lineno (int): The line number to mark, starting from 1.
            error (str): The error message to display.
        """
        self.clear_mark()
        self.marker = self.editor.getDoc().markText(
            ltk.to_js({ "line": lineno, "ch": 0}),
            ltk.to_js({ "line": lineno, "ch": 200}),
            ltk.to_js({ "className": "editor_line" }),
        )

    def start_running(self):
        """
        Sets the editor in "run" mode.
        """
        self.find(".CodeMirror-scroll").css("background", "#f2f2f2")

    def stop_running(self):
        """
        Sets the editor in "edit" mode.
        """
        self.find(".CodeMirror-scroll").css("background", "#FFF")
