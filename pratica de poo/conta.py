import datetime
from extrato import Extrato

class Conta:
    def __init__(self, clientes, __numero, __saldo):
        self.clientes = clientes
        self.numero = __numero
        self.saldo = __saldo
        self.sata = datetime.date.today()
        self.extrato = Extrato()
    

    def deposito(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPOSITO", valor, "Data",datetime.date.today ()])
    
    def saque(self, valor):
        if (self.saldo < valor):
            print("Atencao! Operacao nao permitida!")
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.date.today()])
            return True

    def transfereValor(self,contaDestino,valor):
        if self.saldo < valor:
            return ("Atencao! Saldo insuficiente")
        else:
            contaDestino.deposito(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.date.today()])
            return "Transferencia Realizada"
    
    
    def gerarsaldo(self):
        print(f"numero: {self.unmero}\n saldo:{self.saldo}")
