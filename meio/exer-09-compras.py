import math
valor=float(input("Digite o valo da compra: "))
cliente=input("Digite seu tipo de fidelidade(comum ou premium):") .lower()
pagamento=input("Digite a forma de pagamento(pix ou cartao): ") .lower()

if cliente=="premium":
    desconto=valor*0.90
    if pagamento=="pix":
        desconto2=math.ceil(desconto*0.97)
        print(f"Seu valor será de {desconto2}")
    if pagamento=="cartao":
        print(f"Seu valor será de {desconto}")
if cliente=="comum":
    if valor>=200:
        desconto=valor*0.95
        if pagamento=="pix":
            desconto2=math.ceil(desconto*0.97)
            print(f"Seu valor será de {desconto2}")
        if pagamento=="cartao":
            print(f"Seu valor será de {desconto}")
    if valor<200:
        if pagamento=="pix":
            valor=desconto*0.97
            print(f"Seu valor será de {desconto}")
        if pagamento=="cartao":
            print(f"Seu valor será de {valor}")
        
if valor<0 or cliente not in["comum","premium"] or pagamento not in["pix","cartao"]:
    print("Informações invalidas")