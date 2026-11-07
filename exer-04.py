#Receba nome, cargo e salário e acrescente 10%
nome=input("Digite seu nome:")
cargo=input("Digite seu nome:")
salário=float(input("Digite seu salário:"))

#construção
new=salário + salário/100*10

print(f"Parabéns {nome}, você recebeu uma promoção de 10%, seu novo salário é de {new}")