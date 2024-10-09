class GeoStructure:
    def print_calculando(self,tipo):
        print("Calculando a área do",tipo)
    
    def calcula_area_retangulo(self,l1,l2):
        self.print_calculando('retângulo')
        return l1*l2
    
    def calcula_area_triangulo(self,base,altura):
        self.print_calculando('triângulo')
        return base*altura/2
    
    def calcula_area_trapezio(self,lmaior,lmenor,altura):
        self.print_calculando('trapézio')
        return (lmaior+lmenor)*altura/2
    
class Retangulo(GeoStructure):
    def __init__(self,l1,l2):
        self.lado1 = l1
        self.lado2 = l2
        self.area = GeoStructure().calcula_area_retangulo(self.lado1,self.lado2)

class Triangulo(GeoStructure): 
    def __init__(self,base,h):
        self.base = base
        self.altura = h
        self.area = GeoStructure().calcula_area_triangulo(self.base,self.altura)

class Trapezio(GeoStructure):
    def __init__(self,lmaior,lmenor,h):
        self.lmaior = lmaior
        self.lmenor = lmenor
        self.altura = h
        self.area = GeoStructure().calcula_area_trapezio(self.lmaior,self.lmenor,self.altura)
