class BaseClass:
    a = 0

    def random_method(self):
        print(self.a)
        self.a = 7

    def random_method_two(self):
        print(self.a)
        print(self.b)


class Subclass(BaseClass):
    b = 8

    def random_method(self):
        print(self.b)
        print(self.a)


class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid File Format")

        self.filename = filename


class MP3File(AudioFile):
    ext = 'mp3'
    def play(self):
        print("playing mp3 file format")


class WavFile(AudioFile):
    ext = 'wav'
    def play(self):
        print('playing wav file format')


if __name__ == "__main__":
    test = Subclass()
    test.random_method_two()

    mp3 = MP3File('f.mp3')
    mp3.play()

    wav = WavFile('g.wav')
    wav.play()

