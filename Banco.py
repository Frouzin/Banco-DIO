import textwrap
from abc import ABC, abstractclassmethod,abstractproperty
from datetime import datetime
class Cliente:
    def __init__(self,endereco):
        self.endereco = endereco
        self.contas = [] 
        
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)
    
class PessoaFisica(Cliente):
    


class Conta:
    
    

class ContaCorrente(Conta):
    
    
    

class Historico:
    
    

class Transacao(ABC):
    
    


class Saque(Transacao):
    
    

class Deposito(Transacao):
main()            