from conta import Conta
from clientes import Client

cliente1 = Client(123, "Joao", "Rua 1")
cliente2 = Client(123, "Maria", "Rua 2")
cliente3 = Client(456, "Gabriel", "Rua W")

conta1 = Conta([cliente1, cliente2], 1, 2000)
conta2 = Conta(cliente3, 2, 200)


conta1.deposito(1000)
conta1.saque(1500)
conta1.extrato.extrato(conta1.numero)

conta1.transfereValor(conta2, 200)
conta2.extrato.extrato(conta2.numero)