import re

import nltk
from nltk.stem import PorterStemmer

from utils import STOPWORDS


class Text2Graph:
    def __init__(self, text):
        self.text = text
        self.edges = {}
        self.graph = {}

    def preprocess(self):
        self.text = self.text.lower()
        self.text = re.sub("[,()\n\[\]<>;:\'\{\}]", "", self.text)
        sentence_list = re.split("[?.]", self.text)

        stemmer = PorterStemmer()
        cleaned_sentence_list = []
        for sentence in sentence_list:
            clean_text = ""
            text_pos = nltk.pos_tag(sentence.split())
            for (word, tag) in text_pos:
                if ("NN" in tag) or ("ADJ" in tag) or ("JJ" in tag):
                    clean_text += word + " "
            sentence = " ".join([stemmer.stem(word) for word in
                                 clean_text.split() if word not in STOPWORDS])
            cleaned_sentence_list.append(sentence)

        self.text = ". ".join(cleaned_sentence_list)

    @staticmethod
    def update_graph(graph, text, window):
        text += " PADPAD" * (window - 2)
        text = text.split()

        def update_edge_weights(graph, text, i, j):
            text_ij = (text[i], text[j])
            text_ji = (text[j], text[i])

            if text_ij in graph.keys() and "PADPAD" not in text_ij:
                graph[text_ij] += 1
            elif text_ij not in graph.keys() and "PADPAD" not in text_ij:
                graph[text_ij] = 1

            if text_ji in graph.keys() and "PADPAD" not in text_ji:
                graph[text_ji] += 1
            elif text_ji not in graph.keys() and "PADPAD" not in text_ji:
                graph[text_ji] = 1

            return graph

        for i in range(0, len(text) - window + 1):
            for j in range(i + 1, i + window):
                graph = update_edge_weights(graph, text, i, j)

        return graph

    def generate_graph(self, window=2):
        for sentence in re.split("[?.]", self.text):
            self.graph = self.update_graph(self.graph, sentence, window)

        print(self.graph)

    def degree_centrality(self):
        node_score = {}

        for (node_1, node_2), weight_12 in self.graph.items():
            if node_1 not in node_score.keys():
                node_score[node_1] = weight_12
            else:
                node_score[node_1] += weight_12

        node_score = sorted([(node, score) for (node, score) in
                             node_score.items()], key=lambda x: x[1],
                            reverse=True)

        return node_score

    def normalized_degree_centrality(self):
        node_score = self.degree_centrality()
        n = len(node_score) - 1
        return [(node, score / n) for (node, score) in node_score]


if __name__ == "__main__":
    from gslabs.db.db_requester import DBRequester

    db_requester = DBRequester()
    results, col_names = db_requester.get_query_results("""SELECT message 
    FROM messages WHERE is_question=1 and message not like like "%{file:%" 
    and message not like "%ttps%" """)

    document = ". ".join(results)

    doc = Text2Graph(document)
    doc.preprocess()
    doc.generate_graph(window=2)
    a = doc.degree_centrality()
    b = doc.normalized_degree_centrality()

    for (node, score) in a:
        print(node, score)

    for (node, score) in b:
        print(node, score)