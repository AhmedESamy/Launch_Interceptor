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
    
    
def test_calculate_angle():
    pass
def test_triangle_area():
    pass