def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []

    # Try every possible starting position for the window
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            positions.append(i)

    return positions


found = naive_search("ABABDABACDABABCABAB", "ABABCABAB")
print(found)   # [10]