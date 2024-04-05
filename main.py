def filter_lines(input_file, keyword):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    filtered_lines = [line for line in lines if keyword in line]

    with open("filtered.txt", 'w') as f:
        f.writelines(filtered_lines)


if __name__ == "__main__":
    filter_lines("input.txt", "example")
