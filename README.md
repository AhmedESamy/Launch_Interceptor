# Launch Interceptor Decision System

This project implements a decision-making system to determine whether to launch a missile interceptor. The decision is based on analyzing planar data points, applying Launch Interceptor Conditions (LICs), and evaluating them using logical rules. The system calculates intermediate results like the Conditions Met Vector (CMV), Preliminary Unlocking Matrix (PUM), Final Unlocking Vector (FUV), and ultimately makes the final launch decision.

---

## **Features**
- Evaluate 15 predefined Launch Interceptor Conditions (LICs).
- Compute intermediate matrices and vectors (CMV, PUM, FUV).
- Dynamically configure parameters and data points.
- Output a final "YES" or "NO" launch decision.
- Modular structure for easy extensions and testing.

---

## **Getting Started**

### **Prerequisites**
Before running this project, ensure you have the following installed:
- **Python 3.8+**
- Required Python packages listed in `requirements.txt`.

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/AhmedESamy/DECIDE.git
   cd DECIDE

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

## **Usage**
Run the Program
1. To execute the decision-making process:
   ```bash
   python main.py

2. Run with Custom Input
Provide input and output file paths:

   ```bash
   python main.py --input data/input.json --output results/output.json

3. Run Tests
Execute unit tests:

   ```bash
   pytest src/tests/

4. Run Tests with Verbose Output
   ```bash
   pytest src/tests/ --verbose

## **Project Structure**
   ```bash
   project/
   ├── src/
   │   ├── decide.py              # Main logic for launch decision
   │   ├── compute_lics.py        # Functions to compute LICs
   │   ├── utils.py               # Utility functions
   │   ├── tests/                 # Unit tests
   ├── data/                      # Input and output files
   ├── README.md                  # Documentation
   ├── requirements.txt           # Python dependencies
   └── main.py       
