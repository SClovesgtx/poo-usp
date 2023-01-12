class Poligono:
    def __init__(self, numero_de_lados: int) -> None:
        self.n = numero_de_lados
        self.lados = [0 for i in range(numero_de_lados)]
    
    def le_dados(self):
        self.lados = [float(input(f"Digite o tamanho do lado {i+1}: \n")) for i in range(self.n)]

    def mostra_lados(self):
        for i in range(self.n):
            print(f"O tamanho do lado {i+1} é {self.lados[i]}.\n")

class Triangulo(Poligono):
    def __init__(self) -> None:
        super().__init__(numero_de_lados=3)
    
    def area(self):
        a, b, c = self.lados
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print(f"A área do triângulo é {round(area, 2)}.\n")


class Retangulo(Poligono):
    def __init__(self) -> None:
        super().__init__(numero_de_lados=4)


triangulo = Triangulo()
triangulo.le_dados()
triangulo.area()