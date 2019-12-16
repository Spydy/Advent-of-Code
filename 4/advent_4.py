def first_star():
    password_range = (278384, 824795)

    valid_password_count = 0

    def check_valid(password):
        string_password = str(password)
        double_found = False
        for number in range(1, 6):
            if int(string_password[number]) < int(string_password[number-1]):
                return False
            if int(string_password[number]) == int(string_password[number-1]):
                double_found = True
        if double_found:
            return True

    for password in range(password_range[0], password_range[1]+1):
        if not check_valid(password):
            continue

        valid_password_count += 1

    print(valid_password_count)

def second_star():
    password_range = (278384, 824795)

    valid_password_count = 0

    def check_valid(password):
        string_password = str(password)
        double_found = False

        for number in range(1, 6):
            if int(string_password[number]) < int(string_password[number-1]):
                return False
            if int(string_password[number]) == int(string_password[number-1]):
                try:
                    if int(string_password[number]) != int(string_password[number+1]):
                        if int(string_password[number]) != int(string_password[number - 2]):
                            double_found = True
                except IndexError:
                    if int(string_password[number]) != int(string_password[number-2]):
                        double_found = True
        if double_found:
            return True

    for password in range(password_range[0], password_range[1]+1):
        if not check_valid(password):
            continue

        valid_password_count += 1

    print(valid_password_count)


if __name__ == "__main__":
    first_star()
    second_star()
