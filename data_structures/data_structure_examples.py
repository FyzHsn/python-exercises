from collections import (
    defaultdict,
    namedtuple)


Sessions = namedtuple("Sessions", "id type created_at ended_at")


def letter_frequency(sentence):
    freq = defaultdict(int)
    for letter in sentence:
        freq[letter] += 1
    return freq


class WeirdSort:
    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, other):
        if self.sort_num:
            return self.number < other.number
        return self.string < other.string

    def __repr__(self):
        return "{}: {}".format(self.string, self.number)


class StrangeTuple:
    def __init__(self, twople):
        self.twople = twople

    def __add__(self, other):
        return self.twople[0] + other.twople[0], self.twople[1] + other.twople[1]


if __name__ == "__main__":

    ################
    # Named Tuples #
    ################
    sessions = []

    for i in range(0, 5):
        sessions.append(Sessions(i, 'individual', '2019-08-04 00:00:0{}'.format(i),
                                 '2019-08-05 00:00:0{}'.format(i)))

    print(sessions)

    ################
    # Dictionaries #
    ################
    stocks = {"GOOG": (613.30, 625.86, 610.50),
              "MSFT": (30.25, 30.70, 30.19)}

    print(stocks["GOOG"])
    print(stocks.get("GOOG"))
    print(stocks.get("RIM", "Data not found"))
    print(stocks.setdefault("LAND", (None, None, None)))
    print(stocks.get("LAND"))

    print(letter_frequency("mango lover"))

    a = WeirdSort('a', 4, True)
    b = WeirdSort('b', 3, True)
    c = WeirdSort('c', 2, True)
    d = WeirdSort('d', 1, True)

    l = [a, b, c, d]
    print(l)
    l.sort()
    print(l)

    a = StrangeTuple((1, 2))
    b = StrangeTuple((3, 4))
    print(a + b)





