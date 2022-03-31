class Sokoban:
  """
  Definimos los componentes

  0- Cajas
  1- Paredes
  2- Muñeco
  3- Camino
  4- Metas
  5- Muñeco_meta
  6- Caja_meta
  """
  #Mapa inicial del juego
  mapa= [
    [1,3,3,3,3,3,3,3,3,1],    
    [1,3,3,3,3,3,3,3,3,1],
    [1,3,3,3,2,3,3,3,3,1],
    [1,3,3,3,3,3,3,3,3,1],
    [1,3,3,3,3,3,3,3,3,1],
    [1,3,3,3,3,3,3,3,3,1],
  ]
  #Posicion inicial del muñeco
  muneco_columna=4
  muneco_fila=2

  def imprimirMapa(self): #Metodo para imprimir el mapa
    for fila in self.mapa:
      print(fila)
      

  def moverDerecha(self): #Metodo para mover el personaje a la derecha
    if self.mapa[self.muneco_fila][self.muneco_columna]==2 and self.mapa[self.muneco_fila][self.muneco_columna+1]==3:
      self.mapa[self.muneco_fila][self.muneco_columna]=3
      self.mapa[self.muneco_fila][self.muneco_columna+1]=2
      self.muneco_columna+=1
      
  def moverIzquierda(self): 
    if self.mapa[self.muneco_fila][self.muneco_columna]==2 and self.mapa[self.muneco_fila][self.muneco_columna-1]==3:
      self.mapa[self.muneco_fila][self.muneco_columna]=3
      self.mapa[self.muneco_fila][self.muneco_columna-1]=2
      self.muneco_columna+=1

  def moverAbajo(self): 
    if self.mapa[self.muneco_fila][self.muneco_columna]==2 and self.mapa[self.muneco_fila+1][self.muneco_columna]==3:
      self.mapa[self.muneco_fila][self.muneco_columna]=3
      self.mapa[self.muneco_fila+1][self.muneco_columna]=2
      self.muneco_columna+=1
      


instrucciones= "q- Salir\nd- Derecha\na- Izquierda" #Variable con las instrucciones del juego
def jugar (self):
  while True: #Bucle infinito
    self.imprimirMapa()
    print (instrucciones) #Imprime las instrucciones
    movimiento= input("Mover: ") 
    if movimiento == "d": #Si el movimiento es igual a d
      juego.moverDerecha() #Llama al metodo mover derecha
    elif movimiento == "a": #Si el movimiento es igual a a
      juego.moverIzquierda() #Llama al metodo mover izquierda
    elif movimiento == "q": #Si el movimiento es igual a q
      print("Saliste del juego")
    break

juego= Sokoban() #Crea un objeto del juego Sokoban
juego.jugar() #Imprime el mapa