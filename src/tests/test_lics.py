import pytest
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