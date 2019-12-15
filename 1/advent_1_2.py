import math

total_fuel_need = 0

with open("input.txt", "r") as input_file:
    line = input_file.readline()
    while line:
        module_mass = int(line)
        fuel = math.floor(module_mass / 3) - 2
        total_fuel_need += fuel
        additional_fuel_need = math.floor(fuel / 3) - 2
        while additional_fuel_need > 0:
            total_fuel_need += additional_fuel_need
            additional_fuel_need = math.floor(additional_fuel_need / 3) - 2

        line = input_file.readline()

print(total_fuel_need)
