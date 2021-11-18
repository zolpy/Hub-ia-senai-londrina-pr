import datetime


class Historico:
    "Essa classe representa informações sobre histórico de transações"
    def __init__(self) -> None:
        self.data_abertura = datetime.datetime.today() 
        self.transacoes = []

    def imprime(self):
        print("Data da abertura: {}".format(self.data_abertura))
        print("Transações: ")
        for i in self.transacoes:
            print("-", i)



class Cliente:
    "Essa classe representa informações sobre os dados dos clientes"
    def __init__(self,nome, sobrenome, cpf) -> None:
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    @property
    def get_nome(self):
        print('Imprimindo @property nome()')
        return self._nome.title()

    @nome.setter
    def set_nome(self, nome):
        print('Imprimindo @setter nome()')
        self._nome = nome

class Conta:
    "Essa classe representa informações sobre as contas dos clientes"
    def __init__(self, numero, cliente, saldo, limite=1000.0) -> None:
        print("Construindo meu objeto ...{}.format(self)")
        self._numero = numero
        self.__cliente = cliente
        self.__saldo = saldo
        self.__limite = limite
        self.historico = Historico()

    # Função depositar
    def deposita(self,valor):
        self.__saldo += valor


    # Função sacar
    def saca(self, valor):
        if (self.__saldo < valor):
            return False
        else:
            self.__saldo -= valor
            return True

    # Função extrato
    def extrato(self):
        print("numero: {} \nsaldo: {} \n".format(self._numero, self.__saldo))

    def transfere_para(self, destino, valor):
        """ Efetua uma transferência entre contas

            Args:
                destino (float): Conta destino.
                valor (float): Valor a ser transferido

            Returns:
                bool: Um Booleano informando se a transação aconteceu ou não 
        """
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append("Transferência de {} para conta {}".format(valor, destino._numero))
            return True

    def get_saldo(self):
        return self.saldo

    

   