def count_vectorizer(texts):
    texts = [text.lower() for text in texts]
    bow_keys = sorted(list(set(" ".join(texts).split())), key=lambda x: x)

    m = len(texts)
    n = len(bow_keys)

    bow = {word: [0] * m for word in bow_keys}
    for i, text in enumerate(texts):
        for word in text.split():
            bow[word][i] += 1

    mat = [bow[word] for word in bow_keys]
    mat_transpose = [[0 for i in range(0, n)] for j in range(0, m)]

    for i in range(0, m):
        for j in range(0, n):
            mat_transpose[i][j] = mat[j][i]

    return mat_transpose


if __name__ == "__main__":
    corpus = ["I like books", "Books are crooks", "crooks are toques"]
    print(count_vectorizer(corpus))