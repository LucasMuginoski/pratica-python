def multiplica_por(multiplificador):

    def multi(multiplicando):
        return multiplicando * multiplificador
    return multi

multificando_por_10 = multiplica_por(10)
print(multificando_por_10(1))

print(multificando_por_10(2))

print(multificando_por_10(3))

multificando_por_5 = multiplica_por(5)

print(multificando_por_5(1))

print(multificando_por_5(25))
