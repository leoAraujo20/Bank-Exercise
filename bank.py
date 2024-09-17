import bank_classes

client1 = bank_classes.Client('Joao', 25 )
account1 = client1.criar_conta(bank_classes.CheckingAccount('001', '12345-6', 5000))
client1.conta.withdraw_money(100)
print(client1.conta.balance)