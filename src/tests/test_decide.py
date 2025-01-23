import json
from decide import decide

def test_decide():
    # Load sample input data
    with open("data/input.json", "r") as f:
        data = json.load(f)
    
    # Extract inputs from the JSON
    num_points = data["NUMPOINTS"]
    points = data["POINTS"]
    parameters = data["PARAMETERS"]
    lcm = data["LCM"]
    puv = data["PUV"]
    
    # Call the DECIDE function
    launch_decision, intermediate_results = decide(num_points, points, parameters, lcm, puv)
    
    # Validate CMV length and PUM matrix size
    assert len(intermediate_results["CMV"]) == 15, "CMV should have 15 elements"
    assert len(intermediate_results["PUM"]) == 15, "PUM should have 15 rows"
    assert len(intermediate_results["PUM"][0]) == 15, "PUM should have 15 columns"
    
    # Check the final decision
    assert launch_decision in ["YES", "NO"], "Launch decision should be either YES or NO"
    
    print("All tests passed!")
