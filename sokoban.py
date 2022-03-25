print("Hola mundo")
class Sokoban:
  """
  Definimos los componentes

  0- Cajas
  1- Paredes
  2- Muñeco
  3- Camino
  4- Metas
  """
  posicion_columna=4 #Posicion inicial del muñeco
  mapa= [1,3,3,3,2,3,3,3,1] #Mapa inicial del juego

  def __init__(self): #Metodo para inicializar el objeto
    pass #Inicializacion del objeto

  def imprimirMapa(self): #Metodo para imprimir el mapa
    for i in self.mapa: #Recorre cada posicion del mapa
      if i==3: #Si el elemento es un 3 (camino)
        print(" ",end="") #Imprime " " y no da salto de linea
      elif i==2: #Si el elemento es un 2 (muñeco)
        print(chr(64),end="") #Imprime @ y no da salto de linea
      elif i==1: #Si el elemento es un 1 (pared)
        print("|",end="") #Imprime | y no da salto de linea
      else: #De lo contrario
        print(i,end="") #Imprime el elemento encontrado
    print() #Imprime una linea en blanco

  def moverDerecha(self): #Metodo para mover el personaje a la derecha
    self.posicion_columna +=1 #Actualiza la posicion a la derecha
    self.mapa[self.posicion_columna]=2 #Coloca al muñeco en la nueva posicion
    self.mapa[self.posicion_columna -1]=3 #Coloca un espacio donde estaba el muñeco
    self.imprimirMapa() #Imprime el mapa actualizado

  def moverIzquierda(self): #Metodo para mover el personaje a la izquierda
    self.posicion_columna -=1 #Actualiza la posicion a la izquierda
    self.mapa[self.posicion_columna]=2 #Coloca al muñeco en la nueva posicion
    self.mapa[self.posicion_columna +1]=3 #Coloca un espacio donde estaba el muñeco
    self.imprimirMapa() #Imprime el mapa actualizado

juego= Sokoban() #Crea un objeto del juego Sokoban
juego.imprimirMapa() #Imprime el mapa

instrucciones= "q- Salir\nd- Derecha\na- Izquierda" #Variable con las instrucciones del juego

while True: #Bucle infinito
  print (instrucciones) #Imprime las instrucciones
  movimiento= input("Mover: ") #Lee hacia donde se quiere mover el muñeco
  if movimiento == "d": #Si el movimiento es igual a d
    juego.moverDerecha() #Llama al metodo mover derecha
  elif movimiento == "a": #Si el movimiento es igual a a
      juego.moverIzquierda() #Llama al metodo mover izquierda
  elif movimiento == "q": #Si el movimiento es igual a q
    print("Saliste del juego")
    break