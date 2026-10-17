def solution(X, Y, D):
    # Calculate the distance to the target.
    distance = Y - X

    # Count the full jumps using integer division.
    jumps = distance // D
    if distance % D != 0:
        jumps = jumps + 1

    return jumps