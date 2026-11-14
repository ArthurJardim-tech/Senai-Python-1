#receba o ano de nascimento e o ano atual, e calcule a idade e semanas

#entrada
nascimento = int(input("Digite seu ano de nascimento:"))
ano = int(input("Digite o ano atual:"))


#construção

idade = ano-nascimento
semanas=idade*4*12

#saida
if nascimento<ano:
    print(f"Se você nasceu em {nascimento} e estamos em {ano} você tem {idade} de idade e {semanas} semanas de vida.")

if nascimento>ano:
    print("Parabéns você viajou no tempo.")


















