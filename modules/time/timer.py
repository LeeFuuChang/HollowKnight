from .. import const

class Timer:
    __instances__ = []

    @classmethod
    def addAll(cls):
        for timer in cls.__instances__:
            timer.add()

    def __init__(self, t):
        self.__instances__.append(self)
        self.i = 0
        self.setTime(t)

    def setTime(self, t):
        self.t = t

    def setTrue(self):
        self.i = self.t*const.game.FPS

    def delete(self):
        self.__instances__.remove(self)

    def add(self):
        self.i += 1

    def reset(self):
        self.i = 0

    def check(self, autoReset=True):
        if self.i/const.game.FPS >= self.t:
            if autoReset: self.reset()
            return True
        return False