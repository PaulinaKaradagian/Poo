"""Ejercicio Integrador POO
Esta guía es un solo ejercicio integrador de POO.
Ejercicio único
● Crear una clase llamada Punto con sus dos coordenadas X e Y.
● Añadir un método constructor para crear puntos fácilmente. Si no se recibe una
coordenada, su valor será cero.
● Sobreescribir el método string, para que al imprimir por pantalla un punto
aparezca en formato (X,Y)
● Añadir un método llamado cuadrante que indique a qué cuadrante pertenece el
punto, teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0
e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
● Añadir un método llamado vector, que tome otro punto y calcule el vector
resultante entre los dos puntos.
● (Optativo) Añadir un método llamado distancia, que tome otro punto y calcule la
distancia entre los dos puntos y la muestre por pantalla. La fórmula es la
siguiente:
Nota:
La función raíz cuadrada en Python sqrt() se debe importar del módulo math y utilizarla
de la siguiente forma:
import math
math.sqrt(9)
● Crear una clase llamada Rectángulo con dos puntos (inicial y final) que
formarán la diagonal del rectángulo.
● Añadir un método constructor para crear ambos puntos fácilmente, si no se
envían se crearán dos puntos en el origen por defecto.
● Añadir al rectángulo un método llamado base que muestre la base.
● Añadir al rectángulo un método llamado altura que muestre la altura.
● Añadir al rectángulo un método llamado area que muestre el area.
Sugerencia:
Pueden identificar fácilmente estos valores si intentan dibujar el cuadrado a
partir de su diagonal. Recuerden que pueden utilizar la función abs() para
saber el valor absoluto de un número.
Experimentación
● Crear los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
● Consultar a qué cuadrante pertenecen el punto A, C y D.
● Consultar los vectores AB y BA.
● (Optativo) Consultar la distancia entre los puntos 'A y B' y 'B y A'.
● (Optativo) Determinar cual de los 3 puntos A, B o C, se encuentra más lejos del
origen, punto (0,0).
● Crear un rectángulo utilizando los puntos A y B.
● Consultar la base, altura y área del rectángulo."""

class Punto():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


    def __str__(self):

        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x > 0 :
            if self.y > 0 :
                return f"{self} pertenece al primer cuadrante."
            if self.y < 0:
                print(f"{self} pertenece al cuarto cuadrante")
            if self.y == 0:
                print(f"{self} Está sobre el eje x postivo")
        elif self.x < 0:
            if self.y > 0:
                print(f"{self} pertenece al segundo cuadrante")
            if self.y < 0:
                print(f"{self} pertenece al tercer cuadrante")
            if self.y == 0:
                print(f"{self} Está sobre el eje x negativo")
        elif self.x == 0:
            if self.y > 0:
                print(f"{self} Está sobre el eje y postivo")
            if self.y < 0:
                print(f"{self} Está sobre el eje y negativo")
            if self.y == 0:
                print(f"{self} coincide con el punto de origen")

    def vector(self, p):
        print(f"El vector entre {self} y {p} es ({p.x - self.x}, {p.y - self.y})")

    def distancia(self, p):
        d = math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)
        print(f"La distancia entre los puntos {self} y {p} es {d}")


class Rectangulo:

    def __init__(self, pInicial=Punto(), pFinal=Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal

        # Hago los cálculos, pero no llamo los atributos igual
        # que los métodos porque sino podríamos sobreescribirlos
        self.vBase = abs(self.pFinal.x - self.pInicial.x)
        self.vAltura = abs(self.pFinal.y - self.pInicial.y)
        self.vArea = self.vBase * self.vAltura

    def base(self):
        print(f"La base del rectÃ¡ngulo es {self.vBase}")

    def altura(self):
        print(f"La altura del rectÃ¡ngulo es {self.vAltura}")

    def area(self):
        print(f"El área del rectángulo es {self.vArea}")


A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)

A.distancia(D)
B.distancia(D)
C.distancia(D)

R = Rectangulo(A, B)
R.base()
R.altura()
R.area()