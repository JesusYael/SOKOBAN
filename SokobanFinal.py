"""
  Definimos los componentes

  3- Cajas
  1- Paredes
  2- Muñeco
  0- Espacio
  4- Meta
  5- Personaje_meta
  6- Caja_meta
  """


class Sokoban:
    mapa = []
    personaje_x = 0
    personaje_y = 0

    def __init__(self):
        pass

    def cargarMapa(self):  #Carga el mapa en la matriz
        file = open("level1.txt", "r")
        self.mapa = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 1],
            [1, 0, 0, 0, 4, 0, 2, 0, 4, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

    def imprimirMapa(self):  #Imprime el mapa fila por fila
        for fila in self.mapa:
            print(fila)

    def posicionPersonaje(
            self):  #Nos dara la posicion del personaje en la matriz
        for fila in range(len(self.mapa)):
            for columna in range(len(self.mapa[fila])):
                if self.mapa[fila][columna] == 2:
                    self.personaje_x = fila
                    self.personaje_y = columna

    def movimientoIzquierda(self):  #Movimientos hacia la izquierda

        if self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x][self.personaje_y - 1] == 0:
            self.mapa[self.personaje_x][self.personaje_y] = 0
            self.mapa[self.personaje_x][self.personaje_y - 1] = 2
            self.personaje_y = self.personaje_y - 1
            print("izquierda-personaje,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x][self.personaje_y - 1] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 0
            self.mapa[self.personaje_x][self.personaje_y - 1] = 5
            self.personaje_y = self.personaje_y - 1
            print("izquierda-personaje,meta")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x][self.personaje_y - 1] == 3 and self.mapa[
                    self.personaje_x][self.personaje_y - 2] == 0:
            self.mapa[self.personaje_x][self.personaje_y] = 0
            self.mapa[self.personaje_x][self.personaje_y - 1] = 2
            self.mapa[self.personaje_x][self.personaje_y - 2] = 3
            self.personaje_y = self.personaje_y - 1
            print("izquierda-personaje,caja,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x][self.personaje_y - 1] == 3 and self.mapa[
                    self.personaje_x][self.personaje_y - 2] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 0
            self.mapa[self.personaje_x][self.personaje_y - 1] = 2
            self.mapa[self.personaje_x][self.personaje_y - 2] = 6
            self.personaje_y = self.personaje_y - 1
            print("izquierda-personaje,caja,meta")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x][self.personaje_y - 1] == 6 and self.mapa[
                    self.personaje_x][self.personaje_y - 2] == 0:
            self.mapa[self.personaje_x][self.personaje_y] = 0
            self.mapa[self.personaje_x][self.personaje_y - 1] = 5
            self.mapa[self.personaje_x][self.personaje_y - 2] = 3
            self.personaje_y = self.personaje_y - 1
            print("izquierda-personaje,caja_meta,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x][self.personaje_y - 1] == 6 and self.mapa[
                    self.personaje_x][self.personaje_y - 2] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 0
            self.mapa[self.personaje_x][self.personaje_y - 1] = 5
            self.mapa[self.personaje_x][self.personaje_y - 2] = 6
            self.personaje_y = self.personaje_y - 1
            print("izquierda-personaje,caja_meta,meta")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x][self.personaje_y - 1] == 0:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x][self.personaje_y - 1] = 2
            self.personaje_y = self.personaje_y - 1
            print("izquierda-personaje_meta,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x][self.personaje_y - 1] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x][self.personaje_y - 1] = 5
            self.personaje_y = self.personaje_y - 1
            print("izquierda-personaje_meta,meta")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x][self.personaje_y - 1] == 3 and self.mapa[
                    self.personaje_x][self.personaje_y - 2] == 0:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x][self.personaje_y - 1] = 2
            self.mapa[self.personaje_x][self.personaje_y - 2] = 3
            self.personaje_y = self.personaje_y - 1
            print("izquierda-personaje_meta,caja,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x][self.personaje_y - 1] == 3 and self.mapa[
                    self.personaje_x][self.personaje_y - 2] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x][self.personaje_y - 1] = 2
            self.mapa[self.personaje_x][self.personaje_y - 2] = 6
            self.personaje_y = self.personaje_y - 1
            print("izquierda-personaje_meta,caja,meta")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x][self.personaje_y - 1] == 6 and self.mapa[
                    self.personaje_x][self.personaje_y - 2] == 0:  #
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x][self.personaje_y - 1] = 5
            self.mapa[self.personaje_x][self.personaje_y - 2] = 3
            self.personaje_y = self.personaje_y - 1
            print("izquierda-personaje_meta,caja_meta,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x][self.personaje_y - 1] == 6 and self.mapa[
                    self.personaje_x][self.personaje_y - 2] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x][self.personaje_y - 1] = 5
            self.mapa[self.personaje_x][self.personaje_y - 2] = 6
            self.personaje_y = self.personaje_y - 1
            print("izquierda-personaje_meta,caja_meta,meta")

    def movimientoDerecha(self):  #Movimientos derecha
        if self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x][self.personaje_y + 1] == 0:
            self.mapa[self.personaje_x][self.personaje_y] = 0
            self.mapa[self.personaje_x][self.personaje_y + 1] = 2
            self.personaje_y = self.personaje_y + 1
            print("derecha-personaje,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x][self.personaje_y + 1] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 0
            self.mapa[self.personaje_x][self.personaje_y + 1] = 5
            self.personaje_y = self.personaje_y + 1
            print("derecha-personaje,meta")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x][self.personaje_y + 1] == 3 and self.mapa[
                    self.personaje_x][self.personaje_y + 2] == 0:
            self.mapa[self.personaje_x][self.personaje_y] = 0
            self.mapa[self.personaje_x][self.personaje_y + 1] = 2
            self.mapa[self.personaje_x][self.personaje_y + 2] = 3
            self.personaje_y = self.personaje_y + 1
            print("derecha-personaje,caja,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x][self.personaje_y + 1] == 3 and self.mapa[
                    self.personaje_x][self.personaje_y + 2] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 0
            self.mapa[self.personaje_x][self.personaje_y + 1] = 2
            self.mapa[self.personaje_x][self.personaje_y + 2] = 6
            self.personaje_y = self.personaje_y + 1
            print("derecha-personaje,caja,meta")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x][self.personaje_y + 1] == 6 and self.mapa[
                    self.personaje_x][self.personaje_y + 2] == 0:
            self.mapa[self.personaje_x][self.personaje_y] = 0
            self.mapa[self.personaje_x][self.personaje_y + 1] = 5
            self.mapa[self.personaje_x][self.personaje_y + 2] = 3
            self.personaje_y = self.personaje_y + 1
            print("derecha-personaje,caja_meta,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x][self.personaje_y + 1] == 6 and self.mapa[
                    self.personaje_x][self.personaje_y + 2] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 0
            self.mapa[self.personaje_x][self.personaje_y + 1] = 5
            self.mapa[self.personaje_x][self.personaje_y + 2] = 6
            self.personaje_y = self.personaje_y + 1
            print("derecha-personaje,caja_meta,meta")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x][self.personaje_y + 1] == 0:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x][self.personaje_y + 1] = 2
            self.personaje_y = self.personaje_y + 1
            print("derecha-personaje_meta,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x][self.personaje_y + 1] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x][self.personaje_y + 1] = 5
            self.personaje_y = self.personaje_y + 1
            print("derecha-personaje_meta,meta")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x][self.personaje_y + 1] == 3 and self.mapa[
                    self.personaje_x][self.personaje_y + 2] == 0:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x][self.personaje_y + 1] = 2
            self.mapa[self.personaje_x][self.personaje_y + 2] = 3
            self.personaje_y = self.personaje_y + 1
            print("derecha-personaje_meta,caja,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x][self.personaje_y + 1] == 3 and self.mapa[
                    self.personaje_x][self.personaje_y + 2] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x][self.personaje_y + 1] = 2
            self.mapa[self.personaje_x][self.personaje_y + 2] = 6
            self.personaje_y = self.personaje_y + 1
            print("derecha-personaje_meta,caja,meta")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x][self.personaje_y + 1] == 6 and self.mapa[
                    self.personaje_x][self.personaje_y + 2] == 0:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x][self.personaje_y + 1] = 5
            self.mapa[self.personaje_x][self.personaje_y + 2] = 3
            self.personaje_y = self.personaje_y + 1
            print("derecha-personaje_meta,caja_meta,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x][self.personaje_y + 1] == 6 and self.mapa[
                    self.personaje_x][self.personaje_y + 2] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x][self.personaje_y + 1] = 5
            self.mapa[self.personaje_x][self.personaje_y + 2] = 6
            self.personaje_y = self.personaje_y + 1
            print("derecha-personaje_meta,caja_meta,meta")

    def movimientoArriba(self):  #Moviminetos arriba
        if self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x - 1][self.personaje_y] == 0:
            self.mapa[self.personaje_x][self.personaje_y] = 0
            self.mapa[self.personaje_x - 1][self.personaje_y] = 2
            self.personaje_x = self.personaje_x - 1
            print("arriba-personaje,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x - 1][self.personaje_y] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 0
            self.mapa[self.personaje_x - 1][self.personaje_y] = 5
            self.personaje_x = self.personaje_x - 1
            print("arriba-personaje,meta")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x - 1][self.personaje_y] == 3 and self.mapa[
                    self.personaje_x - 2][self.personaje_y] == 0:
            self.mapa[self.personaje_x][self.personaje_y] = 0
            self.mapa[self.personaje_x - 1][self.personaje_y] = 2
            self.mapa[self.personaje_x - 2][self.personaje_y] = 3
            self.personaje_x = self.personaje_x - 1
            print("arriba-personaje,caja,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x - 1][self.personaje_y] == 3 and self.mapa[
                    self.personaje_x - 2][self.personaje_y] == 4:
            self.mapa[self.personaje_x][
                self.personaje_y] = 0  # put floor character last position
            self.mapa[self.personaje_x - 1][
                self.personaje_y] = 2  # move the character to next position
            self.mapa[self.personaje_x - 2][self.personaje_y] = 6
            self.personaje_x = self.personaje_x - 1  # update the character position
            print("arriba-personaje,caja,meta")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x - 1][self.personaje_y] == 6 and self.mapa[
                    self.personaje_x - 2][self.personaje_y] == 0:
            self.mapa[self.personaje_x][
                self.personaje_y] = 0  # put floor character last position
            self.mapa[self.personaje_x - 1][
                self.personaje_y] = 5  # move the character to next position
            self.mapa[self.personaje_x - 2][self.personaje_y] = 3
            self.personaje_x = self.personaje_x - 1  # update the character position
            print("arriba-personaje,caja_meta,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x - 1][self.personaje_y] == 6 and self.mapa[
                    self.personaje_x - 2][self.personaje_y] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 0
            self.mapa[self.personaje_x - 1][self.personaje_y] = 5
            self.mapa[self.personaje_x - 2][self.personaje_y] = 6
            self.personaje_x = self.personaje_x - 1
            print("arriba-personaje,caja_meta,meta")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x - 1][self.personaje_y] == 0:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x - 1][self.personaje_y] = 2
            self.personaje_x = self.personaje_x - 1
            print("arriba-personaje_meta,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x - 1][self.personaje_y] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x - 1][self.personaje_y] = 5
            self.personaje_x = self.personaje_x - 1
            print("arriba-personaje_meta,meta")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x - 1][self.personaje_y] == 3 and self.mapa[
                    self.personaje_x - 2][self.personaje_y] == 0:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x - 1][self.personaje_y] = 2
            self.mapa[self.personaje_x - 2][self.personaje_y] = 3
            self.personaje_x = self.personaje_x - 1
            print("arriba-personaje_meta,caja,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x - 1][self.personaje_y] == 3 and self.mapa[
                    self.personaje_x - 2][self.personaje_y] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x - 1][self.personaje_y] = 2
            self.mapa[self.personaje_x - 2][self.personaje_y] = 6
            self.personaje_x = self.personaje_x - 1
            print("arriba-personaje_meta,caja,meta")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x - 1][self.personaje_y] == 6 and self.mapa[
                    self.personaje_x - 2][self.personaje_y] == 0:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x - 1][self.personaje_y] = 5
            self.mapa[self.personaje_x - 2][self.personaje_y] = 3
            self.personaje_x = self.personaje_x - 1
            print("arriba-personaje_meta,caja_meta,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x - 1][self.personaje_y] == 6 and self.mapa[
                    self.personaje_x - 2][self.personaje_y] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x - 1][self.personaje_y] = 5
            self.mapa[self.personaje_x - 2][self.personaje_y] = 6
            self.personaje_x = self.personaje_x - 1
            print("arriba-personaje_meta,caja_meta,meta")

    def movimientoAbajo(self):  #Movimientos abajo
        if self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x + 1][self.personaje_y] == 0:
            self.mapa[self.personaje_x][self.personaje_y] = 0
            self.mapa[self.personaje_x + 1][self.personaje_y] = 2
            self.personaje_x = self.personaje_x + 1
            print("abajo-personaje,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x + 1][self.personaje_y] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 0
            self.mapa[self.personaje_x + 1][self.personaje_y] = 5
            self.personaje_x = self.personaje_x + 1
            print("abajo-personaje,meta")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x + 1][self.personaje_y] == 3 and self.mapa[
                    self.personaje_x + 2][self.personaje_y] == 0:
            self.mapa[self.personaje_x][self.personaje_y] = 0
            self.mapa[self.personaje_x + 1][self.personaje_y] = 2
            self.mapa[self.personaje_x + 2][self.personaje_y] = 3
            self.personaje_x = self.personaje_x + 1
            print("abajo-personaje,caja,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x + 1][self.personaje_y] == 3 and self.mapa[
                    self.personaje_x + 2][self.personaje_y] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 0
            self.mapa[self.personaje_x + 1][self.personaje_y] = 2
            self.mapa[self.personaje_x + 2][self.personaje_y] = 6
            self.personaje_x = self.personaje_x + 1
            print("abajo-personaje,caja,meta")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x + 1][self.personaje_y] == 6 and self.mapa[
                    self.personaje_x + 2][self.personaje_y] == 0:
            self.mapa[self.personaje_x][self.personaje_y] = 0
            self.mapa[self.personaje_x + 1][self.personaje_y] = 5
            self.mapa[self.personaje_x + 2][self.personaje_y] = 3
            self.personaje_x = self.personaje_x + 1
            print("abajo-personaje,caja_meta,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x + 1][self.personaje_y] == 6 and self.mapa[
                    self.personaje_x + 2][self.personaje_y] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 0
            self.mapa[self.personaje_x + 1][self.personaje_y] = 5
            self.mapa[self.personaje_x + 2][self.personaje_y] = 6
            self.personaje_x = self.personaje_x + 1
            print("abajo-personaje,caja_meta,meta")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x + 1][self.personaje_y] == 0:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x + 1][self.personaje_y] = 2
            self.personaje_x = self.personaje_x + 1
            print("abajo-personaje_meta,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x + 1][self.personaje_y] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x + 1][self.personaje_y] = 5
            self.personaje_x = self.personaje_x + 1
            print("abajo-personaje_meta,meta")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x + 1][self.personaje_y] == 3 and self.mapa[
                    self.personaje_x + 2][self.personaje_y] == 0:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x + 1][self.personaje_y] = 2
            self.mapa[self.personaje_x + 2][self.personaje_y] = 3
            self.personaje_x = self.personaje_x + 1
            print("abajo-personaje_meta,caja,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x + 1][self.personaje_y] == 3 and self.mapa[
                    self.personaje_x + 2][self.personaje_y] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x + 1][self.personaje_y] = 2
            self.mapa[self.personaje_x + 2][self.personaje_y] = 6
            self.personaje_x = self.personaje_x + 1
            print("abajo-personaje_meta,caja,meta")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x + 1][self.personaje_y] == 6 and self.mapa[
                    self.personaje_x + 2][self.personaje_y] == 0:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x + 1][self.personaje_y] = 5
            self.mapa[self.personaje_x + 2][self.personaje_y] = 3
            self.personaje_x = self.personaje_x + 1
            print("abajo-personaje_meta,caja_meta,espacio")

        elif self.mapa[self.personaje_x][self.personaje_y] == 5 and self.mapa[
                self.personaje_x + 1][self.personaje_y] == 6 and self.mapa[
                    self.personaje_x + 2][self.personaje_y] == 4:
            self.mapa[self.personaje_x][self.personaje_y] = 4
            self.mapa[self.personaje_x + 1][self.personaje_y] = 5
            self.mapa[self.personaje_x + 2][self.personaje_y] = 6
            self.personaje_x = self.personaje_x + 1
            print("abajo-personaje_meta,caja_meta,meta")

    def powerup(self):  #Powerup para poder jalar cajas

        if self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x + 1][self.personaje_y] == 3 and self.mapa[
                    self.personaje_x + 2][self.personaje_y] == 1:
            self.mapa[self.personaje_x][self.personaje_y] = 3
            self.mapa[self.personaje_x + 1][self.personaje_y] = 0
            self.mapa[self.personaje_x - 1][self.personaje_y] = 2
            self.personaje_x = self.personaje_x - 1
            print("arriba-jalar caja para arriba")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x - 1][self.personaje_y] == 3 and self.mapa[
                    self.personaje_x - 2][self.personaje_y] == 1:
            self.mapa[self.personaje_x][self.personaje_y] = 3
            self.mapa[self.personaje_x - 1][self.personaje_y] = 0
            self.mapa[self.personaje_x + 1][self.personaje_y] = 2
            self.personaje_x = self.personaje_x + 1
            print("abajo-jalar caja para abajo")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x][self.personaje_y - 1] == 3 and self.mapa[
                    self.personaje_x][self.personaje_y - 2] == 1:
            self.mapa[self.personaje_x][self.personaje_y] = 3
            self.mapa[self.personaje_x][self.personaje_y - 1] = 0
            self.mapa[self.personaje_x][self.personaje_y + 1] = 2
            self.personaje_y = self.personaje_y + 1
            print("derecha-jalar caja hacia la derecha")

        elif self.mapa[self.personaje_x][self.personaje_y] == 2 and self.mapa[
                self.personaje_x][self.personaje_y + 1] == 3 and self.mapa[
                    self.personaje_x][self.personaje_y + 2] == 1:
            self.mapa[self.personaje_x][self.personaje_y] = 3
            self.mapa[self.personaje_x][self.personaje_y + 1] = 0
            self.mapa[self.personaje_x][self.personaje_y - 1] = 2
            self.personaje_y = self.personaje_y - 1
            print("izquierda-jalar caja hacia la izquierda")

    def checkLevelComplete(self):
        """_summary_: Check if the level is complete
        """
        # TODO: Check if the level is complete
        # If return True, the level is complete
        # If return False, the level is not complete
        return False

    def jugar(self):
        """_summary_: Play the game
        """
        self.cargarMapa()  # Call the map
        self.posicionPersonaje()  # Update the character position for new map
        instructions = "d-Right, a-Left, w-Up, s-Down"  # Instructions
        print(instructions)  # Print the instructions
        while True:  # Infinite loop
            complete = self.checkLevelComplete(
            )  # Check if the level is complete
            if complete == True:  # If the level is complete
                print("Level Complete")  # Print the level complete
                input("Press Enter to continue..."
                      )  # Wait for the user to press enter
                self.cargarMapa()  # Call the map
                self.posicionPersonaje(
                )  # Update the character position for new map
            self.imprimirMapa()  # Call the printMap method
            print("Character position: [{},{}]".format(
                self.personaje_x,
                self.personaje_y))  # Print the character position
            move = input("Select move: ")  # Ask for the move
            if move == 'a':  # If the move is left
                self.movimientoIzquierda()  # Call moveLeft rules
            elif move == 'd':  # If the move is right
                self.movimientoDerecha()  # Call moveRight rules
            elif move == 'w':  # If the move is up
                self.movimientoArriba()  # Call moveUp rules
            elif move == 's':  # If the move is down
                self.movimientoAbajo()  # Call moveDown rules
            elif move == "e":
                self.powerup()  #Se agarran las cajas
            elif move == 'q':  # If the move is quit
                break  # Game quit


game = Sokoban()  # Create a object from Sokoban class
game.jugar()  # Fun Fun Fun ;)
