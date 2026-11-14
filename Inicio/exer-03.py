#Receba nome, peso e altura. Calcule IMC.


#entrada 
nome=input("Digite seu nome:")
peso=float(input("Digite seu peso em kg:"))
altura=float(input("Digite sua altura em m:"))

#processo
imc=peso / altura**2

#saida
if imc<204:
    print(f"{nome} considerando sua altura e peso seu IMC é {imc}.")

if imc>204:
    print("vc está com obesidade mórbida, procure um médico.")