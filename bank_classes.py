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
        raise NotImplementedError('Implement this class according to the type of bank')

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
    pass

if __name__ == '__main__':
    person1 = Person('João',25)
    print(person1.name)
    person1.name = 'Felipe'
    print(person1.name)

    

        
