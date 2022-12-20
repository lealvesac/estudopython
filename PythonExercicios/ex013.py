#Faça um algoritimo que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento.

salarioFuncionario = float(input("Informe o salario do funcionario: R$"))
aumento = 15
novoSalario = salarioFuncionario + (salarioFuncionario * aumento / 100)

print(f"O novo salario do funcionario é de R${novoSalario:.2f}")