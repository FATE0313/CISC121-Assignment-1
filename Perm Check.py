def solution(A):
    ordered = sorted(A)
    expected = 1
    for number in ordered:
        if number != expected:
            return 0
        expected = expected + 1

    return 1