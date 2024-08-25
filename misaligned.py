color_map = []
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
            color_map.append(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)

def generate_color_map():
    expected_color_map = []
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors,1):
            print(f'{i * 5 + j} | {major} | {minor}')
            expected_color_map.append(f'{i * 5 + j} | {major} | {minor}')
    return expected_color_map

def test_print_color_map():
    expected_output = generate_color_map()
    global color_map
    for index, (expected, actual) in enumerate(zip(expected_output, color_map)):
        assert(expected == actual)

if __name__ == "__main__":
    print_color_map()
    test_print_color_map()
