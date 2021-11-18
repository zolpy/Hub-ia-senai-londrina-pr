class Mamifero:
    'polimorfismo em Python é a capacidade que uma subclasse tem de ter métodos com co mesmo nome de sua superclasse'
    def __init__(self) -> None:
        pass

class Cachorro(Mamifero):
    def __init__(self) -> None:
        super().__init__()

    def seu_son(self):
        print('Au Au')


class Gato(Mamifero):
    def __init__(self) -> None:
        super().__init__()

    def seu_son(self):
        print('Miau Miau')

class Rato(Mamifero):
    def __init__(self) -> None:
        super().__init__()

    def seu_son(self):
        print('Qui qui')


if __name__=='__main__':
    dog = Cachorro()
    cat = Gato()
    mouse = Rato()

    mamiferos = [dog, cat, mouse]

    for mamifero in mamiferos:
        mamifero.seu_son()
