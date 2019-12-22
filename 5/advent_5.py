from enum import Enum


Action = {
    "ADD": ["01", "1"],
    "MULTIPLY": ["02", "2"],
    "INPUT": ["03", "3"],
    "OUTPUT": ["04", "4"],
    "JUMP-IF-TRUE": ["05", "5"],
    "JUMP-IF-FALSE": ["06", "6"],
    "IS-LESS": ["07", "7"],
    "IS-EQUAL": ["08", "8"],
    "STOP": "99"
}

ParameterMode = {
    "POSITION": "0",
    "IMMEDIATE": "1"
}


def intcode_computer(intcode):
    intcode = intcode.split(",")
    index = 0

    while True:
        parameter = str(intcode[index])

        if len(parameter) > 2:
            opcode = parameter[-2:]
            parameter_modes = parameter[:-2]
        else:
            opcode = parameter
            parameter_modes = ''

        if opcode in Action["STOP"]:
            break

        elif opcode in Action["ADD"]:
            try:
                noun_parameter_mode = parameter_modes[-1]
            except IndexError:
                noun_parameter_mode = "0"
            try:
                verb_parameter_mode = parameter_modes[-2]
            except IndexError:
                verb_parameter_mode = "0"

            if noun_parameter_mode in ParameterMode["POSITION"]:
                noun = int(intcode[int(intcode[index+1])])
            elif noun_parameter_mode in ParameterMode["IMMEDIATE"]:
                noun = int(intcode[index+1])

            if verb_parameter_mode in ParameterMode["POSITION"]:
                verb = int(intcode[int(intcode[index+2])])
            elif verb_parameter_mode in ParameterMode["IMMEDIATE"]:
                verb = int(intcode[index+2])

            output_position = int(intcode[index+3])

            intcode[output_position] = str(noun + verb)

            index = index + 4

        elif opcode in Action["MULTIPLY"]:
            try:
                noun_parameter_mode = parameter_modes[-1]
            except IndexError:
                noun_parameter_mode = "0"
            try:
                verb_parameter_mode = parameter_modes[-2]
            except IndexError:
                verb_parameter_mode = "0"

            if noun_parameter_mode == ParameterMode["POSITION"]:
                noun = int(intcode[int(intcode[index + 1])])
            elif noun_parameter_mode == ParameterMode["IMMEDIATE"]:
                noun = int(intcode[index + 1])

            if verb_parameter_mode == ParameterMode["POSITION"]:
                verb = int(intcode[int(intcode[index + 2])])
            elif verb_parameter_mode == ParameterMode["IMMEDIATE"]:
                verb = int(intcode[index + 2])

            output_position = int(intcode[index + 3])

            intcode[output_position] = str(noun * verb)

            index = index + 4

        elif opcode in Action["INPUT"]:
            output_position = int(intcode[index + 1])
            print("Please give input: ")
            user_input = input()
            intcode[output_position] = str(user_input)

            index = index + 2

        elif opcode in Action["OUTPUT"]:
            try:
                noun_parameter_mode = parameter_modes[-1]
            except IndexError:
                noun_parameter_mode = "0"

            if noun_parameter_mode == ParameterMode["POSITION"]:
                output_position = int(intcode[index + 1])
                print("OUTPUT: " + intcode[output_position])
            elif noun_parameter_mode == ParameterMode["IMMEDIATE"]:
                print("OUTPUT: " + intcode[index + 1])

            index = index + 2

        elif opcode in Action["JUMP-IF-TRUE"]:
            try:
                noun_parameter_mode = parameter_modes[-1]
            except IndexError:
                noun_parameter_mode = "0"
            try:
                verb_parameter_mode = parameter_modes[-2]
            except IndexError:
                verb_parameter_mode = "0"

            if noun_parameter_mode == ParameterMode["POSITION"]:
                noun = int(intcode[int(intcode[index + 1])])
            elif noun_parameter_mode == ParameterMode["IMMEDIATE"]:
                noun = int(intcode[index + 1])

            if verb_parameter_mode == ParameterMode["POSITION"]:
                verb = int(intcode[int(intcode[index + 2])])
            elif verb_parameter_mode == ParameterMode["IMMEDIATE"]:
                verb = int(intcode[index + 2])

            if noun == 0:
                index = index + 3
            else:
                index = verb

        elif opcode in Action["JUMP-IF-FALSE"]:
            try:
                noun_parameter_mode = parameter_modes[-1]
            except IndexError:
                noun_parameter_mode = "0"
            try:
                verb_parameter_mode = parameter_modes[-2]
            except IndexError:
                verb_parameter_mode = "0"

            if noun_parameter_mode == ParameterMode["POSITION"]:
                noun = int(intcode[int(intcode[index + 1])])
            elif noun_parameter_mode == ParameterMode["IMMEDIATE"]:
                noun = int(intcode[index + 1])

            if verb_parameter_mode == ParameterMode["POSITION"]:
                verb = int(intcode[int(intcode[index + 2])])
            elif verb_parameter_mode == ParameterMode["IMMEDIATE"]:
                verb = int(intcode[index + 2])

            if noun == 0:
                index = verb
            else:
                index = index + 3

        elif opcode in Action["IS-LESS"]:
            try:
                noun_parameter_mode = parameter_modes[-1]
            except IndexError:
                noun_parameter_mode = "0"
            try:
                verb_parameter_mode = parameter_modes[-2]
            except IndexError:
                verb_parameter_mode = "0"

            if noun_parameter_mode == ParameterMode["POSITION"]:
                noun = int(intcode[int(intcode[index + 1])])
            elif noun_parameter_mode == ParameterMode["IMMEDIATE"]:
                noun = int(intcode[index + 1])

            if verb_parameter_mode == ParameterMode["POSITION"]:
                verb = int(intcode[int(intcode[index + 2])])
            elif verb_parameter_mode == ParameterMode["IMMEDIATE"]:
                verb = int(intcode[index + 2])

            if noun < verb:
                intcode[int(intcode[index + 3])] = "1"
            else:
                intcode[int(intcode[index + 3])] = "0"

            index = index + 4

        elif opcode in Action["IS-EQUAL"]:
            try:
                noun_parameter_mode = parameter_modes[-1]
            except IndexError:
                noun_parameter_mode = "0"
            try:
                verb_parameter_mode = parameter_modes[-2]
            except IndexError:
                verb_parameter_mode = "0"

            if noun_parameter_mode == ParameterMode["POSITION"]:
                noun = int(intcode[int(intcode[index + 1])])
            elif noun_parameter_mode == ParameterMode["IMMEDIATE"]:
                noun = int(intcode[index + 1])

            if verb_parameter_mode == ParameterMode["POSITION"]:
                verb = int(intcode[int(intcode[index + 2])])
            elif verb_parameter_mode == ParameterMode["IMMEDIATE"]:
                verb = int(intcode[index + 2])

            if noun == verb:
                intcode[int(intcode[index + 3])] = "1"
            else:
                intcode[int(intcode[index + 3])] = "0"

            index = index + 4

with open("input.txt", "r") as input_file:
    file_intcode = input_file.readline()
    intcode_computer(file_intcode)
