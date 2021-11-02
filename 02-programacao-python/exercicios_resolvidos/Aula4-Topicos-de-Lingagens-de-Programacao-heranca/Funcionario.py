#https://www.caelum.com.br/apostila-python-orientacao-a-objetos/heranca-e-classes-abstratas#repetindo-codigo

# Limpa Tela (CTRL+L) ou (CLEAR) ou 
import os
os.system('cls' if os.name == 'nt' else 'clear')

class Funcionario:

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def	get_bonificacao(self):
        return self._salario *	0.10    

"""
Além de um funcionário comum, há também outros cargos, como os gerentes. 
Os gerentes guardam a mesma informação que um funcionário comum, mas possuem outras informações, 
além de ter funcionalidades um pouco diferentes. Um gerente no nosso banco possui também uma senha 
numérica que permite o acesso ao sistema interno do banco, além do número de funcionários que ele 
gerencia:
"""

class Gerente(Funcionario):

    def __init__(self, nome, cpf, salario, senha, qtd_funcionarios):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios

    def autentica(self, senha):
        if self._senha == senha:
            print("acesso permitido")
            return True
        else:
            print("acesso negado")              
            return False

    def	get_bonificacao(self):
        return self._salario *	0.15


class Diretor(Funcionario):

    def __init__(self, nome, cpf, salario, senha, controlar_atividades):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._controlar_atividades = controlar_atividades

    def autentica(self, senha):
        if self._senha == senha:
            print("acesso permitido")
            return True
        else:
            print("acesso negado")              
            return False

    def	get_bonificacao(self):
        return self._salario *	0.16

class Secretario(Funcionario):

    def __init__(self, nome, cpf, salario, senha, marcar_viagens):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._marcar_viagens = marcar_viagens

    def autentica(self, senha):
        if self._senha == senha:
            print("acesso permitido")
            return True
        else:
            print("acesso negado")              
            return False

    def	get_bonificacao(self):
        return self._salario *	0.16


class Presidente(Funcionario):

    def __init__(self, nome, cpf, salario, senha, almocar_com_executivos):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._almocar_com_executivos = almocar_com_executivos


    def autentica(self, senha):
        if self._senha == senha:
            print("acesso permitido")
            return True
        else:
            print("acesso negado")              
            return False

    def	get_bonificacao(self):
        return self._salario *	0.99

#adicionando um funcionario
funcionario	=	Funcionario('Carlos', '111111111-11',	2000.0)
print("#"*80)
print(f"Nome do funcionario do ano é: {funcionario._nome} ")

#Adicionando uma bonificação para o gerente
gerente	=	Gerente('Luiz',	'111111111-22',	15000.0, '1234', 0)
print("#"*80)
print(f"Pelo seu trabalho {gerente._nome} toma aqui um grujeta de R$ {gerente.get_bonificacao()}")

#Adicionando uma bonificação para o diretor
diretor	=	Diretor('Luiz Carlos',	'111111111-22',	15000.0, '1234', 'Casa das Máquinas')
print("#"*80)
print(f"Pelo seu trabalho {diretor._nome} toma aqui um grujeta de R$ {diretor.get_bonificacao()}")

#Adicionando uma bonificação para o secretaria
secretario	=	Secretario('Atena',	'111111111-22',	125000.0, '1234', 'Monte Olimpo')
print("#"*80)
print(f"Pelo seu trabalho {secretario._nome} toma aqui um grujeta de R$ {secretario.get_bonificacao()}")

#Adicionando uma bonificação para o presidente
presidente	=	Secretario('LCBJ',	'111111111-22',	200000.0, '1234', 'Executivos da Agroaki')
print("#"*80)
print(f"Pelo seu trabalho {presidente._nome} toma aqui um grujeta de R$ {presidente.get_bonificacao()}")


"""
Utilize	o método vars() para acessar os	atributos de  Gerente e	ver	que	a classe 
herda todos os atributos de Funcionario	:
"""
print("#"*80)
print(f'vars(funcionario), {vars(funcionario)}')

print("#"*80)
print(f'vars(gerente), {vars(gerente)}')
print("#"*80)

print(f'vars(diretor), {vars(diretor)}')
print("#"*80)

print(f'vars(diretor), {vars(secretario)}')
print("#"*80)

print(f'vars(presidente), {vars(presidente)}')
print("#"*80)

