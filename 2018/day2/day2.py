import os
from collections import Counter
from itertools import combinations


def checksum(filename):
    with open(filename) as f:
        id_counts = map(Counter, f.readlines())
    twos, threes = 0, 0
    for counts in id_counts:
        if 2 in counts.values():
            twos += 1
        if 3 in counts.values():
            threes += 1
    return twos * threes


def match_ids(filename):
    def one_off(id1, id2):
        id_pairs = zip(id1, id2)
        mask = map(lambda x: x[0] == x[1], id_pairs)
        if sum(mask) == 1:
            mask
            return True, 

    with open(filename) as f:
        ids = f.readlines()

    id_combos = combinations(ids, 2)
    for combo in id_combos:
        match, letters = one_off(combo[1], combo[1])
        if match:
            return letters
    

if __name__ == '__main__':
    pardir = os.path.abspath(os.path.join(__file__, os.path.pardir))
    input = os.path.join(pardir, 'input.txt')

    print('Part 1:', checksum(input))
