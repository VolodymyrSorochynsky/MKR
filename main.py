def filter_lines(input_file, keyword, output_fine):
    """
        Function takes the path to the input file, a keyword, and the path to the output file.
        Reads the contents of the input file and writes into the output file all lines that contain the specified
        keyword.

        Parameters:
        input_file (str): The path to the input file with the extension ".txt".
        keyword (str): The keyword to search for in the lines of the input file.
        output_file (str): The path to the output file with the extension ".txt", where the filtered lines will be
        written.

        Returns:
        None

        Raises:
        FileNotFoundError: If the input file does not exist.

        Example:
        >>> filter_lines("input.txt", "example", "filtered.txt")
        """
    with open(input_file, 'r') as f:
        lines = f.readlines()

    filtered_lines = [line for line in lines if keyword in line]

    with open(output_fine, 'w') as f:
        f.writelines(filtered_lines)


if __name__ == "__main__":
    filter_lines("input.txt", "example", "filtered.txt")
