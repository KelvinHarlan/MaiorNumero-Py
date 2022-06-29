#Faça um Programa que leia três números e mostre o maior deles.

numero_1 = float(input('Digite o 1° número\n'))
numero_2 = float(input('Digite o 2° número\n'))
numero_3 = float(input('Digite o 3° número\n'))

numeros = [numero_1, numero_2, numero_3]
maior_numero = max(numeros)
print(f'O maior número escolhido foi: {maior_numero}')