import pytest
import math
import json
from src.utils import distance, calculate_angle, triangle_area
from src.compute_lics import lic_0, lic_1, lic_2, lic_3, lic_4

# Load sample input data with LIC examples
with open("data/input_LIC_test.json", "r") as f:
    data = json.load(f)

examples = data.get("examples", [])


@pytest.mark.parametrize("point1, point2, expected_distance", [
    ([1, 0], [7, 0], 6),  # Straight line on x-axis
    ([0, -2], [0, 5], 7),  # Straight line on y-axis
    ([-14, -4], [18, 2], 2 * math.sqrt(265)),  # Line crossing two quadrants
    ([7, 7], [7, 7], 0),  # point1 == point2
])
def test_distance(point1, point2, expected_distance):
    result = distance(point1, point2)
    assert math.isclose(result, expected_distance, rel_tol=1e-9)


@pytest.mark.parametrize("point1, point2, point3, expected_angle", [
    ([4, 14], [18, 14], [18, 2], math.radians(90)),  # Right triangle
    ([-8, 8], [14, 10], [26, -8], math.pi - 1.073453610448074),  # All points in different quadrants
    ([1, 0], [2, 0], [3, 0], math.pi),  # A line
])
def test_calculate_angle(point1, point2, point3, expected_angle):
    result = calculate_angle(point1, point2, point3)
    assert math.isclose(result, expected_angle, rel_tol=1e-6)


@pytest.mark.parametrize("point1, point2, point3, expected_area", [
    ([8, 10], [12, 14], [2, 12], 16),  # Triangle in first quadrant
    ([20, 80], [50, -10], [-40, -40], 4500),  # Triangle over all quadrants
    ([10, 10], [20, 20], [-10, -10], 0),  # A line
])
def test_triangle_area(point1, point2, point3, expected_area):
    result = triangle_area(point1, point2, point3)
    assert math.isclose(result, expected_area, rel_tol=1e-9)


@pytest.mark.parametrize("example_index, expected_result", [
    (0, True),  # Positive case for LIC0
    (1, False),  # Negative case for LIC0
])
def test_lic_0(example_index, expected_result):
    example = examples[example_index]
    result = lic_0(example['NUMPOINTS'], example['POINTS'], example['PARAMETERS'])
    assert result == expected_result


@pytest.mark.parametrize("example_index, expected_result", [
    (2, True),  # Positive case for LIC1
    (3, False),  # Negative case for LIC1
])
def test_lic_1(example_index, expected_result):
    example = examples[example_index]
    result = lic_1(example['NUMPOINTS'], example['POINTS'], example['PARAMETERS'])
    assert result == expected_result


@pytest.mark.parametrize("example_index, expected_result", [
    (4, True),  # Positive case for LIC2
    (5, False),  # Negative case for LIC2
])
def test_lic_2(example_index, expected_result):
    example = examples[example_index]
    result = lic_2(example['NUMPOINTS'], example['POINTS'], example['PARAMETERS'])
    assert result == expected_result


@pytest.mark.parametrize("example_index, expected_result", [
    (6, True),  # Positive case for LIC3
    (7, False),  # Negative case for LIC3
])
def test_lic_3(example_index, expected_result):
    example = examples[example_index]
    result = lic_3(example['NUMPOINTS'], example['POINTS'], example['PARAMETERS'])
    assert result == expected_result


@pytest.mark.parametrize("example_index, expected_result", [
    (8, True),  # Positive case for LIC4
    (9, False),  # Negative case for LIC4
])
def test_lic_4(example_index, expected_result):
    example = examples[example_index]
    result = lic_4(example['NUMPOINTS'], example['POINTS'], example['PARAMETERS'])
    assert result == expected_result
