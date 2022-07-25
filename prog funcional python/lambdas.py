# estrutura lamba argumento: expressão
# são funcoes anonimas

def multiplica(a,b):
    return a*b

#funcao lambda equivalente:
lambda a,b: a*b

#Refatorando script1 com lambda

def multiplicar_por(multiplicador):
    return lambda multiplicando: multiplicando * multiplicador

multiplicar_por_10 = multiplicar_por(10)

print(multiplicar_por_10(1))
print(multiplicar_por_10(2))
print(multiplicar_por_10(3))

#programação funcional tem como boa prática e regras não usar loops(for e while) e sim funcoes recursivas

print("usar o método map para percorrer elementos iteráveis (arrays, tuplas e dicionarios)")
print("O metodo map é puro e de ordem superior")

lista = [1, 2, 3, 4 ,5]
print(lista)

#sintaxe: map(função, iterável1, iterável2...)
nova_lista = map(lambda item:item*3, lista)

print(list(nova_lista))

nova_lista2 = filter(lambda item: item % 2 != 0, lista)
print(list(nova_lista2))