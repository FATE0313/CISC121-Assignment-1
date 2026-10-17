def solution(A, K):
    if len(A) == 0:
        return A

    # Move the last element to the front K times.
    for i in range(K):
        last = A.pop()
        A.insert(0, last)

    return A