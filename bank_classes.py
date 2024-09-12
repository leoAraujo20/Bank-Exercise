from abc import ABC, abstractmethod

class Pessoa():
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        self._name = name

if __name__ == '__main__':
    person1 = Pessoa('João',25)
    print(person1.name)
    person1.name = 'Felipe'
    print(person1.name)
    

        
