# INDICE
# Linea 11: Identidad entre objetos
# Linea 27: Operadores Lógicos
# Linea 36: Listas
# Linea 72: Tuplas
# Linea 105: Lectura de archivos



# -------------------------------------------------------------------------------------------

# Identidad entre objetos 

text1 = ("Hola, soy un texto")
text2 = ("Hola, soy un texto")

print("text1:", id(text1))  # Muestra la dirección de memoria del objeto text1
print("text2:", id(text2))  # Muestra la dirección de memoria del objeto text2

print(text1 is text2)  # False, porque son objetos diferentes en memoria
print(text1 == text2)  # True, porque el contenido es el mismo

# IDENTIDAD: is true si ambos objetos son el mismo en memoria
# IGUALDAD: == true si ambos objetos tienen el mismo contenido

# --------------------------------------------------------------------------------------------

# Operadores Lógicos

# Modifican expresiones evaluadas en un contexto booleano para crear condiciones más complejas
# not => invierte el valor booleano de la expresión. TRUE si x es FALSE, y viceversa
# or => devuelve TRUE si al menos una de las expresiones es TRUE
# and => devuelve TRUE si ambas expresiones son TRUE

# --------------------------------------------------------------------------------------------

# Listas

# Son colecciones ordenadas de elementos que pueden ser de diferentes tipos
# Se definen con corchetes []
# Pueden contener duplicados y son mutables (se pueden modificar)

# Ejemplo de lista
my_list = [1, 2, 3, "Hola", True]

# Acceso a elementos de la lista
print(my_list[0])  # Imprime el primer elemento de la lista (1)
print(my_list[3])  # Imprime el cuarto elemento de la lista ("Hola")

# Modificación de elementos de la lista
my_list[1] = 10  # Cambia el segundo elemento de la lista a 10
print(my_list)  # Imprime la lista modificada [1, 10, 3, "Hola", True]

# Agregar elementos a la lista
my_list.append("Nuevo elemento")  # Agrega un nuevo elemento al final de la lista
print(my_list)  # Imprime la lista con el nuevo elemento agregado

# Eliminar elementos de la lista
my_list.remove(3)  # Elimina el primer elemento con valor 3 de la lista
print(my_list)  # Imprime la lista sin el elemento 3

# Concatenar listas
another_list = [4, 5, 6]
my_list += another_list  # Agrega los elementos de another_list a my_list
print(my_list)  # Imprime la lista concatenada [1, 10, "Hola", True, "Nuevo elemento", 4, 5, 6]

# Longitud, minimo y maximo de la lista
print(len(my_list))  # Imprime la longitud de la lista (7 en este caso)
print(min(my_list))  # Imprime el valor mínimo de la lista (1)
print(max(my_list))  # Imprime el valor máximo de la lista (True, que se evalúa como 1 en este contexto)

# --------------------------------------------------------------------------------------------
# Tuplas

# Son colecciones ordenadas e inmutables de elementos
# Se definen con paréntesis ()
# No se pueden modificar una vez creadas

my_tuple = (1, 2, 3, "Hola", True)

# Acceso a elementos de la tupla
print(my_tuple[0])  # Imprime el primer elemento de la tupla (1)
print(my_tuple[3])  # Imprime el cuarto elemento de la tupla ("Hola")

# Longitud, minimo y maximo de la tupla
print(len(my_tuple))  # Imprime la longitud de la tupla (5 en este caso)
print(min(my_tuple))  # Imprime el valor mínimo de la tupla (1)
print(max(my_tuple))  # Imprime el valor máximo de la tupla (True, que se evalúa como 1 en este contexto)

# Concatenar tuplas
another_tuple = (4, 5, 6)
my_tuple += another_tuple  # Agrega los elementos de another_tuple a my_tuple
print(my_tuple)  # Imprime la tupla concatenada (1, 2, 3, "Hola", True, 4, 5, 6)

# Tuplas de un solo elemento
single_element_tuple = (42,)  # Nota la coma al final para indicar que es una tupla de un solo elemento

# Empaquetado y desempaquetado de tuplas
packed_tuple = (1, 2, 3)
a, b, c = packed_tuple  # Desempaquetado de la tupla en variables a, b y c
print(a, b, c)  # Imprime los valores desempaquetados (1, 2, 3)

# --------------------------------------------------------------------------------------------

# Lectura de archivos

# Abrir un archivo en modo lectura
with open("example.txt", "r") as file:
    # Leer todo el contenido del archivo
    content = file.read()
    print(content)  # Imprime el contenido del archivo

# Leer línea por línea
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # Imprime cada línea del archivo, eliminando espacios en blanco al principio y al final

# Leer un archivo y almacenar su contenido en una lista
with open("example.txt", "r") as file:
    lines = file.readlines()  # Lee todas las líneas del archivo y las almacena en una lista
    print(lines)  # Imprime la lista de líneas

# Leer un archivo y procesar su contenido
with open("example.txt", "r") as file:
    for line in file:
        if "Python" in line:  # Verifica si la palabra "Python" está en la línea
            print(line.strip())  # Imprime la línea si contiene "Python"

# Escribir en un archivo
with open("output.txt", "w") as file:
    file.write("Hola, este es un archivo de salida.\n")  # Escribe una línea en el archivo

# Agregar contenido a un archivo existente
with open("output.txt", "a") as file:
    file.write("Agregando una nueva línea al archivo.\n")  # Agrega una línea al final del archivo existente

# git push -u origin main






