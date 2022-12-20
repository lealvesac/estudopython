#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

precoProduto = float(input("Informe o valor do produto: R$"))
desconto = 5
produtoComDesconto = precoProduto - (precoProduto * desconto / 100)

print(f"O produto com desconto fica R${produtoComDesconto:.2f}")