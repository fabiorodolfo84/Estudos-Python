
print("######Programa que clalcula a media de um aluno######")

Python = float( input ("Digite a nota de Python: "))
Java = float (input ("Digite a nota de Java: "))
Javascript = float(input("Digite a nota de Javascript: "))
Rust = float(input("Digite a nota de Rust: "))

media = (Python + Java + Javascript + Rust) / 4

print ("A nota de Python é:",Python)
print ("A nota de Java é:",Java)
print ("A nota de Javascript é:",Javascript)
print ("A nota de Rust é:",Rust)

print("A media final é:",media)

if media >= 7:
    print("Aprovado :)")
else:
    print("Reprovado!!! :(")
    
    print("$$$$ FIM $$$")



