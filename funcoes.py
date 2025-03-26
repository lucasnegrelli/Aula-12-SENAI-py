import random

# 1 - Função para gerar um número aleatório entre 5 e 10
def gerar_aleatorio_5_10():
    """Função que gera um número aleatório entre 5 e 10 (inclusive)"""
    num_aleat = random.randint(5, 10)
    print('\n1 - Crie um número aleatório de 5,10')
    print('***', num_aleat, '***')
    return num_aleat

# 2 - Função para gerar 3 números aleatórios de 8 bits
def gerar_tres_aleatorios():
    """Função que gera três números aleatórios de 8 bits"""
    print('\n2 - Crie 3 números aleatórios')
    # Gerar três números aleatórios de 8 bits
    numero1 = random.getrandbits(8)
    numero2 = random.getrandbits(8)
    numero3 = random.getrandbits(8)
    
    # Imprimir os três números
    print(numero1, numero2, numero3)
    return numero1, numero2, numero3

# 3 - Função para gerar um número aleatório entre 10 e 30
def gerar_aleatorio_range():
    """Função que gera um número aleatório entre 10 e 30 usando randrange"""
    from random import randrange
    print('\n3 - Crie um número aleatório entre 10 a 30. Utilize o range()')
    numero = randrange(10, 30)  # Gera um número aleatório na faixa de inteiros de 10 a 29
    print('***', numero, '***')
    return numero

# 4 - Função para contagem regressiva
def contagem_regressiva():
    """Função que exibe uma contagem regressiva de 10 a 1 e depois imprime 'Fogo!'"""
    print('\n4 - Contagem regressiva simples. \nEscreva um programa que exiba uma contagem regressiva de 10 a 1, e depois imprima "Fogo!".(loop for)')
    # O loop 'for' irá contar de 10 até 1 (inclusive)
    for i in range(10, 0, -1):
        # A cada iteração, o valor de 'i' será impresso (de 10 até 1)
        print(i)
    
    # Após a contagem regressiva, imprime "Fogo!".
    print("Fogo!")

# 5 - Função para calcular a soma de números pares
def soma_pares():
    """Função que calcula a soma de todos os números pares de 2 até o número inserido pelo usuário"""
    print('\n5 - Soma de números pares \nPeça ao usuário que insira um número inteiro positivo e, em seguida, \ncalcule a soma de todos os números pares de 2 até o número inserido. (use módulo, if, for)')
    
    # Solicitar ao usuário um número inteiro positivo
    numero = int(input("Digite um número inteiro positivo: "))
    
    # Inicializar a variável que vai armazenar a soma
    soma = 0
    
    # Percorrer os números de 2 até o número inserido (inclusive)
    for i in range(2, numero + 1):
        # Verificar se o número é par usando o operador módulo (%)
        if i % 2 == 0:  # Se o resto da divisão por 2 for 0, o número é par
            soma += i  # Adicionar o número à soma
    
    # Imprimir o resultado final
    print("A soma dos números pares de 2 até", numero, "é:", soma)
    return soma

# 6 - Função para mostrar a tabuada de multiplicação
def tabuada_multiplicacao():
    """Função que mostra a tabuada de multiplicação de um número de 1 a 10"""
    print('\n6 - Tabuada de multiplicação\nPeça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10. (while ou for )')
    
    # Solicitar ao usuário um número inteiro
    numero = int(input("Digite um número inteiro para ver sua tabuada: "))
    
    # Exibir a tabuada de multiplicação de 1 a 10
    for i in range(1, 11):
        resultado = numero * i  # Multiplicar o número pelo valor de i
        print(f"{numero} x {i} = {resultado}")  # Exibir o resultado formatado
    
    return numero

# 7 - Função para exibir números ímpares em ordem decrescente
def impares_reversos():
    """Função que exibe números ímpares em ordem decrescente de 99 a 1"""
    print('\n7 - Números ímpares reversos\nExiba uma contagem regressiva de números ímpares de 99 a 1. (for)')
    
    # Exibir números ímpares em ordem decrescente de 99 até 1
    # Começamos em 99 e decrementamos de 2 em 2 para pegar apenas os ímpares
    for i in range(99, 0, -2):
        print(i)