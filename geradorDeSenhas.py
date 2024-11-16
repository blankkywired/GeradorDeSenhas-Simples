#Criar um algoritmo que crie senhas fortes com letras, numeros e simbolos baseado na quantidade de cada elemento que o usuario pedir

import random

letras = ['A' , 'B' , 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K' , 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1' , '2', '3' , '4', '5', '6', '7', '8', '9']
simbolos = [ '@', '!', '#', '$', '%', '&', '*', '(', ')', '-', '+', '=', '/', '?', '^', '~', '>', '<', ':', ';']

print('Bem-Vindo ao PyassWord Generator')

#Entradas
qtd_Letras = int(input('Quantas letras voce quer na sua senha?:\n'))
qtd_Numeros = int(input('Quantos numeros voce quer em sua senha?:\n'))
qtd_Simbolos = int(input('Quantos simbolos voce quer em sua senha:?\n'))


separador  = ''

l = random.sample(letras, qtd_Letras)
separador = ""
l = separador.join(l)


n = random.sample(numeros, qtd_Numeros)
separador = ""
n = separador.join(n)

s = random.sample(simbolos, qtd_Simbolos)
s = separador.join(s)

separador2 = ""
print(f'Sua senha é:' , separador.join(l)+separador.join(n)+separador.join(s))




