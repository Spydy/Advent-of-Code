from enum import Enum


class Action(Enum):
    ADD = 1
    MULTIPLY = 2
    STOP = 99


def intcode_computer(intcode):
    intcode = intcode.split(",")
    intcode = [int(i) for i in intcode]

    intcode[1] = 12
    intcode[2] = 2

    for opcode_position in range(0, len(intcode), 4):

        opcode = intcode[opcode_position]
        input_position_1 = intcode[opcode_position+1]
        input_position_2 = intcode[opcode_position+2]
        output_position = intcode[opcode_position+3]

        if Action(opcode) == Action.ADD:
            intcode[output_position] = intcode[input_position_1] + intcode[input_position_2]
        elif Action(opcode) == Action.MULTIPLY:
            intcode[output_position] = intcode[input_position_1] * intcode[input_position_2]
        elif Action(opcode) == Action.STOP:
            break
        else:
            break

    print(intcode[0])


with open("input.txt", "r") as input_file:
    file_intcode = input_file.readline()
    intcode_computer(file_intcode)
