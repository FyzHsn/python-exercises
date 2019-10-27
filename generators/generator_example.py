import os

CURRENT_DIR = os.path.dirname(__file__)


class MaxFinder:
    def __init__(self, sequence):
        self.sequence = sequence

    def __iter__(self):
        return self

    def __next__(self):
        v = self.sequence.readline()

        if not v:
            raise StopIteration

        return int(v)


if __name__ == "__main__":
    filepath = os.path.join(CURRENT_DIR, 'number_list.txt')
    with open(filepath) as f:
        numbers = (int(num) for num in f)

        max_val = next(numbers)

        for num in numbers:
            if num > max_val:
                max_val = num

    print(max_val)

    with open(filepath) as f:
        numbers = MaxFinder(f)

        max_val = next(numbers)

        for num in numbers:
            if num > max_val:
                max_val = num

    print(max_val)
