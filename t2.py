class sokoban:
  mapa= [file]

  def cargarNivel(self):
    file= open("nivel1.sokoban","r")
  for x in file:
    print(fila,end="")
    for y in file:
      print(columna,end="")
      print()
    #Aqui va codigo



sokoban= Sokoban[]
print (sokoban.mapa)
sokoban.cargarNivel()
print (sokoban.mapa)