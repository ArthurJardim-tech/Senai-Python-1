import math
figura=input("Qual figura geométrica voce quer (Quadrado, retangulo, triangulo, cubo, prisma, cilintro, tetraedro, cone ou esfera)? ")
if figura in ["Quadrado","retangulo","triangulo","quadrado"]:
    area1=input("Você deseja calcular a área? ")
    if area1== "sim":
        if figura=="quadrado":
            m1=float(input("Qual o lado da figura?"))
            Aquadrado=m1**2
            print(f"A área do seu quadrado é de {Aquadrado}.")
        elif figura=="triangulo":
            m1=float(input("Qual a base da figura?"))
            m2=float(input("Qual a altura da figura?"))
            Atriangulo= m1*m2/2
            print(f"A área do seu triangulo é de {Atriangulo}.")
        elif figura=="retangulo":
            m1=float(input("Qual a base da figura?"))
            m2=float(input("Qual a altura da figura?"))
            Aretangulo=m1*m2
            print(f"A área do seu retangulo é de {Aretangulo}.")

elif figura in ["cubo","prisma","cilintro","tetraedro","cone","esfera"]:
    volume=input("Você deseja calcular o volume? ")
    area2=input("Voce deseja calcular a área? ")
    if volume=="sim" or area2=="sim":
        if figura == "cubo":
            m3 = float(input("Digite a aresta: "))
            Acubo=6 * m3**2
            Vcubo=m3**3

        elif figura == "prisma":
            m3 = float(input("Digite a base: "))
            m4 = float(input("Digite a altura: "))
            m5 = float(input("Digite a largura: "))
            Aprisma= 2 * (m3*m4 + m3*m5 + m4*m5)
            Vprisma=(m3*m5)*m4

        elif figura == "cilintro":
            m3 = float(input("Digite o raio: "))
            m4 = float(input("Digite a altura: "))
            Acilintro= 2 * math.pi * m3 * (m3 + m4)
            Vcilindro=math.pi*m3**2*m4

        elif figura == "tetraedro":
            m3 = float(input("Digite a aresta: "))
            Atetraedro=m3**2 * math.sqrt(3)
            Vtetraedro=(m3**3 * math.sqrt(2)) /12

        elif figura == "cone":
            m3 = float(input("Digite o raio: "))
            m4 = float(input("Digite a altura: "))
            g = float(input("Digite a geratriz: "))
            Acone=math.pi * m3 * (m3 + g)
            Vcone=((math.pi*m3**2)*m4)/3
        
        elif figura== "esfera":
            m3=float(input("Digite o raio: "))
            Aesfera = 4 * math.pi * m3**2
            Vesfera=(math.pi*(m3**3))* 4/3

        if volume==area2=="sim":
            if figura=="cubo":
                print(f"A área e o volume do seu cubo são {Acubo} m² e {Vcubo} m³.")
            elif figura=="prisma":
                print(f"A área e o volume do seu prisma são {Aprisma} m² e {Vprisma} m³.")
            elif figura=="cilintro":
                print(f"A área e o volume do seu cilindro são {Acilintro} m² e {Vcilindro} m³.")
            elif figura=="tetraedro":
                print(f"A área e o volume do seu tetraedro são {Atetraedro} m² e {Vtetraedro} m³.")
            elif figura=="cone":
                print(f"A área e o volume do seu cone são {Acone} m² e {Vcone} m³.")
            elif figura=="esfera":
                print(f"A área e o volume da sua esfera são {Aesfera} m² e {Vesfera} m³.")

        elif volume=="sim" and area2=="nao":
            if figura=="cubo":
                print(f"O volume do seu cubo é {Vcubo} m³.")
            elif figura=="prisma":
                print(f"O volume do seu prisma é {Vprisma} m³.")
            elif figura=="cilintro":
                print(f"O volume do seu cilindro é {Vcilindro} m³.")
            elif figura=="tetraedro":
                print(f"O volume do seu tetraedro é {Vtetraedro} m³.")
            elif figura=="cone":
                print(f"O volume do seu cone é {Vcone} m³.")
            elif figura=="esfera":
                print(f"O volume da sua esfera é {Vesfera} m³.")

        elif area2=="sim" and volume=="nao":
            if figura=="cubo":
                print(f"A área do seu cubo é {Acubo} m².")
            elif figura=="prisma":
                print(f"A área do seu prisma é {Aprisma} m².")
            elif figura=="cilintro":
                print(f"A área do seu cilindro é {Acilintro} m².")
            elif figura=="tetraedro":
                print(f"A área do seu tetraedro é {Atetraedro} m².")
            elif figura=="cone":
                print(f"A área do seu cone é {Acone} m².")
            elif figura=="esfera":
                print(f"A área da sua esfera é {Aesfera} m².")
    else:
        print("Operação ecerrada.")

else:
    print("Figura geométrica não encontrada.")