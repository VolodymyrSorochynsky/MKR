def filter_lines(input_file, keyword, output_fine):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    filtered_lines = [line for line in lines if keyword in line]

    with open(output_fine, 'w') as f:
        f.writelines(filtered_lines)


if __name__ == "__main__":
    filter_lines("input.txt", "example", "filtered.txt")
