"""
Drawing primitives that can be used to visualize data.
"""

#pylint: disable=unused-argument
#pylint: disable=wrong-import-position
#pylint: disable=too-many-arguments
#pylint: disable=too-many-positional-arguments


def line(x1, y1, x2, y2, color, w):
    """ Draw a line """

def text(x, y, txt, size=12, font="Arial", color="black"):
    """ Draw a text """

def rect(x, y, w, h, fill="white", border="gray"):
    """ Draw a rectangle """

def circle(x, y, radius, fill="white", border="gray"):
    """ Draw a circle """

def arc(x, y, radius, start_angle, end_angle, color='black'):
    """ Draw an arc """

def barchart(x, y, w, h, data, highlight=None, fill="black", scale=1):
    """ Draw a barchart """
