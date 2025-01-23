import json
from src.decide import decide

if __name__ == "__main__":
    # Load input data from JSON file
    with open("data/input.json", "r") as f:
        data = json.load(f)

    # Extract inputs from the JSON
    num_points = data["NUMPOINTS"]
    points = data["POINTS"]
    parameters = data["PARAMETERS"]
    lcm = data["LCM"]
    puv = data["PUV"]

    # Call the DECIDE function with intermediate results
    launch_decision, intermediate_results = decide(
        num_points, points, parameters, lcm, puv, return_intermediate=True
    )
    
    # Print the final decision
    print(f"Launch Decision: {launch_decision}")
    
    # Optionally, print intermediate results for debugging or logging
    print("\nIntermediate Results:")
    print(f"Conditions Met Vector (CMV): {intermediate_results['CMV']}")
    print(f"Preliminary Unlocking Matrix (PUM): {intermediate_results['PUM']}")
    print(f"Final Unlocking Vector (FUV): {intermediate_results['FUV']}")
