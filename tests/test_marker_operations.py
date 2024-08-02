import os
from unittest import TestCase

from toolbox.marker_operations import read_markers

# Expected map for test_read_markers1
sub_test_map1 = {"\\nam": "*", "\\lng": "Default", "\\mkrOverThis": "name"}
test_map1 = {"\\dt": sub_test_map1}

# Expected map for test_read_markers2
font_sub_test_map2 = {
    "\\Name": "Times New Roman",
    "\\Size": "10",
    "\\charset": "00",
    "\\rgbColor": "128,128,128",
}
sub_test_map2 = {
    "\\nam": "Reference Number",
    "\\lng": "Default",
    "\\fnt": font_sub_test_map2,
    "\\mkrOverThis": "name",
}
test_map2 = {"\\ref": sub_test_map2}

# Expected map for test_read_markers3
test_map3 = {"\\ref": sub_test_map2, "\\dt": sub_test_map1}

# Expected map for test_read_markers4
sub2_test_map4 = {
    "\\nam": "Free Translation",
    "\\lng": "chinese",
    "\\mkrOverThis": "ref",
}
test_map4 = {"\\dt": sub_test_map1, "\\f": sub2_test_map4}


def test_read_markers1():
    # Tests if correctly parses one marker
    # First path is if running in pycharm, second is if running in tox
    path = "./example_test_files/marker_text1.typ"
    if "TOX_ENV_NAME" in os.environ:
        path = "./tests/example_test_files/marker_text1.typ"
    TestCase().assertDictEqual(read_markers(path), test_map1)


def test_read_markers2():
    # Tests if correctly parses one marker with font variables
    path = "./example_test_files/marker_text2.typ"
    if "TOX_ENV_NAME" in os.environ:
        path = "./tests/example_test_files/marker_text2.typ"
    TestCase().assertDictEqual(read_markers(path), test_map2)


def test_read_markers3():
    # Tests if correctly parses two markers, one with font variables
    path = "./example_test_files/marker_text3.typ"
    if "TOX_ENV_NAME" in os.environ:
        path = "./tests/example_test_files/marker_text3.typ"
    TestCase().assertDictEqual(read_markers(path), test_map3)


def test_read_markers4():
    # Tests it correctly parses two markers
    path = "./example_test_files/marker_text4.typ"
    if "TOX_ENV_NAME" in os.environ:
        path = "./tests/example_test_files/marker_text4.typ"
    TestCase().assertDictEqual(read_markers(path), test_map4)
