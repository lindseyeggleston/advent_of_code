import os
import re
import numpy as np
from collections import namedtuple


def parse_claims(filename):
    def parse_claim(claim):
        Claim = namedtuple('Claim', ['id', 'left', 'top', 'width', 'height'])
        match = re.search(r'#(?P<id>\d+)\s@\s(?P<left>\d+),(?P<top>\d+):\s(?P<width>\d+)x(?P<heigth>\d+)\s*', claim)
        claim_tup = Claim(*map(int, match.groups()))
        return claim_tup

    with open(filename) as f:
        claims = list(map(parse_claim, f.readlines()))

    fabric = np.zeros((1000, 1000))
    for claim in claims:
        fabric[claim.top:claim.top + claim.height, claim.left:claim.left + claim.width] += 1

    return fabric, claims


def count_overlap(fabric):
    return len(np.where(fabric > 1)[0])


def unique_claim(fabric, claims):
    for claim in claims:
        pattern = fabric[claim.top:claim.top + claim.height, claim.left:claim.left + claim.width]
        if len(np.where(pattern != 1)[0]) == 0:
            return claim.id


if __name__ == '__main__':
    pardir = os.path.abspath(os.path.join(__file__, os.path.pardir))
    input = os.path.join(pardir, 'input.txt')

    fabric, claims = parse_claims(input)
    print('Part 1:', count_overlap(fabric))
    print('Part 2:', unique_claim(fabric, claims))
