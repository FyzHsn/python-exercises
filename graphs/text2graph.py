import re

import nltk
from nltk.stem import PorterStemmer

from utils import STOPWORDS


class Text2Graph:
    def __init__(self, text):
        self.text = text
        self.edges = {}
        self.graph = {}

    def preprocess(self, remove_stopwords=True):
        """Text preprocessor

        Clean text by removing punctuations, stopwords, non-noun and
        adjectives in addition to stemming.

        :return: clean text
        :rtype: str
        """

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

            if remove_stopwords:
                sentence = " ".join([stemmer.stem(word) for word in
                                     clean_text.split() if word not in
                                     STOPWORDS])

            cleaned_sentence_list.append(sentence)

        self.text = ". ".join(cleaned_sentence_list)

    @staticmethod
    def update_graph(graph, text, window):
        text += " PADPAD" * (window - 2)
        text = text.split()

        def update_edge_weights(graph, text, i, j):
            text_ij = (text[i], text[j])

            if text_ij in graph.keys() and "PADPAD" not in text_ij:
                graph[text_ij] += 1
            elif text_ij not in graph.keys() and "PADPAD" not in text_ij:
                graph[text_ij] = 1

            return graph

        for i in range(0, len(text) - window + 1):
            for j in range(i + 1, i + window):
                graph = update_edge_weights(graph, text, i, j)
                graph = update_edge_weights(graph, text, j, i)

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


class Corpora2Graph:
    def __init__(self):
        pass

    def preprocess(self):
        pass




if __name__ == "__main__":
    document = """Kinematics is the branch of classical mechanics that 
    describes the motion of 
points, objects and systems of groups of objects, without reference to the 
causes of motion (i.e., forces ). The study of kinematics is often referred 
to as the geometry of motion. Objects are in motion all around us. Everything 
from a tennis match to a space-probe flyby of the planet Neptune involves 
motion. When you are resting, your heart moves blood through your veins. 
Even in inanimate objects there is continuous motion in the vibrations of 
atoms and molecules. Interesting questions about motion can arise: how long 
will it take for a space probe to travel to Mars? Where will a football land 
if thrown at a certain angle? An understanding of motion, however, is also key 
to understanding other concepts in physics. An understanding of acceleration, 
for example, is crucial to the study of force. To describe motion, 
kinematics studies the trajectories of points, lines and other geometric 
objects, as well as their differential properties (such as velocity and 
acceleration). Kinematics is used in astrophysics to describe the motion of  
celestial bodies and systems; and in mechanical engineering, robotics and 
biomechanics to describe the motion of systems composed of joined parts 
(such as an engine, a robotic arm, or the skeleton of the human body). A 
formal study of physics begins with kinematics. The word kinematics comes 
from a Greek word kinesis meaning motion, and is related to other English 
words such as cinema (movies) and kinesiology (the study of human motion). 
Kinematic analysis is the process of measuring the kinematic quantities 
used to describe motion. The study of kinematics can be abstracted into 
purely mathematical expressions, which can be used to calculate various 
aspects of motion such as velocity, acceleration, displacement, time, 
and trajectory."""

    doc = Text2Graph(document)
    doc.preprocess(remove_stopwords=False)
    doc.generate_graph(window=2)
    a = doc.degree_centrality()
    b = doc.normalized_degree_centrality()

    for (node, score) in a:
        print(node, score)

    for (node, score) in b:
        print(node, score)