import numpy as np

def fair_sharer(values, num_iterations, share=0.1):
    """
    Runs num_iterations.

    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neighbor of the rightmost field.

    Args:
        values: 1D array of values (list or numpy array)
        num_iterations: Integer to set the number of iterations
        share: Fraction of the value to redistribute

    Returns:
        Updated list of values after redistribution
    """

    values = np.array(values)
    elements = len(values)
    
    for _ in range(num_iterations):
        max_index = np.argmax(values)
        max_value = values[max_index]

        redistribution = max_value * share

        values[max_index] -= 2 * redistribution
        values[(max_index - 1) % elements] += redistribution # Modulo to wrap around
        values[(max_index + 1) % elements] += redistribution

    return values.tolist()


print(fair_sharer([0, 1000, 800, 0], 1))
print(fair_sharer([0, 1000, 800, 0], 2))

