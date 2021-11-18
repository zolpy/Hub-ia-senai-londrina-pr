class Pessoa():
    "Construindo a classe para utilizar metodo main"
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def set_apresenta_nome(self):
        return self.nome
    
    def set_apresenta_idade(self):
        return self.idade

class Alunos(Pessoa):
    "Herança da classe pessoa"
    def __init__(self, nome, idade, matricula) -> None:
        super().__init__(nome, idade)
        self.matricula = matricula

    def set_apresenta_matricula(self):
        return self.matricula


if __name__ == '__main__':
    p1 = Pessoa("Clayton", 47)

    print("A pessoa {} possui {} anos de idade".format(p1.set_apresenta_nome(), p1.set_apresenta_idade()))

    aluno = Alunos("João", 33, 300)
    print("O aluno {} possui {} anos de idade com o registro {}".format(aluno.set_apresenta_nome()
    , aluno.set_apresenta_idade(), aluno.set_apresenta_matricula()))