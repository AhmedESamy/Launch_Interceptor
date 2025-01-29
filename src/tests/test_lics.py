import pytest
import src.utils as utils
import src.compute_lics as lics

@pytest.mark.parametrize("NUMPOINTS, POINTS, LENGTH1, expected_result", [
    # LIC 0.1 Test - Distance between [-1,0] and [2,1] is greater than LENGTH1=2
    # Expected to give True
    (3, [[-1, 0], [2, 1], [0, -1]], 2, True),
    # LIC 0.2 Test - Distance between [1,0] and [0,1] is lesser than LENGTH1=2
    # Expected to give False
    (3, [[1, 0], [0, 1], [0, 0]], 2, False),
])

def test_lic_0(NUMPOINTS, POINTS, LENGTH1, expected_result):
    assert lics.lic_0(NUMPOINTS, POINTS, LENGTH1) == expected_result


@pytest.mark.parametrize("NUMPOINTS, POINTS, RADIUS1, expected_result", [
    # LIC 1.1 Test - Points [-1,0], [1,0], [0,-2] can't be contained by RADIUS1=1
    # Expected to give True
    (3, [[-1, 0], [1, 0], [0, -2]], 1, True),
    # LIC 1.2 Test - Points [-1,0], [1,0], [-1,0] can be contained by RADIUS1=1
    # Expected to give False
    (3, [[-1, 0], [1, 0], [-1, 0]], 1, False),
])

def test_lic_1(NUMPOINTS, POINTS, RADIUS1, expected_result):
    assert lics.lic_1(NUMPOINTS, POINTS, RADIUS1) == expected_result


@pytest.mark.parametrize("NUMPOINTS, POINTS, EPSILON, expected_result", [
    # LIC 2.1 Test - [1,0],[0,0],[0,1] forms valid pi/2 angle.
    # Expected to give True
    (3, [[1, 0], [0, 0], [0, 1]], 0.1, True), 
    # LIC 2.2 Test - Coinciding points form no angle.
    # Expected to give False
    (3, [[0, 0], [0, 0], [0, 0]], 0.1, False), 
])

def test_lic_2(NUMPOINTS, POINTS, EPSILON, expected_result):
    assert lics.lic_2(NUMPOINTS, POINTS, EPSILON) == expected_result


@pytest.mark.parametrize("NUMPOINTS, POINTS, AREA1, expected_result", [
    # LIC 3.1 Test - Vertices in [-1,0],[1,0],[0,-2] creates a surface area of 2 > AREA1=1.9
    # Expected to give True
    (3, [[-1, 0], [1, 0], [0, -2]], 1.9, True), 
    # LIC 3.2 Test - Coinciding points results in no surface area
    # Expected to give False
    (3, [[0, 0], [0, 0], [0, 0]], 3, False), 
])

def test_lic_3(NUMPOINTS, POINTS, AREA1, expected_result):
    assert lics.lic_3(NUMPOINTS, POINTS, AREA1) == expected_result


@pytest.mark.parametrize("NUMPOINTS, POINTS, Q_PTS, QUADS, expected_result", [
    # LIC 4.1 Test - [-1,0],[1,0],[0,-2] contains Q_PTS=3 consecutive elements in more than QUADS=2 different quadrants
    # Expected to give True
    (3, [[-1, 0], [1, 0], [0, -2]], 3, 2, True),
    # LIC 4.2 Test - [0,1],[1,0],[0,0] all belong to the same quadrant.
    # Expected to give False
    (3, [[0, 1], [1, 0], [0, 0]], 3, 2, False), 
])

def test_lic_4(NUMPOINTS, POINTS, Q_PTS, QUADS, expected_result):
    assert lics.lic_4(NUMPOINTS, POINTS, Q_PTS, QUADS) == expected_result


@pytest.mark.parametrize("NUMPOINTS, POINTS, expected_result", [
    # LIC 5.1 Test - when X decreases from 2 to 1
    # Expected to give True
    (3, [[2, 0], [1, 0], [3, 0]], True),
    # LIC 5.2 Test - When there is no decrease
    # Expected to give False
    (3, [[1, 0], [2, 0], [3, 0]], False),
])

def test_lic_5(NUMPOINTS, POINTS, expected_result):
    assert lics.lic_5(NUMPOINTS, POINTS) == expected_result


@pytest.mark.parametrize("NUMPOINTS, POINTS, N_PTS, DIST, expected_result", [
    # LIC 6.1 Test - when point (1,2) is > DIST of 1.0 from line
    # Expected to give True
    (5, [[0, 0], [1, 2], [1, 0],[3, 3], [4, 4]], 3, 1.0, True),
    # LIC 6.2 Test - when point (1,0.5) is < DIST of 1.0 from line
    # Expected to give False
    (3, [[0, 0], [1, 0.5], [2, 0]], 3, 1.0, False),
])

