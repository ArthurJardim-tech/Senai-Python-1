import math

nome=input("Digite o nome do contratante: ") .lower()
peso=float(input("Digite o peso da carga: "))
capacidade=float(input("Digite a capacidade de cada caminhão: "))
distancia=float(input("Digite a distância da entrega: "))
consumo=float(input("Digite seu consumo médio de combustível: "))
preço=float(input("Digite o preço do combustível: "))

caminhao=math.ceil(peso/capacidade)
medio=math.ceil (peso/caminhao)
combustivel=(distancia/consumo)*caminhao
custo=(combustivel*preço) 
if nome=="caua":
    print("O nosso serviço nao abranje as terrinhas do painho")

else:
    print(f"Para a viagem seria necessario {caminhao} caminhão(ões), o peso medio por cada caminhao seria de {medio}kg, o consumo total de combustivel seria de {combustivel}.")
    print(f"Tudo isso custaria {custo} reias.")