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

    first_star()