def test_lic_6(NUMPOINTS, POINTS, N_PTS, DIST, expected_result):
    assert lics.lic_6(NUMPOINTS, POINTS, N_PTS, DIST) == expected_result


@pytest.mark.parametrize("NUMPOINTS, POINTS, K_PTS, LENGTH1, expected_result", [
    # LIC 7.1 Test - Distance from [0,0] to [5,5] > length1 of 7
    # Expected to give True
    (5, [[0, 0], [1, 1], [2, 2], [5, 5], [6, 6]], 2, 7.0, True),
    # LIC 7.2 Test - Distance from [0,0] to [3,3] < length1 of 5
    # Expected to give False
    (5, [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]], 2, 5.0, False),
])

def test_lic_7(NUMPOINTS, POINTS, K_PTS, LENGTH1, expected_result):
    assert lics.lic_7(NUMPOINTS, POINTS, K_PTS, LENGTH1) == expected_result


@pytest.mark.parametrize("NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, expected_result", [
    # LIC 8.1 Test - [0,0], [2,0],[4,4] can't fit in circle: R = 2.52 > 1
    # Expected to give True
    (5, [[0, 0], [1, 0], [2, 0],[3, 0], [4, 4]], 1, 1, 1.0, True),
    # LIC 8.2 Test - [0, 0], [2, 0],[1, 1.1732] can fit in circle: R = 1.15 < 2
    # Expected to give False
    (5, [[0, 0], [0, 1], [2, 0],[4, 0],[1, 1.1732]], 1, 1, 2.0, False),
])

def test_lic_8(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, expected_result):
    assert lics.lic_8(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1) == expected_result


@pytest.mark.parametrize("NUMPOINTS, POINTS, C_PTS, D_PTS, EPSILON, expected_result", [
    # LIC 9.1 Test - [1, 1], [3, 0], [5, 1] forms 2.214 radians < PI-EPSILON (2.642)
    # Expected to give True
    (5, [[1, 1], [2, 2], [3, 0],[4, 4], [5, 1]], 1, 1, 0.5, True),
    # LIC 9.2 Test - [1, 1], [3, 3], [5, 5] forms PI radians (180 degree) = PI > PI - EPSILON
    # Expected to give False
    (5, [[1, 1], [2, 2], [3, 3],[4, 4],[5, 5]], 1, 1, 0.5, False),
])

def test_lic_9(NUMPOINTS, POINTS, C_PTS, D_PTS, EPSILON, expected_result):
    assert lics.lic_9(NUMPOINTS, POINTS, C_PTS, D_PTS, EPSILON) == expected_result


@pytest.mark.parametrize("NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1, expected_result", [
    # LIC 10.1 - (2, 3), (5, 3), (5, 7) gives a triangle of area 6
    # First triplet gives the answer
    (5, [[2, 3], [8, 5], [5, 3], [5, 5], [5, 7]], 1, 1, 5, True),
    # LIC 10.2 (2, 3), (5, 3), (5, 7) gives a triangle of area 6
    # E_PTS and F_PTS are different and greater than 1
    (11, [[2, 3], [8, 5], [8, 5], [8, 5], [5, 3], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 7]], 3, 5, 5, True),
    # LIC 10.3 - No triplet exists
    (5, [[2, 1], [8, 5], [3, 3], [2, 5], [5, 7]], 1, 1, 5, False),
    # LIC 10.4 - (2, 3), (5, 3), (5, 7) gives a triangle of area 6 
    # Check that equality does not give us true
    (5, [[2, 3], [8, 5], [5, 3], [5, 5], [5, 7]], 1, 1, 6, False),
    # LIC 10.5 - (2, 3), (5, 3), (5, 7) gives a triangle of area 6 
    # Triplets exist but not at the correct spacing
    (6, [[2, 3], [8, 5], [5, 3], [5, 5], [5, 7], [5, 7]], 2, 1, 5, False),
])

def test_lic_10(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1, expected_result):
    assert lics.lic_10(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1) == expected_result

