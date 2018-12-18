import os
import string


def check_reaction(unit, adj_unit):
    if unit.swapcase() == adj_unit:
        return True
    else:
        return False


def evaluate_polymer(polymer):
    new_polymer = ''
    for unit in polymer:
        if len(new_polymer):
            adj_unit = new_polymer[-1]
            if check_reaction(unit, adj_unit):
                new_polymer = new_polymer[:-1]
            else:
                new_polymer += unit
        else:
            new_polymer += unit
    return new_polymer


def remove_unit(polymer, unit):
    new_polymer = polymer.replace(unit, '').replace(unit.swapcase(), '')
    return evaluate_polymer(new_polymer)


def main():
    input = os.path.abspath(os.path.join(__file__, os.path.pardir, 'input.txt'))
    with open(input) as f:
        polymer = f.readline().strip()

    new_polymer = evaluate_polymer(polymer)
    print('Part 1:', len(new_polymer))
    reduced_polymers = dict([(unit, len(remove_unit(new_polymer, unit))) for unit in string.ascii_lowercase])
    print('Part 2:', min(reduced_polymers.values()))


if __name__ == '__main__':
    main()