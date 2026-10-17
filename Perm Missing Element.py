def solution(A):
    N = len(A)

    # Sum of integers from 1 to N + 1.
    expected_sum = (N + 1) * (N + 2) // 2

    actual_sum = 0
    for number in A:
        actual_sum = actual_sum + number

    return expected_sum - actual_sum