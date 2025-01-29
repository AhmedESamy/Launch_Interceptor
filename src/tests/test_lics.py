import pytest
import math
import json
from src.utils import distance, calculate_angle, triangle_area
from src.compute_lics import lic_0, lic_1, lic_2, lic_3, lic_4, lic_5, lic_6, lic_7, lic_8, lic_9
import src.compute_lics as lics

@pytest.mark.parametrize("NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1, expected_result", [
    # (2, 3), (5, 3), (5, 7) gives a triangle of area 6
    # First triplet gives the answer
    (5, [[2, 3], [8, 5], [5, 3], [5, 5], [5, 7]], 1, 1, 5, True),
    # (2, 3), (5, 3), (5, 7) gives a triangle of area 6
    # E_PTS and F_PTS are different and greater than 1
    (11, [[2, 3], [8, 5], [8, 5], [8, 5], [5, 3], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 7]], 3, 5, 5, True),
    # No triplet exists
    (5, [[2, 1], [8, 5], [3, 3], [2, 5], [5, 7]], 1, 1, 5, False),
    # (2, 3), (5, 3), (5, 7) gives a triangle of area 6 
    # Check that equality does not give us true
    (5, [[2, 3], [8, 5], [5, 3], [5, 5], [5, 7]], 1, 1, 6, False),
    # (2, 3), (5, 3), (5, 7) gives a triangle of area 6 
    # Triplets exist but not at the correct spacing
    (5, [[2, 3], [8, 5], [5, 3], [5, 5], [5, 7]], 2, 1, 5, False),
    # NUMPOINTS < 5 is automatic fail
    (3, [[2, 3], [5, 3], [5, 7]], 1, 1, 5, False),
])

def test_lic_10(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1, expected_result):
    assert lics.lic_10(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1) == expected_result
    
@pytest.mark.parametrize("NUMPOINTS, POINTS, G_PTS, expected_result", [
    # (5, 3) and (1, 10) is a valid pair
    # First pair gives the right answer
    (3, [[5, 3], [99, 99], [1, 10]], 1, True),
    # (5, 3) and (1, 10) is a valid pair
    # Last pair gives the right answer
    (5, [[99, 99], [99, 99], [5, 3], [99, 99], [1, 10]], 1, True),
    # No such pair exists
    (5, [[99, 99], [99, 99], [99, 99], [99, 99], [100, 100]], 3, False),
    # (101, 100) and (100, 120) is a valid pair
    # G_PTS is greater than 1
    (6, [[101, 100], [99, 99], [99, 99], [99, 99], [99, 99], [100, 120]], 4, True),
    # NUMPOINTS < 3
    (2, [[5, 4], [3, 8]], 1, False),
])

def test_lic_11(NUMPOINTS, POINTS, G_PTS, expected_result):
    assert lics.lic_11(NUMPOINTS, POINTS, G_PTS) == expected_result

@pytest.mark.parametrize("NUMPOINTS, POINTS, K_PTS, LENGTH1, LENGTH2, expected_result", [
    # First condition satisfied with (8, 2) and (14, 2) >= 5 (LENGTH1)
    # Second condition satisfied with (6, 2) and (8, 2) <= 3 (LENGTH2)
    (5, [[6, 2], [7, 2], [8, 2], [11, 2], [14, 2]], 1, 5, 3, True),
    # Both conditions satisfied with (8, 2) and (14, 2) >= 5 (LENGTH1), <= 7 (LENGTH2)
    (5, [[8, 2], [8, 2], [8, 2], [11, 2], [14, 2]], 1, 5, 7, True),
    # First condition satisfied with (8, 2) and (14, 2) >= 5 (LENGTH1)
    # Second condition satisfied with (6, 2) and (8, 2) <= 3 (LENGTH2)
    # K_PTS > 1
    (11, [[6, 2], [7, 2], [7, 2], [7, 2], [7, 2], [8, 2], [11, 2], [11, 2], [11, 2], [11, 2], [14, 2]], 4, 5, 3, True),
    # No conditions satisfied
    (5, [[6, 2], [7, 2], [8, 2], [11, 2], [14, 2]], 1, 100, 1, False),
    # Only one condition satisfied
    (5, [[6, 2], [7, 2], [8, 2], [11, 2], [14, 2]], 1, 5, 1, False),
    # First condition satisfied with (8, 2) and (14, 2) >= 5 (LENGTH1)
    # Second condition satisfied with (6, 2) and (8, 2) <= 3 (LENGTH2)
    # However, fail due to K_PTS = 2, not allowing it
    (5, [[6, 2], [7, 2], [8, 2], [11, 2], [14, 2]], 2, 5, 3, False),
    # NUMPOINTS < 3 which automatically fails
    (2, [[6, 2], [14, 2]], 1, 1, 1, False),
])

def test_lic_12(NUMPOINTS, POINTS, K_PTS, LENGTH1, LENGTH2, expected_result):
    assert lics.lic_12(NUMPOINTS, POINTS, K_PTS, LENGTH1, LENGTH2) == expected_result
    

