from text2graph import Text2Graph

from utils import preprocess


class Corpora2Graph:
    def __init__(self, corpora):
        self.corpora = corpora
        self.vocab = set({})
        self.corpora_graphs = []

        self.word_to_index = None
        self.index_to_word = None

    def transform(self):
        for document in self.corpora:
            doc = Text2Graph(document)
            doc.preprocess(stop_filter=False, pos_filter=False)
            doc.transform(window=4)
            self.corpora_graphs.append(doc)

    def word_index(self):
        docs = preprocess(". ".join(self.corpora),
                          stop_filter=False,
                          pos_filter=False)
        vocab = set({})
        for doc in docs:
            vocab = vocab.union(set(doc.split()))

        vocab = sorted(vocab)

        self.word_to_index = {w: i for (i, w) in enumerate(vocab)}
        self.index_to_word = {i: w for (i, w) in enumerate(vocab)}

    def centrality_matrix(self):
        m = len(self.word_to_index.keys())
        n = len(self.corpora)

        corpora_centrality_matrix = \
            [[0 for i in range(0, n)] for j in range(0, m)]



if __name__ == "__main__":
    doc_list = ["This document is about fruits. How mango is a fruit and how "
                "guava is a fruit. I personally like both fruits, but mangoes "
                "are tastier than guavas.",

                "This document is about animals. Animals such as cats and "
                "dogs. I like both animals equally. Cats and dogs are my "
                "fave animals.",

                ]

    doc_graph = Corpora2Graph(corpora=doc_list)
    doc_graph.transform()
    doc_graph.word_index()
    graph_1 = doc_graph.corpora_graphs[0]
    print(graph_1.graph)
    print(graph_1.degree_centrality())


