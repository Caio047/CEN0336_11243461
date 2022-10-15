#!/usr/bin/env python3

# Import libraries
import sys

# Assign the user arguments into variables
X = sys.argv[1]
Y = sys.argv[2]

# Check whether a and b are positive integer values
if bool(X.isdigit()) is False or int(X) < 0 or int(X) >= 500:
	print("ERRO: O primeiro argumento fornecido nao é um número positivo inteiro menor que 500. Tente novamente.")
	sys.exit()
elif bool(Y.isdigit()) is False or int(Y) < 0 or int(Y) >= 500:
	print("ERRO: O segundo argumento forncecido não é um número inteiro positivo menor que 500. Tente novamente.")
	sys.exit()

# Calculate the squared hypothenusa
else:
	Z = int(X)**2 + int(Y)**2

# Print the squared hypothenusa result
print("O quadrado da hipotenusa para o triangulo retângulo com lados a =", X, "e b =", Y, "é", Z)


