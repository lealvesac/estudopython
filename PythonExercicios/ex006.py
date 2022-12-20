#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input("Informe um numero: "))
dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero**(1/2)

print(f'O numero informado foi {numero}.')
print(f'O Seu Dobro é {dobro}.')
print(f'O Seu Triplo é {triplo}.')
print(f'E Sua Raiz Quadrada é {raizQuadrada:.2f}.')