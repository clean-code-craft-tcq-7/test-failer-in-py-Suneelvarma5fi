color_hashMap = {}

def format_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major_color in enumerate(major_colors):
        for j, minor_color in enumerate(minor_colors):
            color_hashMap[i * 5 + j] =  '| ' +  major_color + ' | ' + minor_color

def print_color_map():
    format_color_map()
    print(color_hashMap)
