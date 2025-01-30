import json
from src.decide import decide

def test_decide():
    # Load sample input data with multiple examples
    with open("data/input.json", "r") as f:
        data = json.load(f)
    
    examples = data.get("examples", [])
    
    for example in examples:
        print(f"Testing example: {example['name']}")
        
        # Extract inputs from the current example
        num_points = example["NUMPOINTS"]
        points = example["POINTS"]
        parameters = example["PARAMETERS"]
        lcm = example["LCM"]
        puv = example["PUV"]
        
        # Call the DECIDE function
        launch_decision, intermediate_results = decide(num_points, points, parameters, lcm, puv)
        
        # Validate CMV length and PUM matrix size
        assert len(intermediate_results["CMV"]) == 15, f"CMV should have 15 elements in {example['name']}"
        assert len(intermediate_results["PUM"]) == 15, f"PUM should have 15 rows in {example['name']}"
        assert len(intermediate_results["PUM"][0]) == 15, f"PUM should have 15 columns in {example['name']}"
        
        # Validate the final decision
        assert launch_decision == example["EXPECTED_OUTPUT"], (
            f"Test failed for {example['name']}: "
            f"expected {example['EXPECTED_OUTPUT']}, got {launch_decision}"
        )
        
        print(f"Test passed for {example['name']}")

if __name__ == "__main__":
    test_decide()
