import pytest
from main import filter_lines


@pytest.fixture
def input_file(tmpdir):
    file_path = tmpdir.join("input.txt")
    with open(file_path, "w") as f:
        f.write("cat, lamp, duck\n")
        f.write("dog, ball, tea\n")
        f.write("hair, dog, lamp\n")
        f.write("ball, cat, dog\n")
        f.write("box, tea, lamp\n")
    return file_path


@pytest.fixture
def output_file(tmpdir):
    return tmpdir.join("filtered.txt")


@pytest.mark.parametrize("keyword, expected_lines", [
    ("cat", ["cat, lamp, duck\n", "ball, cat, dog\n"]),
    ("cap", []),
    ("lamp", ["cat, lamp, duck\n", "hair, dog, lamp\n", "box, tea, lamp\n"]),
])
def test_filter_lines(input_file, output_file, keyword, expected_lines):
    filter_lines(input_file, keyword, output_file)
    with open(output_file, "r") as f:
        lines = f.readlines()
    assert len(lines) == len(expected_lines)
    for line in expected_lines:
        assert line in lines


def test_filter_lines_error(tmpdir):
    input_file = tmpdir.join("file_does_not_exist.txt")
    output_file = tmpdir.join("also_does_not_exist.txt")
    with pytest.raises(FileNotFoundError):
        filter_lines(input_file, "example", output_file)