from conta import Cliente, Conta

'''
conta=Conta('123-1','Clayton', 120.0, 1000.0)
conta.deposita(20.0)
conta.extrato()
conta.saca(40.0)
conta.extrato()

print("\n ********************************************** \n")


minha_conta = Conta('123-3','Carol', 130.0, 1100.0)
minha_conta.saldo = 1000
if (minha_conta.saca(2000)):
    print('Opa, consegui sacar')
else:
    print('Sorry, saldo insuficiente!!!')

conta = Conta('123-3','Carol', 130.0)
print(conta.limite)

cliente=Cliente('Clayton','Pereira','11111111-11')
minha_conta = Conta('123-4', cliente, 120.0)
print(minha_conta.titular.cpf)

'''

print("\n ********************************************** \n")
cliente1=Cliente('Clayton','Pereira','11111111-11')
cliente2=Cliente('Carol','Não_sei','22222222-22')

conta1 = Conta('123-1', cliente1, 120.0)
conta2 = Conta('123-2', cliente2, 130.0)

conta1.deposita(500.0)
conta1.saca(50.0)
conta1.transfere_para(conta2,150.0)
conta1.extrato()
conta1.deposita(230.0)
conta1.historico.imprime()

print("\n ********************************************** \n")
conta2.extrato()
conta2.historico.imprime()
conta2.transfere_para(conta1, 200.0)
conta2.historico.imprime()
conta2.saldo = 100
conta2.extrato()

#Cliente.__doc__


