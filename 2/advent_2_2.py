from enum import Enum


class Action(Enum):
    ADD = 1
    MULTIPLY = 2
    STOP = 99


def intcode_computer(intcode, initial_noun, initial_verb):
    intcode = intcode.split(",")
    intcode = [int(i) for i in intcode]

    intcode[1] = initial_noun
    intcode[2] = initial_verb

    for opcode_position in range(0, len(intcode), 4):

        opcode = intcode[opcode_position]

        if Action(opcode) == Action.STOP:
            break

        noun = intcode[opcode_position+1]
        verb = intcode[opcode_position+2]
        output_position = intcode[opcode_position+3]

        if Action(opcode) == Action.ADD:
            intcode[output_position] = intcode[noun] + intcode[verb]
        elif Action(opcode) == Action.MULTIPLY:
            intcode[output_position] = intcode[noun] * intcode[verb]
        else:
            break

    return(intcode[0])


def brute_forcer(file_intcode, start_noun, start_verb):
    for i in range(100):
        for j in range(100):
            start_noun = i
            start_verb = j
            output = intcode_computer(file_intcode, start_noun, start_verb)
            if output == 19690720:
                print(start_noun, start_verb)
                return output


with open("input.txt", "r") as input_file:
    file_intcode = input_file.readline()
    start_noun = 0
    start_verb = 0
    output = brute_forcer(file_intcode, start_noun, start_verb)
    print(output)
