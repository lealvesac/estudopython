#Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dolares ela pode comprar.

dinheiroCarteira = float(input("Quantos Reais você tem para comprar $ Doláres? R$"))
cotacaoDolar = float(5.25)
conversaoRealDolar = dinheiroCarteira / cotacaoDolar

print(f"A cotação atual do Dólar é de R${cotacaoDolar}, e com o seu montande de R${dinheiroCarteira},"
      f" poderá comprar U${conversaoRealDolar:.2f}.")