def test_assert_lic_10():
    # LIC 10.6 - Breaks contract E_PTS >= 1, E_PTS = 0
    # Gives assertionError
    with pytest.raises(AssertionError) as assertInfo:
        lics.lic_10(5, [[2, 3], [8, 5], [5, 3], [5, 5], [5, 7]], 0, 1, 5)
        assert "E_PTS" in str(assertInfo.value)
    # LIC 10.7 - Break contract F_PTS >= 1, F_PTS = 0
    # Gives assertionError
    with pytest.raises(AssertionError) as assertInfo:
        lics.lic_10(5, [[2, 3], [8, 5], [5, 3], [5, 5], [5, 7]], 1, 0, 5)
        assert "F_PTS" in str(assertInfo.value)
    # LIC 10.8 - Breaks contract E_PTS + F_PTS <= NUMPOINTS - 3
    #            since E_PTS + F_PTS = 2 + 1 = 3, wheras NUMPOINTS - 3 = 2
    # Gives assertionError
    with pytest.raises(AssertionError) as assertInfo:
        lics.lic_10(5, [[2, 3], [8, 5], [5, 3], [5, 5], [5, 7]], 2, 1, 5)
        assert "Sum of E_PTS and F_PTS" in str(assertInfo.value)
   
    
@pytest.mark.parametrize("NUMPOINTS, POINTS, G_PTS, expected_result", [
    # LIC 11.1 - (5, 3) and (1, 10) is a valid pair
    # First pair gives the right answer
    (3, [[5, 3], [99, 99], [1, 10]], 1, True),
    # LIC 11.2 - (5, 3) and (1, 10) is a valid pair
    # Last pair gives the right answer
    (5, [[99, 99], [99, 99], [5, 3], [99, 99], [1, 10]], 1, True),
    # LIC 11.3 - No such pair exists
    (5, [[99, 99], [99, 99], [99, 99], [99, 99], [100, 100]], 3, False),
    # LIC 11.4 - (101, 100) and (100, 120) is a valid pair
    # G_PTS is greater than 1
    (6, [[101, 100], [99, 99], [99, 99], [99, 99], [99, 99], [100, 120]], 4, True),
])

def test_lic_11(NUMPOINTS, POINTS, G_PTS, expected_result):
    assert lics.lic_11(NUMPOINTS, POINTS, G_PTS) == expected_result

def test_assert_lic_11():
    # LIC 11.5 - Breaks 1 <= G_PTS <= NUMPOINTS - 2, G_PTS = 0
    # Gives assertionError
    with pytest.raises(AssertionError) as assertInfo:
        lics.lic_11(5, [[5, 4], [3, 8], [5, 4], [3, 8], [5, 4]], 0)
        assert "G_PTS" in str(assertInfo.value)
    # LIC 11.6 - Breaks 1 <= G_PTS <= NUMPOINTS - 2, G_PTS = NUMPOINTS
    # Gives assertionError
    with pytest.raises(AssertionError) as assertInfo:
        lics.lic_11(5, [[5, 4], [3, 8], [5, 4], [3, 8], [5, 4]], 5)
        assert "G_PTS" in str(assertInfo.value)

@pytest.mark.parametrize("NUMPOINTS, POINTS, K_PTS, LENGTH1, LENGTH2, expected_result", [
    # LIC 12.1
    # First condition satisfied with (8, 2) and (14, 2) >= 5 (LENGTH1)
    # Second condition satisfied with (6, 2) and (8, 2) <= 3 (LENGTH2)
    (5, [[6, 2], [7, 2], [8, 2], [11, 2], [14, 2]], 1, 5, 3, True),
    # LIC 12.2
    # Both conditions satisfied with (8, 2) and (14, 2) >= 5 (LENGTH1), <= 7 (LENGTH2)
    (5, [[8, 2], [8, 2], [8, 2], [11, 2], [14, 2]], 1, 5, 7, True),
    # LIC 12.3
    # First condition satisfied with (8, 2) and (14, 2) >= 5 (LENGTH1)
    # Second condition satisfied with (6, 2) and (8, 2) <= 3 (LENGTH2)
    # K_PTS > 1
    (11, [[6, 2], [7, 2], [7, 2], [7, 2], [7, 2], [8, 2], [11, 2], [11, 2], [11, 2], [11, 2], [14, 2]], 4, 5, 3, True),
    # LIC 12.4
    # No conditions satisfied
    (5, [[6, 2], [7, 2], [8, 2], [11, 2], [14, 2]], 1, 100, 1, False),
    # LIC 12.5
    # Only one condition satisfied
    (5, [[6, 2], [7, 2], [8, 2], [11, 2], [14, 2]], 1, 5, 1, False),
    # LIC 12.6
    # First condition satisfied with (8, 2) and (14, 2) >= 5 (LENGTH1)
    # Second condition satisfied with (6, 2) and (8, 2) <= 3 (LENGTH2)
    # However, fail due to K_PTS = 2, not allowing it
    (5, [[6, 2], [7, 2], [8, 2], [11, 2], [14, 2]], 2, 5, 3, False),
    # LIC 12.7
    # NUMPOINTS < 3 which automatically fails
    (2, [[6, 2], [14, 2]], 1, 1, 1, False),
])

