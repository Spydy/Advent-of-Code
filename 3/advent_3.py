from enum import Enum

wire1_position = [0, 0]
wire2_position = [0, 0]

intersection_points = []


class Axis(Enum):
    X_POSITIVE = "R"
    X_NEGATIVE = "L"
    Y_POSITIVE = "U"
    Y_NEGATIVE = "D"


with open("input.txt", "r") as input_file:
    wire1_path = input_file.readline()
    wire1_path = wire1_path.split(",")

    wire2_path = input_file.readline()
    wire2_path = wire2_path.split(",")

    for instruction in wire1_path:
        if instruction[0] == Axis.X_POSITIVE:
            pass
        elif instruction[0] == Axis.X_NEGATIVE:
            pass
        elif instruction[0] == Axis.Y_POSITIVE:
            pass
        elif instruction[0] == Axis.Y_NEGATIVE:
            pass
        else:
            raise Exception("Invalid direction instruction")

    print(wire1_path[0])
