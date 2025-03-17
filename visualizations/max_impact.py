"""
 Max Impact 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Max Impact"
__author = "laffra"

def __algorithm():
    def impact(effort, productivity, communication, charisma):
        max_impact = (
            30 * productivity +        # your main output
            50 * communication +    # how you collaborate
            20 * charisma            # if they like you
        ) / 100;
        return max_impact

    print('''
    Assume your current impact is %s.

    To maximize your impact in 2020, where is your time best spent?

    Becoming more likable, will make your impact grow to %s.
    Increasing your output yields %s.
    Improving your communication skills, gives %s.

    The advise: Work on your communication skills.
    ''' % (
        impact("The Status Quo", 100, 100, 100),
        impact("2X Charisma", 100, 100, 200),
        impact("2X Productivity", 200, 100, 100),
        impact("2X Communication", 100, 200, 100)
    ))

def __visualization():
    if __lineno__ == 7:
        def center(label, x):
            return x - (len(label) - 8)*2
        
        def bar(x, title, value, color):
            h = value * 2
            y = 350 - h
            rect(x, y, 50, h, color)
            text(center(title, x), y + h + 20, title)
            text(center(str(value), x), y - 20, round(value))
        
        bar(430, "total impact", max_impact, "lightgrey")
        bar(130, "productivity", productivity * .3, "lightyellow")
        bar(230, "communication", communication * .5, "lightblue")
        bar(330, "charisma", charisma * .2, "pink")
        
        text(center(effort, 200), 420, effort, 32)