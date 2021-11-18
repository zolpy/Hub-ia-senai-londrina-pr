def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

# Função depositar
def deposita(conta, valor):
    conta['saldo'] += valor

# Função sacar
def saca(conta, valor):
    conta['saldo'] -= valor

# Função extrato
def extrato(conta):
    #print("numero: {} \nsaldo: {} \n".format(conta['numero'], conta['saldo']))
    print('O número da conta %s possui saldo de %s' %(conta['numero'], conta['saldo']))


conta1 = cria_conta('123-1', 'Clayton', 500.0, 1000.0)
deposita(conta1, 50.00)
extrato(conta1)

conta2 = cria_conta('123-2', 'Carol', 800.0, 1200.0)
deposita(conta2, 150.00)
extrato(conta2)

conta1['saldo']=11110000000
extrato(conta1)


