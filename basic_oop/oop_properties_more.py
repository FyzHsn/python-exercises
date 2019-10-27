import logging

from urllib.request import urlopen


logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s')


class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print("Retrieving new page ...")
            self._content = urlopen(self.url).read()
        return self._content


class AverageList(list):
    @property
    def average(self):
        try:
            return sum(self)/len(self)
        except TypeError:
            logging.error("Make sure list comprised of float and int types only")
            raise


if __name__ == "__main__":
    w = WebPage("amazon.com")
    w._content = "a"
    print(w.content)

    a = AverageList([1, 2, 3.4])
    print(a.average)

    a.append("a")
    print(a.average)