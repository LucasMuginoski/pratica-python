"""
    Programa que faz o calculo do imc de uma pessoa
"""
peso = eval(input("Digite seu peso: "))
altura = eval(input("Agora digite sua altura: "))

imc = peso/(altura**2)

print("Seu imc eh: ", imc)