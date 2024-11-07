def v1_get_counter(s='aba'):
    counter = {}
    for c in s:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1

    print(counter) # For example 'aba' -> {'a': 2, 'b': 1}

from collections import defaultdict
def v2_get_counter(s='aba'):
    counter = defaultdict(int)
    for c in s:
            counter[c] += 1 # This wil normally give an error in a normal dictionary but not in a defaultdict

    print(counter) # For example 'aba' -> defaultdict(<class 'int'>, {'a': 2, 'b': 1})

from collections import Counter
def v3_get_counter(s='aba'):
    counter = Counter(s)

    print(counter) # For example 'aba' -> Counter({'a': 2, 'b': 1})

if __name__ == '__main__':
    v1_get_counter()
    v2_get_counter()
    v3_get_counter()