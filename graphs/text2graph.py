import re

from utils import STOPWORDS


class Text2Graph:
    def __init__(self, text):
        self.text = text
        self.nodes = None
        self.graph = {}

    def preprocess(self):
        self.text = self.text.lower()
        self.text = re.sub("[,?()\[\]<>;:\'\{\}]", "", self.text)
        sentence_list = self.text.split(".")

        cleaned_sentence_list = []
        for sentence in sentence_list:
            sentence = " ".join([word for word in sentence.split() if word
                                not in STOPWORDS])
            cleaned_sentence_list.append(sentence)

        # TODO: Stemming

        self.text = ". ".join(cleaned_sentence_list)

    @staticmethod
    def update_graph(graph, text, window):
        text = text.split()

        for i in range(0, len(text) - window + 1):
            for j in range(i + 1, i + window):
                text_ij = (text[i], text[j])
                text_ji = (text[j], text[i])

                if text_ij in graph.keys():
                    graph[text_ij] += 1
                else:
                    graph[text_ij] = 1

                if text_ji in graph.keys():
                    graph[text_ji] += 1
                else:
                    graph[text_ji] = 1

        for i in range(len(text) - window + 2, len(text)):
            for j in range(i + 1, len(text)):
                text_ij = (text[i], text[j])
                text_ji = (text[j], text[i])

                if text_ij in graph.keys():
                    graph[text_ij] += 1
                else:
                    graph[text_ij] = 1

                if text_ji in graph.keys():
                    graph[text_ji] += 1
                else:
                    graph[text_ji] = 1

        return graph

    def generate_graph(self, window=2):
        for sentence in self.text.split("."):
            self.graph = self.update_graph(self.graph, sentence, window)

        print(self.graph)




if __name__ == "__main__":
    doc = Text2Graph("Books are intelligence. Intelligence are books.")
    doc.preprocess()
    doc.generate_graph(window=3)
