import json
from src.compute_lics import *

# Load sample input data with LIC examples
with open("input_LIC_test.json", "r") as f:
    data = json.load(f)

examples = data.get("examples", [])

def test_lic_0():
    """
    Positive and negative assertion test for LIC 0.
    """

    NUMPOINTS1 = examples[0]['NUMPOINTS']
    POINTS1 = examples[0]['POINTS']
    PARAMETERS1= examples[0]['PARAMETERS']

    NUMPOINTS2 = examples[1]['NUMPOINTS']
    POINTS2 = examples[1]['POINTS']
    PARAMETERS2= examples[1]['PARAMETERS']

    print(f"Testing example: {examples[0]['name']}")
    assert lic_0(NUMPOINTS1, POINTS1, PARAMETERS1) == True

    print(f"Testing example: {examples[1]['name']}")
    assert lic_0(NUMPOINTS2, POINTS2, PARAMETERS2) == False

def test_lic_1():
    """
    Positive and negative assertion test for LIC 0.
    """
    
    NUMPOINTS1 = examples[2]['NUMPOINTS']
    POINTS1 = examples[2]['POINTS']
    PARAMETERS1= examples[2]['PARAMETERS']

    NUMPOINTS2 = examples[3]['NUMPOINTS']
    POINTS2 = examples[3]['POINTS']
    PARAMETERS2= examples[3]['PARAMETERS']

    print(f"Testing example: {examples[2]['name']}")
    assert lic_1(NUMPOINTS1, POINTS1, PARAMETERS1) == True

    print(f"Testing example: {examples[3]['name']}")
    assert lic_1(NUMPOINTS2, POINTS2, PARAMETERS2) == False

def test_lic_2():
    """
    Positive and negative assertion test for LIC 0.
    """

    NUMPOINTS1 = examples[4]['NUMPOINTS']
    POINTS1 = examples[4]['POINTS']
    PARAMETERS1= examples[4]['PARAMETERS']

    NUMPOINTS2 = examples[5]['NUMPOINTS']
    POINTS2 = examples[5]['POINTS']
    PARAMETERS2= examples[5]['PARAMETERS']

    print(f"Testing example: {examples[4]['name']}")
    assert lic_2(NUMPOINTS1, POINTS1, PARAMETERS1) == True

    print(f"Testing example: {examples[5]['name']}")
    assert lic_2(NUMPOINTS2, POINTS2, PARAMETERS2) == False

def test_lic_3():
    """
    Positive and negative assertion test for LIC 0.
    """

    NUMPOINTS1 = examples[6]['NUMPOINTS']
    POINTS1 = examples[6]['POINTS']
    PARAMETERS1= examples[6]['PARAMETERS']

    NUMPOINTS2 = examples[7]['NUMPOINTS']
    POINTS2 = examples[7]['POINTS']
    PARAMETERS2= examples[7]['PARAMETERS']

    print(f"Testing example: {examples[6]['name']}")
    assert lic_3(NUMPOINTS1, POINTS1, PARAMETERS1) == True

    print(f"Testing example: {examples[7]['name']}")
    assert lic_3(NUMPOINTS2, POINTS2, PARAMETERS2) == False

def test_lic_4():
    """
    Positive and negative assertion test for LIC 0.
    """

    NUMPOINTS1 = examples[8]['NUMPOINTS']
    POINTS1 = examples[8]['POINTS']
    PARAMETERS1= examples[8]['PARAMETERS']

    NUMPOINTS2 = examples[9]['NUMPOINTS']
    POINTS2 = examples[9]['POINTS']
    PARAMETERS2= examples[9]['PARAMETERS']

    print(f"Testing example: {examples[8]['name']}")
    assert lic_4(NUMPOINTS1, POINTS1, PARAMETERS1) == True

    print(f"Testing example: {examples[9]['name']}")
    assert lic_4(NUMPOINTS2, POINTS2, PARAMETERS2) == False

if __name__ == "__main__":
    test_lic_0()
    test_lic_1()
    test_lic_2()
    test_lic_3()
    test_lic_4()