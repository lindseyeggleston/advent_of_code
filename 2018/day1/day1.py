import os


def get_changelog(filename):
    with open(filename) as f:
        changelog = map(int, f.readlines())
    return list(changelog)

def change_frequency(changelog):
    return sum(changelog)

def repeat_frequency(changelog):
    current_freq, past_frequencies, soln = 0, set([]), None
    def repeat(changelog, current_freq, past_frequencies):
        for change in changelog:
            current_freq += change
            if current_freq in past_frequencies:
                return current_freq, current_freq
            else:
                past_frequencies.add(current_freq)
        return None, current_freq
    while soln is None:
        soln, current_freq = repeat(changelog, current_freq, past_frequencies)
    return soln


if __name__ == '__main__':
    pardir = os.path.abspath(os.path.join(__file__, os.path.pardir))
    input = os.path.join(pardir, 'input.txt')

    changelog = get_changelog(input)
    print('Part 1:', change_frequency(changelog))
    print('Part 2:', repeat_frequency(changelog))
