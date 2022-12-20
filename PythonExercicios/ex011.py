#Faça um programa que leia a largura e a altura de uma parede
#em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la,
#sabendo que cada litro de tinta, pinta uma area de 2m².

alturaParede = float(input("Informe ALTURA da parede: "))
larguraParede = float(input("Informe a LARGURA da parede: "))

areaDePintura = alturaParede * larguraParede
qtdTintaUsar = areaDePintura / 2

print(f"A sua parede de {alturaParede}ALT e {larguraParede}LARG, da um total de {areaDePintura}m², e você irá"
      f" usar {qtdTintaUsar}LTs de tinta!")