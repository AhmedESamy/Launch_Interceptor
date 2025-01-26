import pytest, math
import src.utils as utils

@pytest.mark.parametrize("point1, point2, expected_distance", [
    ([1, 0], [7, 0], 6), # Straight line on x-axis
    ([0, -2], [0, 5], 7), # Straight line on y-axis
    ([-14, -4], [18, 2], 2*math.sqrt(265)), # Line crossing two quadrants
    ([7, 7], [7, 7], 0), # point1 == point2
    ([-1e6, 1e6], [3e6, 5e6], 4e6*math.sqrt(2)), # Large numbers
])

def test_distance(point1, point2, expected_distance):
    assert math.isclose(
            utils.distance(point1, point2), expected_distance, rel_tol = 1e-9)

@pytest.mark.parametrize("point1, point2, point3, expected_angle", [
    ([4, 14], [18, 14], [18, 2], math.radians(90)), # Right triangle
    ([-8,8], [14, 10], [26, -8], math.pi - 1.073453610448074), # All points in different quadrants
    ([-4, 6], [-14, 0], [-4, 10], 0.2449786631268), # Small angle
    ([1, 0], [2, 0], [3, 0], math.pi), # A line
    ([7, 0], [1, 2], [7, 0], 0), # point1 == point3
])

def test_calculate_angle(point1, point2, point3, expected_angle):
    assert math.isclose(
        utils.calculate_angle(point1, point2, point3), expected_angle, rel_tol = 1e-6)

def test_calculate_angle_incorrect():
    # Tests that break point1 != point2 or point2 != point3
    assert math.isnan(utils.calculate_angle([1, 2], [1, 2], [0, 0]))
    assert math.isnan(utils.calculate_angle([0, 0], [1, 2], [1, 2]))

@pytest.mark.parametrize("point1, point2, point3, expected_area", [
    ([8, 10], [12, 14], [2, 12], 16), # Triangle in first quadrant
    ([20, 80], [50, -10], [-40, -40], 4500), # Triangle over all quadrants
    ([16, -2], [16, 20], [-10, -2], 286), # Right triangle
    ([10, 10], [20, 20], [-10, -10], 0), # A line
    ([13, 13], [13, 13], [13, 13], 0), # point1=point2=point3
])

def test_triangle_area(point1, point2, point3, expected_area):
    assert math.isclose(
        utils.triangle_area(point1, point2, point3), expected_area, rel_tol = 1e-9)