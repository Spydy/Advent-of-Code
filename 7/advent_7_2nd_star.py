from itertools import permutations

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


class Intcode_computer():

    def __init__(self, intcode, phase_setting, amplifier_input):
        self.intcode = intcode.split(",")
        self.phase_setting = phase_setting
        self.amplifier_input = amplifier_input
        self.output = ""
        self.index = 0
        self.first = True
        self.parameter = ""
        self.opcode = ""
        self.parameter_modes = ""
        self.verb = ""
        self.noun = ""
        self.user_input = ""
        self.output_position = ""
        self.noun_parameter_mode = ""
        self.verb_parameter_mode = ""
        self.done = False

    def compute(self):
        while not self.done:
            self.parameter = str(self.intcode[self.index]).rstrip()

            if len(self.parameter) > 2:
                self.opcode = self.parameter[-2:]
                self.parameter_modes = self.parameter[:-2]
            else:
                self.opcode = self.parameter
                self.parameter_modes = ''

            if self.opcode in Action["STOP"]:
                self.done = True
                break

            elif self.opcode in Action["ADD"]:
                try:
                    self.noun_parameter_mode = self.parameter_modes[-1]
                except IndexError:
                    self.noun_parameter_mode = "0"
                try:
                    self.verb_parameter_mode = self.parameter_modes[-2]
                except IndexError:
                    self.verb_parameter_mode = "0"

                if self.noun_parameter_mode in ParameterMode["POSITION"]:
                    self.noun = int(self.intcode[int(self.intcode[self.index+1])])
                elif self.noun_parameter_mode in ParameterMode["IMMEDIATE"]:
                    self.noun = int(self.intcode[self.index+1])

                if self.verb_parameter_mode in ParameterMode["POSITION"]:
                    self.verb = int(self.intcode[int(self.intcode[self.index+2])])
                elif self.verb_parameter_mode in ParameterMode["IMMEDIATE"]:
                    self.verb = int(self.intcode[self.index+2])

                self.output_position = int(self.intcode[self.index+3])

                self.intcode[self.output_position] = str(self.noun + self.verb)

                self.index = self.index + 4

            elif self.opcode in Action["MULTIPLY"]:
                try:
                    self.noun_parameter_mode = self.parameter_modes[-1]
                except IndexError:
                    self.noun_parameter_mode = "0"
                try:
                    self.verb_parameter_mode = self.parameter_modes[-2]
                except IndexError:
                    self.verb_parameter_mode = "0"

                if self.noun_parameter_mode == ParameterMode["POSITION"]:
                    self.noun = int(self.intcode[int(self.intcode[self.index + 1])])
                elif self.noun_parameter_mode == ParameterMode["IMMEDIATE"]:
                    self.noun = int(self.intcode[self.index + 1])

                if self.verb_parameter_mode == ParameterMode["POSITION"]:
                    self.verb = int(self.intcode[int(self.intcode[self.index + 2])])
                elif self.verb_parameter_mode == ParameterMode["IMMEDIATE"]:
                    self.verb = int(self.intcode[self.index + 2])

                self.output_position = int(self.intcode[self.index + 3])

                self.intcode[self.output_position] = str(self.noun * self.verb)

                self.index = self.index + 4

            elif self.opcode in Action["INPUT"]:
                self.output_position = int(self.intcode[self.index + 1])
                if self.first:
                    self.first = False
                    self.user_input = self.phase_setting
                else:
                    self.user_input = self.amplifier_input
                self.intcode[self.output_position] = str(self.user_input)

                self.index = self.index + 2

            elif self.opcode in Action["OUTPUT"]:
                try:
                    self.noun_parameter_mode = self.parameter_modes[-1]
                except IndexError:
                    self.noun_parameter_mode = "0"

                if self.noun_parameter_mode == ParameterMode["POSITION"]:
                    self.output_position = int(self.intcode[self.index + 1])
                    self.output = self.intcode[self.output_position]
                elif self.noun_parameter_mode == ParameterMode["IMMEDIATE"]:
                    self.output = self.intcode[self.index + 1]

                self.index = self.index + 2
                break

            elif self.opcode in Action["JUMP-IF-TRUE"]:
                try:
                    self.noun_parameter_mode = self.parameter_modes[-1]
                except IndexError:
                    self.noun_parameter_mode = "0"
                try:
                    self.verb_parameter_mode = self.parameter_modes[-2]
                except IndexError:
                    self.verb_parameter_mode = "0"

                if self.noun_parameter_mode == ParameterMode["POSITION"]:
                    self.noun = int(self.intcode[int(self.intcode[self.index + 1])])
                elif self.noun_parameter_mode == ParameterMode["IMMEDIATE"]:
                    self.noun = int(self.intcode[self.index + 1])

                if self.verb_parameter_mode == ParameterMode["POSITION"]:
                    self.verb = int(self.intcode[int(self.intcode[self.index + 2])])
                elif self.verb_parameter_mode == ParameterMode["IMMEDIATE"]:
                    self.verb = int(self.intcode[self.index + 2])

                if self.noun == 0:
                    self.index = self.index + 3
                else:
                    self.index = self.verb

            elif self.opcode in Action["JUMP-IF-FALSE"]:
                try:
                    self.noun_parameter_mode = self.parameter_modes[-1]
                except IndexError:
                    self.noun_parameter_mode = "0"
                try:
                    self.verb_parameter_mode = self.parameter_modes[-2]
                except IndexError:
                    self.verb_parameter_mode = "0"

                if self.noun_parameter_mode == ParameterMode["POSITION"]:
                    self.noun = int(self.intcode[int(self.intcode[self.index + 1])])
                elif self.noun_parameter_mode == ParameterMode["IMMEDIATE"]:
                    self.noun = int(self.intcode[self.index + 1])

                if self.verb_parameter_mode == ParameterMode["POSITION"]:
                    self.verb = int(self.intcode[int(self.intcode[self.index + 2])])
                elif self.verb_parameter_mode == ParameterMode["IMMEDIATE"]:
                    self.verb = int(self.intcode[self.index + 2])

                if self.noun == 0:
                    self.index = self.verb
                else:
                    self.index = self.index + 3

            elif self.opcode in Action["IS-LESS"]:
                try:
                    self.noun_parameter_mode = self.parameter_modes[-1]
                except IndexError:
                    self.noun_parameter_mode = "0"
                try:
                    self.verb_parameter_mode = self.parameter_modes[-2]
                except IndexError:
                    self.verb_parameter_mode = "0"

                if self.noun_parameter_mode == ParameterMode["POSITION"]:
                    self.noun = int(self.intcode[int(self.intcode[self.index + 1])])
                elif self.noun_parameter_mode == ParameterMode["IMMEDIATE"]:
                    self.noun = int(self.intcode[self.index + 1])

                if self.verb_parameter_mode == ParameterMode["POSITION"]:
                    self.verb = int(self.intcode[int(self.intcode[self.index + 2])])
                elif self.verb_parameter_mode == ParameterMode["IMMEDIATE"]:
                    self.verb = int(self.intcode[self.index + 2])

                if self.noun < self.verb:
                    self.intcode[int(self.intcode[self.index + 3])] = "1"
                else:
                    self.intcode[int(self.intcode[self.index + 3])] = "0"

                self.index = self.index + 4

            elif self.opcode in Action["IS-EQUAL"]:
                try:
                    self.noun_parameter_mode = self.parameter_modes[-1]
                except IndexError:
                    self.noun_parameter_mode = "0"
                try:
                    self.verb_parameter_mode = self.parameter_modes[-2]
                except IndexError:
                    self.verb_parameter_mode = "0"

                if self.noun_parameter_mode == ParameterMode["POSITION"]:
                    self.noun = int(self.intcode[int(self.intcode[self.index + 1])])
                elif self.noun_parameter_mode == ParameterMode["IMMEDIATE"]:
                    self.noun = int(self.intcode[self.index + 1])

                if self.verb_parameter_mode == ParameterMode["POSITION"]:
                    self.verb = int(self.intcode[int(self.intcode[self.index + 2])])
                elif self.verb_parameter_mode == ParameterMode["IMMEDIATE"]:
                    self.verb = int(self.intcode[self.index + 2])

                if self.noun == self.verb:
                    self.intcode[int(self.intcode[self.index + 3])] = "1"
                else:
                    self.intcode[int(self.intcode[self.index + 3])] = "0"

                self.index = self.index + 4


def amplifier_controller(intcode):
    outputs = {}
    amplifier_settings = list(permutations(range(5, 10), 5))

    for setting in amplifier_settings:
        a_computer = Intcode_computer(intcode, setting[0], 0)
        b_computer = Intcode_computer(intcode, setting[1], 0)
        c_computer = Intcode_computer(intcode, setting[2], 0)
        d_computer = Intcode_computer(intcode, setting[3], 0)
        e_computer = Intcode_computer(intcode, setting[4], 0)

        while not (a_computer.done and b_computer.done and c_computer.done and d_computer.done and e_computer.done):
            a_computer.compute()
            b_computer.amplifier_input = a_computer.output
            b_computer.compute()
            c_computer.amplifier_input = b_computer.output
            c_computer.compute()
            d_computer.amplifier_input = c_computer.output
            d_computer.compute()
            e_computer.amplifier_input = d_computer.output
            e_computer.compute()
            a_computer.amplifier_input = e_computer.output

        outputs[str(setting[0]) + str(setting[1]) + str(setting[2]) + str(setting[3]) + str(setting[4])] = int(e_computer.output)

    max_output = max(outputs.values())
    print(max_output)

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        file_intcode = input_file.readline()
        amplifier_controller(file_intcode)
