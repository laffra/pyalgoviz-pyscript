"""
 Strings - Spell/Correct 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Strings - Spell/Correct"
__author = "chris@chrislaffra.com"

def __algorithm():
    # See: http://norvig.com/spell-correct.html    

    import collections
    DICT = ['dog','doggy','cat','kitten']
    NWORDS = collections.defaultdict(int)
    for f in DICT: NWORDS[f] += 1
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def edits1(w1):
        splits     = [(w1[:i], w1[i:]) for i in range(len(w1) + 1)]
        deletes    = [a + b[1:] for a, b in splits if b]
        transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
        replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
        inserts    = [a + c + b     for a, b in splits for c in alphabet]
        return set(deletes + transposes + replaces + inserts)

    def known_edits2(w2):
        return set(e2 for e1 in edits1(w2) for e2 in edits1(e1) if e2 in NWORDS)

    def known(words): return set(w for w in words if w in NWORDS)

    def correct(w):
        candidates = known([w]) or known(edits1(w)) or known_edits2(w) or [w]
        return max(candidates, key=NWORDS.get)

    for target in ["dag", "cot", "smitten", "dogyg"]:
        correction = correct(target)
        print(target, '==>', correction)

def __visualization():
    beep(300+__lineno__*50, 300)

    vars = [[ 'DICT:', DICT],
            [ 'NWORDS:', {k:NWORDS[k] for k in NWORDS}],
            [ 'target:', target],
            [ 'correct:', w1],
            [ 'splits:', splits],
            [ 'deletes:', deletes],
            [ 'transposes:', transposes],
            [ 'replaces:', replaces],
            [ 'inserts:', inserts]]

    for n,var in enumerate(vars):
        name, v = var
        text(10, 80+n*20, name, 14)
        if len(v)>10:
            v = '[' + ','.join(v[:10]) + ', ... %d more]' % (len(v)-10)
        text(120, 80+n*20, v)
    
    text(10, 400, f"Correcting: {target}...", 32)
