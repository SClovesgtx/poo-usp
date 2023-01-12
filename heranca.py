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
        """
        Aqui eu adiciono um método que especializa a classe filha.
        """
        a, b, c = self.lados
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print(f"A área do triângulo é {round(area, 2)}.\n")


class Retangulo(Poligono):
    def __init__(self) -> None:
        super().__init__(numero_de_lados=4)
    
    def le_dados(self):
        """
        Aqui eu altero o comportamento do método
        da classe mãe
        """
        lado1 = float(input(f"Digite o tamanho da altura: \n"))
        lado2 = float(input(f"Digite o tamanho do comprimento: \n"))
        self.lados[0] = self.lados[2] = lado1
        self.lados[1] = self.lados[3] = lado2

    def area(self):
        print(f"Aréa do retêngulo é {self.lados[0] * self.lados[1]}.\n")

    def diagonal(self):
        print(f"A diagonal do retângulo mede {(self.lados[0]**2 + self.lados[1]**2) ** 0.5}.\n")


triangulo = Triangulo()
 # como o triangulo não implementa este método ele sobe para suas 
 # para as suas superclasses até encontrar a primeira super classe
 # que implementa este método e o executa (que no nosso caso é a classe Poligono)
triangulo.le_dados()
triangulo.area()

ret = Retangulo()
ret.le_dados()
ret.area()
ret.diagonal()