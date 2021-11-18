class Eletronico:
    "Super classe (classe Pai)"
    def __init__(self) -> None:
        "Construto é chamado quado instanciamos um objeto"
        self.ligado = True

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def esta_ligado(self):
        return self.ligado


class TV(Eletronico):
    "Classe TV é uma classe filha de Eletronico"
    def __init__(self) -> None:
        Eletronico.__init__(self)
        self.volume = 0

    def aumenta_volume(self):
        self.volume +=1

    def diminui_volume(self):
        if self.volume > 0:
            self.volume -=1

    def obter_volume(self):
        return self.volume

class iPhone(Eletronico):
    def __init__(self) -> None:
        super().__init__()
        self.tocando_musica = False

    def tocar_musica(self):
        self.tocando_musica = True

    def parar_musica(self):
        self.tocando_musica = False

tv = TV()
print(tv.esta_ligado())

tv.ligar()
print(tv.esta_ligado())

tv.aumenta_volume()
print(tv.obter_volume())

fone = iPhone()
print(fone.esta_ligado())

