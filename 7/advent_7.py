from intcode_computer import intcode_computer

def amplifier_controller(intcode):
    outputs = {}

    for a in range(5):
        a_output = intcode_computer(intcode, a, 0)
        for b in range(5):
            b_output = intcode_computer(intcode, b, a_output)
            for c in range(5):
                c_output = intcode_computer(intcode, c, b_output)
                for d in range(5):
                    d_output = intcode_computer(intcode, d, c_output)
                    for e in range(5):
                        e_output = intcode_computer(intcode, e, d_output)
                        # Check that input values are unique
                        if len({str(a), str(b), str(c), str(d), str(e)}) == 5:
                            outputs[str(a) + str(b) + str(c) + str(d) + str(e)] = int(e_output)

    max_output = max(outputs.values())
    print(max_output)

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        file_intcode = input_file.readline()
        amplifier_controller(file_intcode)
