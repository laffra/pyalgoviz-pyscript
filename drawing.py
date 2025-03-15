"""
Drawing primitives.
"""

# pylint: disable=invalid-name
# pylint: disable=global-statement
# pylint: disable=exec-used

import ltk

canvas = None

def init():
    """ Inittializes the drawing canvas """
    global canvas
    div = ltk.find(".drawing").empty()
    canvas = ltk.Canvas()
    div.append(canvas
        .attr("width", int(div.width()))
        .attr("height", int(div.height()))
    )


def clear():
    """ Clears the drawing canvas """
    div = ltk.find(".drawing")
    canvas.fill_style = "white"
    canvas.fill_rect(0, 0, div.width(), div.height())
    canvas.stroke_style = "black"


def number(x, y, label, value, scale=4, color='black'):
    """ Draw a number """
    text(x, y+10, label)
    rect(x+20, y, value*scale, 10, color)
    text(x+22+value*scale, y+10, value)


def barchart(x, y, w, h, items, highlight=-1, scale=1, fill='black', border='black'):
    """ Draw a barchart """
    rect(x, y, w, h, '#FDFDF0', border)
    if items:
        d = min(15, int(w/len(items)))
        offset = (w - len(items)*d)/2
        for n,item in enumerate(items):
            hitem = item*scale
            rect(offset+x+n*d, y+h-hitem, d-2, hitem, 'red' if n==highlight else fill)


NUMBER = ('number', (int,float))
STRING = ('string', str)


def check(primitive, param, value, expected):
    """ Check the type of a parameter """
    kind,typ = expected
    e = f"expected a {kind} for {primitive}.{param}, instead got {repr(value)}"
    assert isinstance(value, typ), e


def text(x, y, txt, size=13, font='Arial', color='black'):
    """ Draw a text """
    check('text', 'x', x, NUMBER)
    check('text', 'y', x, NUMBER)
    check('text', 'size', size, NUMBER)
    check('text', 'font', font, STRING)
    check('text', 'color', color, STRING)
    canvas.fill_style = color
    canvas.font = f"{size}px {font}"
    canvas.fill_text(x, y, txt)


def error(msg):
    """ Draw an error message """
    text(20, 20, msg, 20, 'Arial', 'red')


def line(x1, y1, x2, y2, color='black', width=1):
    """ Draw a line """
    canvas.stroke_style = color
    canvas.line_width = width
    canvas.line(x1, y1, x2, y2)


def rect(x, y, w, h, fill='white', border='black'):
    """ Draw a rectangle """
    check('rect', 'x', x, NUMBER)
    check('rect', 'y', x, NUMBER)
    check('rect', 'w', w, NUMBER)
    check('rect', 'h', h, NUMBER)
    check('rect', 'fill', fill, STRING)
    check('rect', 'border', border, STRING)
    canvas.stroke_style = border
    canvas.rect(x, y, w, h)
    canvas.fill_style = fill
    canvas.fill_rect(x, y, w, h)


def circle(x, y, radius, fill='white', border='black'):
    """ Draw a circle """
    check('circle', 'x', x, NUMBER)
    check('circle', 'y', x, NUMBER)
    check('circle', 'radius', radius, NUMBER)
    check('circle', 'fill', fill, STRING)
    check('circle', 'border', border, STRING)
    canvas.strokeStyle = border
    canvas.circle(x, y, radius)
    canvas.fill_style = border
    canvas.fill_circle(x, y, radius)


def arc(cx, cy, innerRadius, outerRadius, startAngle, endAngle, color='black'):
    """ Draw an arc """
    check('circle', 'cx', cx, NUMBER)
    check('circle', 'cy', cx, NUMBER)
    check('circle', 'innerRadius', innerRadius, NUMBER)
    check('circle', 'outerRadius', outerRadius, NUMBER)
    check('circle', 'startAngle', startAngle, NUMBER)
    check('circle', 'endAngle', endAngle, NUMBER)
    check('circle', 'color', color, STRING)


primitives = {
    'text': text,
    'line': line,
    'rect': rect,
    'circle': circle,
    'arc': arc,
    'error': error,
    'barchart': barchart,
    'number': number
}
