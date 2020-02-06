def permutations(n, r):
    elements = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z']
    if n < len(elements):
        elements = elements[:n]
    else:
        ValueError("Choose n less than 27")

    sample_space = set({})
