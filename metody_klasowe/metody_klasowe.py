class Obywatel:
    def __init__(self, name: str):
        self.name = name

    @classmethod
    def ustaw_janusza(cls, name: str):
        cls.janusz_name = name

    def __str__(self):
        return f'Solution({self.name =})'


if __name__ == '__main__':
    obywatel1 = Obywatel(name='kaku')
    obywatel2 = Obywatel(name='paku')
    obywatel1.ustaw_janusza(name='wiekszy januszito')
    obywatel2.ustaw_janusza(name='januszito')
    print(obywatel1.janusz_name)
    print(obywatel2.janusz_name)
