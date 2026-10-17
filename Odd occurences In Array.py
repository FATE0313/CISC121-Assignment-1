def solution(A):
    ordered = sorted(A)
    i = 0

    # Check the sorted numbers in pairs.
    while i < len(ordered) - 1:
        if ordered[i] != ordered[i + 1]:
            return ordered[i]
        i = i + 2

    return ordered[-1]