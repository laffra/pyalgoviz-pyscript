
window.editorClearLine = () => {
    if (window.editorMarker) {
        window.editorMarker.clear()
    }
}

window.editorMarkLine = (lineno, error) => {
    window.editorClearLine();
    setTimeout(() => {
        window.editorMarker = window.editor.getDoc().markText(
            { line: lineno, ch: 0},
            { line: lineno, ch: 200},
            { className: "editor-error" }
        );
        setTimeout(() => {
            $(".editor-error").attr("title", error)
        }, 500);
    }, 1000)
}

