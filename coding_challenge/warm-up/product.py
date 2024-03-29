import json
import pennylane as qml
import pennylane.numpy as np

dev = qml.device("default.mixed", wires=2)
@qml.qnode(dev)
def is_product(state, subsystem, wires):
    """Determines if a pure quantum state can be written as a product state between 
    a subsystem of wires and their compliment.

    Args:
        state (numpy.array): The quantum state of interest.
        subsystem (list(int)): The subsystem used to determine if the state is a product state.
        wires (list(int)): The wire/qubit labels for the state. Use these for creating a QNode if you wish!

    Returns:
        (str): "yes" if the state is a product state or "no" if it isn't.
    """


    # Put your solution here #
    qml.QubitStateVector(state, wires=wires)
    print(qml.density_matrix([0]))
    return qml.density_matrix([0])
    # if qml.state() == state:
    #     return 'yes'
    # else:
    #     return 'no'


# These functions are responsible for testing the solution.
def run(test_case_input: str) -> str:
    ins = json.loads(test_case_input)
    state, subsystem, wires = ins
    state = np.array(state)
    output = is_product(state, subsystem, wires)
    return output

def check(solution_output: str, expected_output: str) -> None:
    assert solution_output == expected_output


test_cases = [['[[0.707107, 0, 0, 0.707107], [0], [0, 1]]', 'no'], ['[[1, 0, 0, 0], [0], [0, 1]]', 'yes']]

for i, (input_, expected_output) in enumerate(test_cases):
    print(f"Running test case {i} with input '{input_}'...")

    try:
        output = run(input_)

    except Exception as exc:
        print(f"Runtime Error. {exc}")

    else:
        if message := check(output, expected_output):
            print(f"Wrong Answer. Have: '{output}'. Want: '{expected_output}'.")

        else:
            print("Correct!")