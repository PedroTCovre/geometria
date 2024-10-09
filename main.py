from geo_structures_store import Triangulo, Retangulo, Trapezio

i = int(input("Qual área você deseja consultar?\n1 - Triângulo\n2 - Retângulo\n3 - Trapézio\n"))
if i == 1:
    base = int(input("Entre com a base do triângulo: "))
    altura = int(input("Entre com a altura do triângulo: "))
    forma_geometrica = Triangulo(base,altura)
elif i == 2:
    lado1 = int(input("Entre com um dos lados do retângulo: "))
    lado2 = int(input("Entre com o outro lado do retângulo: "))
    forma_geometrica = Retangulo(lado1,lado2)
elif i == 3:
    lmaior = int(input("Entre com o lado maior do trapézio: "))
    lmenor = int(input("Entre com o lado menor do trapézio: "))
    altura = int(input("Entre com a altura do trapézio: "))
    forma_geometrica = Trapezio(lmaior,lmenor,altura)
