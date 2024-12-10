def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neightbor of the rightmost field.
    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    Args
    values:
    1D array of values (list or numpy array)
    num_iteration:
    Integer to set the number of iterations
    """
    values = list(values)

    for _ in range(num_iterations):
        max_value = max(values)  # Biggest value
        max_index = values.index(max_value)  # Find its index
        distribution = max_value * share  # Calculate how much to distribute
        for i in [max_index - 1, max_index + 1]:  # Left and right neighbors
            neighbor_index = i % len(values)  # Keep index within the list
            values[neighbor_index] += distribution  # Add distribution to the neighbor
        values[max_index] -= 2 * distribution  # Subtract twice the share from the largest value
    return values