import pytest
from src.decide import compute_fuv, compute_pum



@pytest.mark.parametrize(
    "CMV, LCM, expected_pum",
    [
        (
            # 1) All CMV entries are True and all LCM entries are NOTUSED
            [True]*15,
            [["NOTUSED"]*15 for _ in range(15)],
            [[True]*15 for _ in range(15)]
        ),
        (
            # 2) Varying values both in CMV and in LCM
            [True, False, True, True, False, True, False, True, False, True, True, False, True, False, True],
            [
            ["ANDD", "ORR", "NOTUSED", "ANDD", "NOTUSED", "ORR", "ANDD", "ORR", "NOTUSED", "ANDD", "ANDD", "ORR", "NOTUSED", "ANDD", "ORR"],
            ["ORR", "ANDD", "ORR", "NOTUSED", "ANDD", "NOTUSED", "ANDD", "ORR", "NOTUSED", "ANDD", "ORR", "ANDD", "NOTUSED", "ANDD", "ORR"],
            ["NOTUSED", "ORR", "ANDD", "NOTUSED", "ANDD", "ANDD", "ORR", "NOTUSED", "ANDD", "ANDD", "NOTUSED", "ANDD", "ORR", "ANDD", "NOTUSED"],
            ["ANDD", "NOTUSED", "NOTUSED", "ANDD", "ORR", "ANDD", "NOTUSED", "ANDD", "ANDD", "NOTUSED", "NOTUSED", "ORR", "ANDD", "ANDD", "ANDD"],
            ["NOTUSED", "ANDD", "ANDD", "ORR", "ANDD", "NOTUSED", "NOTUSED", "ANDD", "ANDD", "ANDD", "NOTUSED", "NOTUSED", "NOTUSED", "ANDD", "ANDD"],
            ["ORR", "NOTUSED", "ANDD", "ANDD", "NOTUSED", "ANDD", "ORR", "ANDD", "NOTUSED", "ORR", "ANDD", "NOTUSED", "ORR", "NOTUSED", "ORR"],
            ["ANDD", "ANDD", "ORR", "NOTUSED", "NOTUSED", "ORR", "ANDD", "ORR", "ANDD", "NOTUSED", "ANDD", "ORR", "NOTUSED", "NOTUSED", "ANDD"],
            ["ORR", "ORR", "NOTUSED", "ANDD", "ANDD", "ANDD", "ORR", "ANDD", "ANDD", "NOTUSED", "ORR", "ANDD", "ORR", "ANDD", "ORR"],
            ["NOTUSED", "NOTUSED", "ANDD", "NOTUSED", "ANDD", "NOTUSED", "ORR", "ANDD", "NOTUSED", "ORR", "NOTUSED", "ANDD", "ANDD", "ANDD", "NOTUSED"],
            ["ANDD", "ANDD", "ANDD", "NOTUSED", "ANDD", "ORR", "ANDD", "NOTUSED", "ORR", "ANDD", "NOTUSED", "ORR", "NOTUSED", "ANDD", "ANDD"],
            ["ANDD", "ORR", "NOTUSED", "NOTUSED", "NOTUSED", "ANDD", "ORR", "ORR", "NOTUSED", "NOTUSED", "ANDD", "ORR", "NOTUSED", "ORR", "ANDD"],
            ["ORR", "ANDD", "ANDD", "ORR", "NOTUSED", "NOTUSED", "ANDD", "ANDD", "ANDD", "ORR", "ORR", "ANDD", "ANDD", "NOTUSED", "ANDD"],
            ["NOTUSED", "NOTUSED", "ORR", "ANDD", "NOTUSED", "NOTUSED", "ANDD", "ANDD", "ORR", "ANDD", "NOTUSED", "ANDD", "NOTUSED", "ORR", "ORR"],
            ["ANDD", "ANDD", "ANDD", "NOTUSED", "ANDD", "NOTUSED", "NOTUSED", "ANDD", "NOTUSED", "NOTUSED", "NOTUSED", "NOTUSED", "ORR", "ANDD", "NOTUSED"],
            ["ORR", "ORR", "NOTUSED", "ANDD", "ANDD", "ORR", "ANDD", "ANDD", "ORR", "NOTUSED", "NOTUSED", "NOTUSED", "ANDD", "NOTUSED", "ORR"]
            ],
            [[True, True, True, True, True, True, False, True, True, True, True, True, True, False, True],
             [True, False, True, True, False, True, False, True, True, False, True, False, True, False, True],
             [True, True, True, True, False, True, True, True, False, True, True, False, True, False, True],
             [True, True, True, True, True, True, True, True, False, True, True, True, True, False, True],
             [True, False, False, True, False, True, True, False, False, False, True, True, True, False, False],
             [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
             [False, False, True, True, True, True, False, True, False, True, False, False, True, True, False],
             [True, True, True, True, False, True, True, True, False, True, True, False, True, False, True],
             [True, True, False, True, False, True, False, False, True, True, True, False, False, False, True],
             [True, False, True, True, False, True, False, True, True, True, True, True, True, False, True],
             [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
             [True, False, False, True, True, True, False, False, False, True, True, False, False, True, False],
             [True, True, True, True, True, True, False, True, True, True, True, False, True, True, True],
             [False, False, False, True, False, True, True, False, True, True, True, True, True, False, True],
             [True, True, True, True, False, True, False, True, True, True, True, True, True, True, True]]
        ),
        (
            # 3 Test a case where all we and Falses and return a table with all false
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [
            ["ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD"],
            ["ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD"],
            ["ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD"],
            ["ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD"],
            ["ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD"],
            ["ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD"],
            ["ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD"],
            ["ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD"],
            ["ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD"],
            ["ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD"],
            ["ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD"],
            ["ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD"],
            ["ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD"],
            ["ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD"],
            ["ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD", "ANDD"]
            ],
            [[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]]
        )
    ]
)
def test_compute_pum(CMV, LCM, expected_pum):
    result_pum = compute_pum(CMV, LCM)
    assert result_pum == expected_pum


@pytest.mark.parametrize(
    "PUM, PUV, expected_fuv",
    [
        (
            #1) Iterate over all and have all True
            [[True]*15 for _ in range(15)],
            [True]*15,
            [True]*15
        ),
        (
            #2) Have a table filled with just false but get all trues because PUV only has falses
            [[False]*15 for _ in range(15)],
            [False]*15,
            [True]*15
        ),
        (
            #3) Have a table filled with just false but get all trues because PUV only has falses
            [[False]*15 for _ in range(15)],
            [False]*15,
            [True]*15
        ),
        (
            #4) A case where we have a set of both true and false values where we iterate over each row
            [[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, False, True, True, True, True], [True, True, True, True, True, True, True, True, False, False, True, True, True, True, True], [True, True, False, True, True, True, True, True, True, True, True, True, True, True, True], [False, True, True, True, True, True, True, True, True, True, True, True, True, False, True], [True, True, True, True, True, True, True, True, True, True, False, True, True, True, True], [True, False, True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, False, True, True, True, True, True, True, True, True, True, True, False, True], [True, False, True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, False, True, True, True, True, True, True, True, True], [True, True, True, True, True, False, True, True, True, True, True, True, True, True, False], [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, False, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True, False, True, True]],
            [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, False, False, False, False, False, False, False, False, False, False, True, False, False]
        )
    ]
)

def test_compute_fuv(PUM, PUV, expected_fuv):
    result_fuv = compute_fuv(PUM, PUV)
    assert result_fuv == expected_fuv
