from intcode_computer import intcode_computer

def first_star(boost_file):
    print("Hello World")

if __name__ == "__main__":
    with open("input.txt") as input_file:
        input_file_contents = input_file.readline()
        first_star(1)