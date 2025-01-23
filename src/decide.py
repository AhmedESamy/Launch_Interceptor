from src.compute_lics import compute_lics
from src.utils import compute_pum, compute_fuv

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
