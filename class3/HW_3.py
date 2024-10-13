import abc

class Sport(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

class Basketball(Sport):
    def play(self):
        print("Playing basketball takes 2 hours.")

class Baseball(Sport):
    def play(self):
        print("Playing baseball takes 4 hours.")

basketball = Basketball()
baseball = Baseball()
basketball.play()
baseball.play()