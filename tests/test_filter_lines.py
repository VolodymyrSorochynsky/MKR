import pytest
import os
from main import filter_lines


def test_filter_lines(input_file, output_file, keyword, expected_lines):
    filter_lines(input_file, keyword, output_file)
    with open(output_file, "r") as f:
        lines = f.readlines()
    assert len(lines) == len(expected_lines)
    for line in expected_lines:
        assert line in lines
