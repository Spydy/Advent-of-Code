"""First Star"""
total_orbit_count = 0


def indirect_orbit_check(check_orbitee, orbit_map):
    global total_orbit_count

    for orbitee, orbiter_list in orbit_map:
        if check_orbitee in orbiter_list:
            total_orbit_count += 1
            indirect_orbit_check(orbitee, orbit_map)
            break


def count_orbits(orbit_map):
    global total_orbit_count

    for orbitee, orbiter_list in orbit_map:
        total_orbit_count += len(orbiter_list)
        for repeats in range(len(orbiter_list)):
            indirect_orbit_check(orbitee, orbit_map)

    print(total_orbit_count)


"""Second Star"""
steps = 0
potential_steps = 0
potential_step_list = []


def map_out(check_orbitee, orbit_map):
    global steps
    global potential_step_list

    for orbitee, orbiter_list in orbit_map:
        if check_orbitee in orbiter_list:
            steps += 1
            if "SAN" in orbiter_list:
                print(steps)
                break
            if len(orbiter_list) == 1:
                map_out(orbitee, orbit_map)
            else:
                for i in range(len(orbiter_list)):
                    if orbiter_list[i] != check_orbitee:
                        map_in(orbiter_list[i], orbit_map)
                    potential_step_list = []
                map_out(orbitee, orbit_map)


def map_in(check_orbiter, orbit_map):
    global steps
    global potential_steps
    global potential_step_list

    for orbitee, orbiter_list in orbit_map:
        if check_orbiter == orbitee:
            potential_steps += 1
            if "SAN" in orbiter_list:
                additional_steps = 0
                for number in potential_step_list:
                    additional_steps += number
                print(steps + additional_steps + 1)
                break
            elif len(orbiter_list) == 1:
                if orbiter_list[0] != check_orbiter:
                    map_in(orbiter_list[0], orbit_map)
                potential_steps = 0
            elif range(len(orbiter_list) > 1):
                for i in range(len(orbiter_list)):
                    if orbiter_list[i] != check_orbiter:
                        potential_step_list.append(potential_steps)
                        potential_steps = 0
                        map_in(orbiter_list[i], orbit_map)


def count_distance(orbit_map):
    for orbitee, orbiter_list in orbit_map:
        if "YOU" in orbiter_list:
            map_out(orbitee, orbit_map)
            break


if __name__ == "__main__":
    def first_star():
        with open("input.txt") as orbit_map_file:
            raw_orbit_map = orbit_map_file.readlines()
            raw_orbit_map = [x.strip() for x in raw_orbit_map]
            orbit_dict = {}
            for orbit in raw_orbit_map:
                orbit = orbit.split(")")
                if not orbit_dict.get(orbit[0]):
                    orbit_dict[orbit[0]] = []
                orbit_dict[orbit[0]].append(orbit[1])

            count_orbits(orbit_dict.items())

    def second_star():
        with open("input.txt") as orbit_map_file:
            raw_orbit_map = orbit_map_file.readlines()
            raw_orbit_map = [x.strip() for x in raw_orbit_map]
            orbit_dict = {}
            for orbit in raw_orbit_map:
                orbit = orbit.split(")")
                if not orbit_dict.get(orbit[0]):
                    orbit_dict[orbit[0]] = []
                orbit_dict[orbit[0]].append(orbit[1])

            count_distance(orbit_dict.items())

    first_star()
    second_star()
