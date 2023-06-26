archivo = open("prueba.txt", "r")  # Abre el archivo en modo lectura

for linea in archivo:
    print(linea)  # Procesa cada línea, por ejemplo, imprímela en la consola

archivo.close()  # Cierra el archivo después de terminar de leerlo

#Analiza un programa escrito en txt, asumiendo buena sintaxis,
#imprimiendo caracteristicas basicas del programa en cuestión.
# txt -> None
def analizador(texto):
    cfg = []
    with open(str(texto),"r") as programa:
      for linea in programa:
        a = linea.split()
        cfg.append(a)
    
    print(prob)
    
    nodos = 1
    arcos = 1
    conexo = 1
    var_ind = []
    com_ciclo = 1


    print("CFG")
    print("Nodos: " + str(nodos))
    print("Arcos: " + str(arcos))
    print("Componentes conexos: " + str(conexo))
    print()
    print("Variables indefinidas")
    for var in var_ind:
        print("Variable: " + var)
        print("Camino: " ) #insertar camino
    print()
    print("Complejidad ciclomatica")
    print(str(com_ciclo))


#Ejemplo
analizador(Prueba.txt)