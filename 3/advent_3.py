from enum import Enum
import math

wire1_position = [0, 0]
wire2_position = [0, 0]

wire1_path = [[0, 0]]
wire2_path = [[0, 0]]

intersection_points = []


class Axis(Enum):
    X_POSITIVE = "R"
    X_NEGATIVE = "L"
    Y_POSITIVE = "U"
    Y_NEGATIVE = "D"


def path_mapper(path):
    wire_position = [0, 0]
    wire_path = []
    i = 0

    for instruction in path:
        if Axis(instruction[0]) == Axis.X_POSITIVE:
            wire_position[0] = wire_position[0] + int(instruction[1:])

        elif Axis(instruction[0]) == Axis.X_NEGATIVE:
            wire_position[0] = wire_position[0] - int(instruction[1:])

        elif Axis(instruction[0]) == Axis.Y_POSITIVE:
            wire_position[1] = wire_position[1] + int(instruction[1:])

        elif Axis(instruction[0]) == Axis.Y_NEGATIVE:
            wire_position[1] = wire_position[1] - int(instruction[1:])

        else:
            raise Exception("Invalid direction instruction")

        if i == 0:
            wire_path.append([(0, 0), (wire_position[0], wire_position[1])])
        else:
            wire_path.append([wire_path[i-1][1], (wire_position[0], wire_position[1])])

        i += 1

    return wire_path


def intersection_checker(line1, line2):
    x_diff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    y_diff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(x_diff, y_diff)
    if div == 0:
        return False

    d = (det(*line1), det(*line2))
    x = int(det(d, x_diff) / div)
    y = int(det(d, y_diff) / div)

    def distance(a, b):
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    def is_between(a, c, b):
        return distance(a, c) + distance(c, b) == distance(a, b)

    point = (x, y)
    first_check = is_between(line1[0], point, line1[1])
    second_check = is_between(line2[0], point, line2[1])

    if first_check and second_check:
        return point


def shortest_manhattan_distance(point_list):
    shortest_found_distance = abs(point_list[0][0]) + abs(point_list[0][1])
    for points in point_list:
        distance = abs(points[0]) + abs(points[1])
        if distance < shortest_found_distance:
            shortest_found_distance = distance

    return shortest_found_distance


with open("input.txt", "r") as input_file:
    wire1_path = input_file.readline()
    wire1_path = wire1_path.split(",")
    wire1_path = path_mapper(wire1_path)

    wire2_path = input_file.readline()
    wire2_path = wire2_path.split(",")
    wire2_path = path_mapper(wire2_path)

    for line_1 in wire1_path:
        for line_2 in wire2_path:
            intersection_point = intersection_checker(line_1, line_2)
            if intersection_point:
                intersection_points.append(intersection_point)

    print(shortest_manhattan_distance(intersection_points))
