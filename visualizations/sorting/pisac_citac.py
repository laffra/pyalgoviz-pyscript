"""
 pisac_citac 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "pisac_citac"
__author = "jakov.manjkas"

def __algorithm():
    inner = False
    niz = [2, 1, -1, 3, 4, 5]
    brojac = 0
    for x in niz:
        if x > 0 and x % 2:
            brojac += 1
    l = len(niz)
    niz += ["*"] * brojac
    pisac = l + brojac - 1
    citac = l - 1
    inner = True
    while citac >= 0:
        if niz[citac] > 0 and niz[citac] % 2:
            niz[pisac] = niz[citac] + 1
            pisac -= 1
        niz[pisac] = niz[citac]
        pisac -= 1
        citac -= 1

def __visualization():
    for i, c in enumerate(niz):
        if inner and i == citac:
            color = "green"
        elif inner and i == pisac:
            color = "red"
        else:
            color = "white"
        rect(50 + 25*i, 50, 25, 25, fill=color)
        text(56 + 25*i, 60, c)