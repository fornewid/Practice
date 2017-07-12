def solve(S):
    diff = lambda idx: S[idx] - S[idx-1]
    pair = lambda idx: (S[idx-1], S[idx])

    min_diff = diff(min(range(1, len(S)), key=diff))
    return [pair(idx) for idx in range(1, len(S)) if diff(idx) is min_diff]