@pytest.mark.parametrize("NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2, expected_result", [
    # First condition satisfied with (-3, 3), (5, 5), (5, 7) since r = sqrt(21.25) > 4 (RADIUS1)
    # Second condition satisfied with (5, 5), (5, 7), (3, 5)  since r = sqrt(1.56) <= 2 (RADIUS2)
    (7, [[-3, 3], [0, 0], [5, 5], [0, 0], [5, 7],
         [0, 0], [3, 6]], 1, 1, 1, 3, True),
    # Both conditions satisfied with (3, 6), (5, 5), (5, 7) since r = sqrt(1.56) > 1 (RADIUS1) 
    # and sqrt(1.56) <= 3 (RADIUS2)
    (5, [[3, 6], [0, 0], [5, 5], [0, 0], [5, 7]], 1, 1, 1, 3, True),
    # Both conditions satisfied with a line (4, 8), (8, 8), (12, 8)
    # since r = 4 > 2 (RADIUS1) and <= 5 (RADIUS2)
    (5, [[4, 8], [0, 0], [8, 8], [0, 0], [12, 8]], 1, 1, 2, 5, True),
    # None of the conditions are satisfied
    (5, [[3, 6], [0, 0], [5, 5], [0, 0], [5, 7]], 1, 1, 100, 1, False),
    # Only one condition is satisfied with (3, 6), (5, 5), (5, 7) 
    # since r = sqrt(1.56) <= 3 (RADIUS2), but RADIUS1 = 3 > sqrt(1.56) 
    (5, [[3, 6], [0, 0], [5, 5], [0, 0], [5, 7]], 1, 1, 3, 3, False),
])

def test_lic_13(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2, expected_result):
    assert lics.lic_13(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2) == expected_result
    

@pytest.mark.parametrize("NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1, AREA2, expected_result", [
    # First condition satisfied with (4, 9), (8, 14), (8, 9) since area = 10 > 9 (AREA1) 
    # Second condition satisfied with (11, 12), (10, 11), (11, 11) since area = sqrt(2) < 2 (AREA2)
    (10, [[4, 9], [0, 0], [8, 14], [0, 0], [8, 9],
         [11, 12], [0, 0], [10, 11], [0, 0], [11, 11]], 1, 1, 9, 2, True),
    # Both conditions satisfied with (4, 9), (8, 14), (8, 9) since area = 10 > 9 (AREA1) and < 11 (AREA2)
    (5, [[4, 9], [0, 0], [8, 14], [0, 0], [8, 9]], 1, 1, 9, 11, True),
    # Both conditions satisfied with an area of 0 from (4, 8), (8, 8), (12, 8)
    # since 0 > -1 (AREA1) and 0 < 1 (AREA2)
    (5, [[4, 8], [0, 0], [8, 8], [0, 0], [12, 8]], 1, 1, -1, 1, True),
    # Only one condition satisfied with (4, 9), (8, 14), (8, 9) since area = 10 > 9 (AREA1) but > 8 (AREA2)
    (5, [[4, 9], [0, 0], [8, 14], [0, 0], [8, 9]], 1, 1, 9, 8, False),
    # No condition satisfied
    (5, [[4, 9], [0, 0], [8, 14], [0, 0], [8, 9]], 1, 1, 100, 0, False),
])

def test_lic_14(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1, AREA2, expected_result):
    assert lics.lic_14(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1, AREA2) == expected_result

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

@pytest.mark.parametrize("example_index, expected_result", [
    (10, True),   # LIC 5.1 - X coordinate decreases
    (11, False),  # LIC 5.2 - No decrease in X
])
def test_lic_5(example_index, expected_result):
    example = examples[example_index]
    result = lic_5(example['NUMPOINTS'], example['POINTS'])
    assert result == (example['EXPECTED_OUTPUT'] == "True")

@pytest.mark.parametrize("example_index, expected_result", [
    (12, True),   # LIC 6.1 - Point far from line
    (13, False),  # LIC 6.2 - Point close to line
])
def test_lic_6(example_index, expected_result):
    example = examples[example_index]
    result = lic_6(
        example['NUMPOINTS'],
        example['POINTS'],
        example['PARAMETERS']['N_PTS'],
        example['PARAMETERS']['DIST']
    )
    assert result == (example['EXPECTED_OUTPUT'] == "True")

@pytest.mark.parametrize("example_index, expected_result", [
    (14, True),   # LIC 7.1 - Distance > LENGTH1
    (15, False),  # LIC 7.2 - Distance < LENGTH1
])
def test_lic_7(example_index, expected_result):
    example = examples[example_index]
    result = lic_7(
        example['NUMPOINTS'],
        example['POINTS'],
        example['PARAMETERS']['K_PTS'],
        example['PARAMETERS']['LENGTH1']
    )
    assert result == (example['EXPECTED_OUTPUT'] == "True")

@pytest.mark.parametrize("example_index, expected_result", [
    (16, True),   # LIC 8.1 - Points can't fit in circle
    (17, False),  # LIC 8.2 - Points can fit in circle
])
def test_lic_8(example_index, expected_result):
    example = examples[example_index]
    result = lic_8(
        example['NUMPOINTS'],
        example['POINTS'],
        example['PARAMETERS']['A_PTS'],
        example['PARAMETERS']['B_PTS'],
        example['PARAMETERS']['RADIUS1']
    )
    assert result == (example['EXPECTED_OUTPUT'] == "True")

@pytest.mark.parametrize("example_index, expected_result", [
    (18, True),   # LIC 9.1 - Angle < PI-EPSILON
    (19, False),  # LIC 9.2 - Angle = PI
])
def test_lic_9(example_index, expected_result):
    example = examples[example_index]
    result = lic_9(
        example['NUMPOINTS'],
        example['POINTS'],
        example['PARAMETERS']['C_PTS'],
        example['PARAMETERS']['D_PTS'],
        example['PARAMETERS']['EPSILON']
    )
    expected = (example['EXPECTED_OUTPUT'] == "True")
    assert result == expected, f"Expected {expected} but got {result}"