"""
 ShannonEntropy 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "ShannonEntropy"
__author = "othererik"

def __algorithm():
    from collections import Counter
    import math
    import random

    def calculate_shannon_entropy(data):
        byte_counts = Counter(data)
        entropy = 0.0
        for count in byte_counts.values():
            frequency = float(count) / len(data)
            entropy = entropy + (frequency * math.log(frequency, 2))
        return -entropy


    test_input = ['elephant',
                  ''.join([chr(random.randint(97, 123)) for _ in range(1000)]),
                  'The quick brown fox jumps over the lazy dog',
                  'aaabbbaaacccaaaddd']

    for x in test_input:
        print('{} -> {}'.format(x[:50], calculate_shannon_entropy(x)))

def __visualization():
    text(50, 60, 'Input   = "{}"'.format(data))
    text(50, 75, 'Entropy = {}'.format(-entropy))