# Equation Solver and Graphing Tool

Python PySide2 program that solves and graphs two functions together.

### Features
- Find the solutions of any two functions.
- Graph the functions and show the solutions points on the graph.
- Validate inputs and shows reason if input function is invalid.
- Simple and intuitive interface.
- Supports operations: +, -, *, /, ^ or **, sqrt(), log() and log10().

---

## Installation

```sh
# Create and activate a virtual environment
python -m venv venv  # Create venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the program
python src/main.py

# Run the tests
pytest src/tests/test_main.py
```

## User Guide

1) Input the two functions in the text fields.<br>
<img src="https://github.com/user-attachments/assets/fe0025f5-0e56-4205-8e04-e20f91135f3e" width="600"><br>

2) If the solve button turns gray, read the cause of the error and edit the functions.<br>
<img src="https://github.com/user-attachments/assets/3e1cd803-8948-4537-80a7-e98de47bec60" width="600"><br>

3) Click on solve to show the graph and solutions table.<br>
<img src="https://github.com/user-attachments/assets/7573109c-a9a1-47e6-ae86-043a80372e04" width="600"><br>

## Hierarchy of the Program

### GUI

- MainWindow: Contains the main thread of the program where events are handled.
- SolveButton: The button class that handles the button states.
- SolutionsTable: The table class that handless table population and clearing.

### Main Logic

- Function: Contains the Function class that performs tasks to the function like validate and parse.
- Solver: Contains solver function that finds the solutions to the functions.
- Graph: Contains draw_graph function that creates the matplotlib graph and centers the solution points.
- SolverThread: A worker thread that performs the solving logic.

## Program Sequence Diagram

![image](https://github.com/user-attachments/assets/aa064270-51a5-4cbe-86c5-3935a96c77be)

## Testing

- test_solver: Unit test for the solving function to check if the output solutions are correct.
- test_main: End-to-end test for the program, inputs two functions and asserts that the correct solutions are shown on the table and graph.

## Examples

<img src="https://github.com/user-attachments/assets/f399bbac-1702-4de6-8842-5cc2dae5ed2f" width="600"><br>
*working example.*

<img src="https://github.com/user-attachments/assets/d959c278-637c-4a99-98db-57d0b2941c98" width="600"><br>
*working example.*

<img src="https://github.com/user-attachments/assets/e9c7b37e-4eba-4804-959b-a149a46d932b" width="600"><br>
*same function example.*

<img src="https://github.com/user-attachments/assets/23fdc163-1166-4294-82d5-8c5947dac6e3" width="600"><br>
*no solution example.*

<img src="https://github.com/user-attachments/assets/60d30481-39d6-4904-9250-5b399b9e5af7" width="600"><br>
*extra variable error.*

<img src="https://github.com/user-attachments/assets/905e7a8a-49f5-48ea-901b-ccff73917a97" width="600"><br>
*invalid syntax error.*

<img src="https://github.com/user-attachments/assets/7c558dd6-f2a9-4315-945f-4a3f78e74b4a" width="600"><br>
*unknown function error.*

