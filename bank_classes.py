from abc import ABC, abstractmethod

class Account(ABC):
    
    def __init__ (self, agency, account_number, balance):
        self.agency = agency
        self.account_number = account_number
        self.balance = balance
    
    def deposit_money(self,value):
        self.balance += value

    @abstractmethod
    def withdraw_money():
        raise NotImplementedError('Implement this class according to the type of account!')

class CheckingAccount(Account):

    def withdraw_money(self, value):
        self.balance -= value
        

class Person():
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        self._name = name
    
class Client(Person):
    def criar_conta(self, conta:Account):
        self.conta = conta

if __name__ == '__main__':
    client1 = Client('Joao', 25 )
    account1 = client1.criar_conta(CheckingAccount('001', '12345-6', 5000))
    client1.conta.withdraw_money(100)
    print(client1.conta.balance)
    

  

        
