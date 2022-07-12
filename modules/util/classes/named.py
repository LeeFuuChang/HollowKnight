class NamedObject:
    def __init__(self, **kwargs):
        self.names = []
        for name, value in kwargs.items():
            self.names.append(name)
            self.__setattr__(
                name, value
            )

    def __getitem__(self, __arg):
        return self.__getattribute__(__arg)