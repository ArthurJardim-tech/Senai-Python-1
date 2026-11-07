#receba essa idade em anos e imprima em mesese, dias,horas e minutos


#entrada = idade
#int = ele pega o texto e converte para numero
idade = int(input("Digite a sua idade: "))

#processo
meses= idade*12
dias= idade*365
horas= dias*24
minutos= horas*60
segundos= minutos*60
nascimento= 2026-idade


#saida
if idade<117:
    print(f"Se vc tem {idade} anos, vc tem: {meses} meses, {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos de vida e nasceu em {nascimento}.16")

if idade>117:
    print("🥳Parabéns🥳 você é a pessoa mais velha da terra.")