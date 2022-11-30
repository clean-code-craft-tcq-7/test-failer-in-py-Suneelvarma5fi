
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            pair_number = i * 5 + j
            print(f'{pair_number} | {major} | {minor}')
    return pair_number


result = print_color_map()
assert(result == 25)
print("All is well (maybe!)\n")
