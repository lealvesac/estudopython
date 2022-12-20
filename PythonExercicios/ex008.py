#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

metros = float(input("Informe uma quantidade em metros para converter: "))
centimetros = metros * 100
milimetros = metros * 1000

print(f"A conversão de {metros}m METROS, ficará {centimetros}cm em CENTRIMETROS, e {milimetros}mm em MILIMETROS.")