def test_lic_12(NUMPOINTS, POINTS, K_PTS, LENGTH1, LENGTH2, expected_result):
    assert lics.lic_12(NUMPOINTS, POINTS, K_PTS, LENGTH1, LENGTH2) == expected_result

def test_assert_lic_12():
    # LIC 12.8 - Breaks LENGTH2 >= 0, LENGTH2 = -1
    # Gives assertionError
    with pytest.raises(AssertionError) as assertInfo:
        lics.lic_12(5, [[6, 2], [7, 2], [8, 2], [11, 2], [14, 2]], 1, 5, -1)
        assert "LENGTH2" in str(assertInfo.value)  

@pytest.mark.parametrize("NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2, expected_result", [
    # LIC 13.1
    # First condition satisfied with (-3, 3), (5, 5), (5, 7) since r = sqrt(21.25) > 4 (RADIUS1)
    # Second condition satisfied with (5, 5), (5, 7), (3, 5)  since r = sqrt(1.56) <= 2 (RADIUS2)
    (7, [[-3, 3], [0, 0], [5, 5], [0, 0], [5, 7],
         [0, 0], [3, 6]], 1, 1, 1, 3, True),
    # LIC 13.2
    # Both conditions satisfied with (3, 6), (5, 5), (5, 7) since r = sqrt(1.56) > 1 (RADIUS1) 
    # and sqrt(1.56) <= 3 (RADIUS2)
    (5, [[3, 6], [0, 0], [5, 5], [0, 0], [5, 7]], 1, 1, 1, 3, True),
    # LIC 13.3
    # Both conditions satisfied with a line (4, 8), (8, 8), (12, 8)
    # since r = 4 > 2 (RADIUS1) and <= 5 (RADIUS2)
    (5, [[4, 8], [0, 0], [8, 8], [0, 0], [12, 8]], 1, 1, 2, 5, True),
    # LIC 13.4
    # None of the conditions are satisfied
    (5, [[3, 6], [0, 0], [5, 5], [0, 0], [5, 7]], 1, 1, 100, 1, False),
    # LIC 13.5
    # Only one condition is satisfied with (3, 6), (5, 5), (5, 7) 
    # since r = sqrt(1.56) <= 3 (RADIUS2), but RADIUS1 = 3 > sqrt(1.56) 
    (5, [[3, 6], [0, 0], [5, 5], [0, 0], [5, 7]], 1, 1, 3, 3, False),
])

def test_lic_13(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2, expected_result):
    assert lics.lic_13(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2) == expected_result

def test_assert_lic_13():
    # LIC 13.6 - Breaks RADIUS2 >= 0, RADIUS2 = -1
    # Gives assertionError
    with pytest.raises(AssertionError) as assertInfo:
        lics.lic_13(5, [[3, 6], [0, 0], [5, 5], [0, 0], [5, 7]], 1, 1, 1, -1)
        assert "RADIUS2" in str(assertInfo.value)     

@pytest.mark.parametrize("NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1, AREA2, expected_result", [
    # LIC 14.1
    # First condition satisfied with (4, 9), (8, 14), (8, 9) since area = 10 > 9 (AREA1) 
    # Second condition satisfied with (11, 12), (10, 11), (11, 11) since area = sqrt(2) < 2 (AREA2)
    (10, [[4, 9], [0, 0], [8, 14], [0, 0], [8, 9],
         [11, 12], [0, 0], [10, 11], [0, 0], [11, 11]], 1, 1, 9, 2, True),
    # LIC 14.2
    # Both conditions satisfied with (4, 9), (8, 14), (8, 9) since area = 10 > 9 (AREA1) and < 11 (AREA2)
    (5, [[4, 9], [0, 0], [8, 14], [0, 0], [8, 9]], 1, 1, 9, 11, True),
    # LIC 14.3
    # Both conditions satisfied with an area of 0 from (4, 8), (8, 8), (12, 8)
    # since 0 > -1 (AREA1) and 0 < 1 (AREA2)
    (5, [[4, 8], [0, 0], [8, 8], [0, 0], [12, 8]], 1, 1, -1, 1, True),
    # LIC 14.4
    # Only one condition satisfied with (4, 9), (8, 14), (8, 9) since area = 10 > 9 (AREA1) but > 8 (AREA2)
    (5, [[4, 9], [0, 0], [8, 14], [0, 0], [8, 9]], 1, 1, 9, 8, False),
    # LIC 14.5
    # No condition satisfied
    (5, [[4, 9], [0, 0], [8, 14], [0, 0], [8, 9]], 1, 1, 100, 0, False),
])

def test_lic_14(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1, AREA2, expected_result):
    assert lics.lic_14(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1, AREA2) == expected_result