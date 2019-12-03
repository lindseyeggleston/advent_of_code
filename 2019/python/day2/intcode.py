from copy import deepcopy


def intcode_decoder(intcode: list) -> list:
    for i in range(0, len(intcode), 4):
        opcode = intcode[i]
        if opcode == 99:
            return intcode
        first_param = intcode[intcode[i + 1]]
        second_param = intcode[intcode[i + 2]]
        third_param = intcode[i + 3]
        if opcode == 1:
            intcode[third_param] = first_param + second_param
        elif opcode == 2:
            intcode[third_param] = first_param * second_param
        else:
            raise ValueError("Unrecognized opcode '{}'".format(opcode))
    return intcode


def main():
    with open("../../data/day2.txt", "r") as f:
        line = f.readline()
        intcode = list(map(int, line.split(",")))
    intcode_ = deepcopy(intcode)
    intcode_[1] = 80  # noun
    intcode_[2] = 18   # verb
    final_intcode = intcode_decoder(intcode_)
    return final_intcode[0]


if __name__ == "__main__":
    print(main())