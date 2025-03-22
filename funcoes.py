import random

# 1
num_aleat = random.randint(5, 10)
print('\n1 - Crie um número aleatório de 5,10')
print('***',num_aleat,'***')


# 2
print('\n2 - Crie 3 números aleatórios')
# Gerar três números aleatórios de 8 bits
numero1 = random.getrandbits(8)
numero2 = random.getrandbits(8)
numero3 = random.getrandbits(8)

# Imprimir os três números
print(numero1, numero2, numero3)


# 3
from random import randrange
print('\n3 - Crie um número aleatório entre 10 a 30. Utilize o range()')
print('***',randrange(10, 30),'***') #faixa de inteiro


# 4
print('\n4 - Contagem regressiva simples. \nEscreva um programa que exiba uma contagem regressiva de 10 a 1, e depois imprima "Fogo!".(loop for)')
# O loop 'for' irá contar de 10 até 1 (inclusive)
for i in range(10, 0, -1):
    # A cada iteração, o valor de 'i' será impresso (de 10 até 1)
    print(i)

# Após a contagem regressiva, imprime "Fogo!".
print("Fogo!")


# 5
print('\n**5 - Soma de números pares** \nPeça ao usuário que insira um número inteiro positivo e, em seguida, \ncalcule a soma de todos os números pares de 2 até o número inserido. (use módulo, if, for)')

# Solicitar ao usuário um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Inicializar a variável que vai armazenar a soma
soma = 0

# Percorrer os números de 2 até o número inserido (inclusive)
for i in range(2, numero + 1):
    # Verificar se o número é par
    if i % 2 == 0:
        soma += i  # Adicionar o número à soma

# Imprimir o resultado final
print("A soma dos números pares de 2 até", numero, "é:", soma)


# 6
print('\n**6 - Tabuada de multiplicação**\nPeça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10. (while ou for )')

# Solicitar ao usuário um número inteiro
numero = int(input("Digite um número inteiro para ver sua tabuada: "))

# Exibir a tabuada de multiplicação de 1 a 10
for i in range(1, 11):
    resultado = numero * i  # Multiplicar o número pelo valor de i
    print(f"{numero} x {i} = {resultado}")  # Exibir o resultado


# 7
print('\n**7 - Números ímpares reversos**\nExiba uma contagem regressiva de números ímpares de 99 a 1. (for)')

# Exibir números ímpares em ordem decrescente de 99 até 1
for i in range(99, 0, -2):
    print(i)
