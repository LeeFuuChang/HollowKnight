class NamedObject:
    def __init__(self, **kwargs):
        self.names = []
        for name, value in kwargs.items():
            self.names.append(name)
            self.__setattr__(
                name, value
            )