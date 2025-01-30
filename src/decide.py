from src.compute_lics import compute_lics

def decide(NUMPOINTS, POINTS, PARAMETERS, LCM, PUV, return_intermediate=True):
    """
    Main function to decide whether to launch or not.

    Args:
        NUMPOINTS (int): Number of planar data points.
        POINTS (list): List of tuples [(x1, y1), (x2, y2), ...].
        PARAMETERS (dict): Parameters for the LICs.
        LCM (list): Logical Connector Matrix.
        PUV (list): Preliminary Unlocking Vector.
        return_intermediate (bool): Whether to return intermediate results (CMV, PUM, FUV).

    Returns:
        str: "YES" if launch is decided, otherwise "NO".
        dict (optional): Intermediate results { "CMV": CMV, "PUM": PUM, "FUV": FUV }.
    """
    # Step 1: Compute the Conditions Met Vector (CMV)
    CMV = compute_lics(NUMPOINTS, POINTS, PARAMETERS)

    # Step 2: Compute the Preliminary Unlocking Matrix (PUM)
    PUM = compute_pum(CMV, LCM)

    # Step 3: Compute the Final Unlocking Vector (FUV)
    FUV = compute_fuv(PUM, PUV)

    # Step 4: Compute the final launch decision
    launch_decision = "YES" if all(FUV) else "NO"

    # Optionally return intermediate results
    if return_intermediate:
        return launch_decision, {"CMV": CMV, "PUM": PUM, "FUV": FUV}
    
    return launch_decision


def compute_pum(CMV, LCM):
    """
    Compute the Preliminary Unlocking Matrix (PUM) based on CMV and LCM.

    Args:
        CMV (list): Conditions Met Vector.
        LCM (list): Logical Connector Matrix.

    Returns:
        list: PUM (Preliminary Unlocking Matrix).
    """
    # Placeholder: Compute PUM based on the logical operators in LCM
    PUM = [[False for _ in range(15)] for _ in range(15)]
    for i in range(0, 15):
        for j in range(0, 15):
            if (LCM[j][i] == 'ANDD'):
                PUM[j][i] = CMV[j] and CMV[i]
            elif (LCM[j][i] == 'ORR'):
                PUM[j][i] = CMV[j] or CMV[i]
            elif (LCM[j][i] == 'NOTUSED'):
                PUM[j][i] = True
    return PUM

def compute_fuv(PUM, PUV):
    """
    Compute the Final Unlocking Vector (FUV).

    Args:
        PUM (list): Preliminary Unlocking Matrix.
        PUV (list): Preliminary Unlocking Vector.

    Returns:
        list: FUV (Final Unlocking Vector).
    """
    FUV = [False] * 15
    
    for i in range(15):
        if PUV[i] == False:
            FUV[i] = True
        else:
            if all(PUM[i][j] for j in range(15)):
                FUV[i] = True
            else:
                FUV[i] = False

    return FUV