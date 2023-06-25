archivo = open("prueba.txt", "r")  # Abre el archivo en modo lectura

for linea in archivo:
    print(linea)  # Procesa cada línea, por ejemplo, imprímela en la consola

archivo.close()  # Cierra el archivo después de terminar de leerlo
