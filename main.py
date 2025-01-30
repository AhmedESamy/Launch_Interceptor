import json
from src.decide import decide

def main():
    # Load the JSON file containing multiple examples
    with open("data/input.json", "r") as f:
        data = json.load(f)
    
    examples = data.get("examples", [])
    
    # Iterate through each example and run the `decide` function
    for example in examples:
        print(f"Running example: {example['name']}")
        
        # Extract inputs from the current example
        num_points = example["NUMPOINTS"]
        points = example["POINTS"]
        parameters = example["PARAMETERS"]
        lcm = example["LCM"]
        puv = example["PUV"]
        
        # Call the DECIDE function
        launch_decision, intermediate_results = decide(num_points, points, parameters, lcm, puv)
        
        # Print the results
        print(f"Expected Output: {example['EXPECTED_OUTPUT']}")
        print(f"Actual Launch Decision: {launch_decision}")
        print(f"Intermediate Results: {intermediate_results}\n")
        
        # Validate the result
        if launch_decision == example["EXPECTED_OUTPUT"]:
            print("Test Passed!")
        else:
            print("Test Failed!")

if __name__ == "__main__":
    main()
