a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?', (a.isspace()))
print('É um numero?', (a.isnumeric()))
print('É alfabetico?', (a.isalpha()))
print('É Alfanumerico?', (a.isalnum()))
print('Esta em maiuscula?', (a.isupper()))
print('Está em minuscula?', (a.islower()))
print('Esta capitalizada?', (a.istitle()))
