#Faça um programa que leia algo pelo teclado
#e mostre na tela o seu tipo primitivo
#e todas as informaçoes possiveis sobre ele.

entrada = input("Digite algo: \n")
print("Tipo primitivo: {}.".format(type(entrada)))
print("È alfanumerico? {}.".format(entrada.isalpha))
print("È um decimal? {}.".format(entrada.isdecimal()))
print("Esta em caixa baixa? {}.".format(entrada.islower()))
print("È apenas espaço em branco? {}.".format(entrada.isspace()))
print("Esta em caixa alta? {}.".format(entrada.isupper()))

