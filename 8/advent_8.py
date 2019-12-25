from math import ceil, inf


def first_star(image_data):
    min_number_of_zeroes = inf
    image_size = 25*6
    layers = []
    for i in range(ceil(len(image_data) / image_size)):
        layers.append(image_data[(i*image_size):((i+1)*image_size)])
    for layer in layers:
        number_of_zeroes = layer.count('0')
        if number_of_zeroes < min_number_of_zeroes:
            min_number_of_zeroes = number_of_zeroes
            layer_with_least_zeroes = layer

    print(layer_with_least_zeroes.count('1') * layer_with_least_zeroes.count('2'))


def second_star(image_data):
    image_size = 25 * 6
    layers = []
    image = []
    for i in range(ceil(len(image_data) / image_size)):
        layers.append(image_data[(i * image_size):((i + 1) * image_size)])

    first_layer = list(layers[0])
    for digit_index in range(image_size):
        i = 1
        while first_layer[digit_index] == '2':
            first_layer[digit_index] = layers[i][digit_index]
            i += 1

    for digit in first_layer:
        if digit == "0":
            image.append("░")
        elif digit == "1":
            image.append("█")

    for i in range(0, image_size, 26):
        image.insert(i, '\n')

    image = "".join(image)

    print(image)


if __name__ == "__main__":
    with open("input.txt") as input_file:
        input_file_contents = input_file.readline()
        first_star(input_file_contents)
        second_star(input_file_contents)
