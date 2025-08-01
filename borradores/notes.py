# INDICE
# Linea 11: Identidad entre objetos
# Linea 27: Operadores Lógicos
# Linea 36: Listas
# Linea 72: Tuplas
# Linea 105: Lectura de archivos
# Linea 138: Diccionarios
# Linea 176: Bytes
# Linea 280: OOP, Object Oriented Prog.



# -------------------------------------------------------------------------------------------

# Identidad entre objetos 

text1 = ("Hola, soy un texto")
text2 = ("Hola, soy un texto")

print("text1:", id(text1))  # Muestra la dirección de memoria del objeto text1
print("text2:", id(text2))  # Muestra la dirección de memoria del objeto text2

print(text1 is text2)  # False, porque son objetos diferentes en memoria
print(text1 == text2)  # True, porque el contenido es el mismo

# IDENTIDAD: is true si ambos objetos son el mismo en memoria: son la misma cosa
# IGUALDAD: == true si ambos objetos tienen el mismo contenido: no son la misma cosa, pero valen lo mismo

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
# print(min(my_list))  # Imprime el valor mínimo de la lista si todos los valores fueran enteros, como hay mas de un tipo, habra un TypeError (1)
# print(max(my_list))  # Imprime el valor máximo de la lista (True, que se evalúa como 1 en este contexto)

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
# print(min(my_tuple))  # Imprime el valor mínimo de la tupla (1), igual que en las listas, si hay mas tipos que no sean enteros, TypeError
# print(max(my_tuple))  # Imprime el valor máximo de la tupla (True, que se evalúa como 1 en este contexto)

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

# ---------------------------------------------------------------------------------------------------------------------
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

# --------------------------------------------------------------------------------------------

# Diccionarios

# Son colecciones desordenadas de pares clave-valor
# Se definen con llaves {}
my_dict = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceso a valores por clave
print(my_dict["nombre"])  # Imprime el valor asociado a la clave "nombre" (Juan)

# Modificación de valores
my_dict["edad"] = 31  # Cambia el valor asociado a la clave "edad" a 31
print(my_dict)  # Imprime el diccionario modificado

# Agregar nuevos pares clave-valor
my_dict["profesion"] = "Ingeniero"  # Agrega un nuevo par clave-valor al diccionario
print(my_dict)  # Imprime el diccionario con el nuevo par agregado

# Eliminar un par clave-valor
del my_dict["ciudad"]  # Elimina el par clave-valor asociado a la clave "ciudad"
print(my_dict)  # Imprime el diccionario sin el par "ciudad"

# Longitud del diccionario
print(len(my_dict))  # Imprime la cantidad de pares clave-valor en el diccionario (3 en este caso)

# Recorrer un diccionario
for key, value in my_dict.items():
    print(f"{key}: {value}")  # Imprime cada clave y su valor asociado

# --------------------------------------------------------------------------------------------

# Bytes

# 1 byte = 8 bits
# Son inmutables
# El tipo de dato es "bytes" 
# La sintaxis es, b'<cadena de bytes>'. La cadena está en formato hexadecimal

byte_chain = b'\x02\x1f' # 543. reserva dos bytes de memoria con valor hexadecimal
print(type(byte_chain))
print(byte_chain)

byte_chain_bin = bin(543) # pasar int a binario
print(byte_chain_bin)

byte_chain_hex = hex(543) # pasar int a hexadecimal
print(byte_chain_hex)

byte_chain = int.from_bytes(byte_chain, "big") # pasar de bytes a integer
print(byte_chain)

bythe_chain_2 = bytes(3) # reservar bytes, en este caso tres, de memoria
print(bythe_chain_2)

# Transforma datos en bytes

data_tobyte = b"Bytes"
print(type(data_tobyte))
print(data_tobyte)

# Representacion de bytes en ASCII

byte_chain_3 = b"\x41\x42\x40" # A, B y C en ASCII
hex_to_int = int("41", base=16)
print(hex_to_int)

slicing = byte_chain_3[-1:] # accede al valor decimal que corresponde en ASCII "@"
slicing_2 = byte_chain_3[-1] # accede al valor decimal 
print(slicing)
print(slicing_2)

# Operaciones con bytes

byte_chain_4 = b'\x41\x20\x51'
byte_chain_5 = b'\x03\x01\x14\x65\x24\x5b\x19\x34'

byte_op = byte_chain_4 * 3
print(byte_op)

# ByteArrays
# Cadenas de bytes similar a bytes pero son MUTABLES
# Se identifica como bytearray(). Es una funcion, los parametros son la propia cadena

byte_array = bytearray(b'\x20\x19\x61\x62\x39\x40')
print(byte_array)
print(type(byte_array))

# Acceso a los elementos
print(byte_array[0])
print(byte_array[0:4])

# Modificacion de elementos
byte_array[0] = 0x30  # Cambia el primer elemento a 0x30 (48 en decimal)
byte_array[1:3] = bytearray(b'\x31\x32')  # Cambia los elementos del índice 1 al 2 a 0x31 y 0x32 (49 y 50 en decimal)
byte_array[0:1] = b'A' # Los valores ASCII deben ser accedidos mediante slicing, sino, dara error

print(byte_array)
print(byte_array[0])
print(byte_array[1:3])

# help(ord) # Return the Unicode code point for a one-character string.
# help(chr) #  Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.

print(ord('X')) # returns '88'
print(chr(97)) # returns 'a'

cad1 = bytearray(bytes(9))
print((cad1))

n = 97
index = 0

while index < 9:
    cad1[index] = n
    n += 1
    index += 1

print(cad1)

for letter in cad1:
    print(f'{letter} = {chr(letter)}')

# --------------------------------------------------------------------------------------------

def print_alph():
    for i in range(97, 123):
        print(chr(i))

    alph = []
    for i in range(ord('a'), ord('z') + 1):
        alph.append(chr(i))
    print(alph)

print_alph()
print()

# --------------------------------------------------------------------------------------------

# Object oriented programing

# NameSpace: Un espacio de nombres es un contenedor que permite agrupar identificadores (nombres) y evitar colisiones entre ellos.
# se accede a los namespaces mediante scope, que es el contexto en el que se puede acceder a un identificador. Global o local.

# Classes, decorators and properties
class Car: # Se declara una clase que contendra objetos de esa clase. una clase coche creara objetos de clase coche

    def __init__(self, brand, model, year, power, fuel_cons, km): # los parametros que una clase coche deberia tener
        self.brand = brand
        self.model = model
        self.year = year
        self.power = power
        self.fuel_cons = fuel_cons
        self.km = km

    """def __str__(self): # la function str devuelve los resultados como strings, ya que sino, devilveria la posicion de memoria del objeto
        return f'{self.brand, self.model, self.year, self.power, self.fuel_cons, self.km}'"""
    
    def print_parm(self):
        print  (f'- Brand: {self.brand}\n'
                f'- Model: {self.model}\n'
                f'- Year: {self.year}\n'
                f'- Power: {self.power} Hp\n'
                f'- Fuel Consumption: {self.fuel_cons} l/100\n'
                f'- Kilometers: {self.km} km\n')
        

car1 = Car('BMW', 'X5', 2025, 213, 15, 0)

car1.print_parm()
car1.km = 15
car1.print_parm()

# Herencias

class ElectricCar(Car):
    def __init__(self, brand, model, year, power, fuel_cons, km, battery):
        super().__init__(brand, model, year, power, fuel_cons, km)
        self.battery = battery

    def battery_details(self):
        print(f'Battery capacity: {self.battery} Kwh/100\n')

car2 = ElectricCar('Tesla', 'Model X', 2024, 290, 11, 0, 564)

car2.print_parm() 
car2.battery_details()

# string utils
string = 'The universe is, and we are'
print(string.lower()) # vuelve todos los caracteres minusculas: the universe is, and we are
print(string.swapcase()) # cambia las mayusculas por minusculas y las minusculas por mayusculas: tHE UNIVERSE IS, AND WE ARE
print(string.title()) # por cada letra precedida de espacio, la vuelve mayuscula: The Universe Is, And We Are
print(string.upper()) # todos los caracteres mayusculas: THE UNIVERSE IS, AND WE ARE
print(string.count('e')) # cuenta todas las coincidencias: 5
print(string.count('we')) # 1
print(string.find('e')) # devuelve el indice de la primera coincidencia: 2
print(string.find('T')) # 0
print(string.find('t')) # devuelve -1 si es error, no hay coincidencias (case sensitive)

# string format
print(string.center(20)) # centra con 20 caracteres por cada lado
print(string.ljust(20)) # justifica a la izquierda y añade 20 caracteres vacios por la derecha
print(string.lstrip()) # elimina los espacios que va encontrando desde la izquierda hasta que topa con un caracter y lo devuelve
print(string.rstrip()) # lo mismo pero por la derecha
print(string.strip()) # elimina los espacios por ambos lados
print(string.replace(' ', '')) # reemplaza las coincidencias del priemr argumento por un segundo
print(string.split())

string2 = '  The    Universe   Is    And We   Are    '
string2 = ' '.join(string2.split()) # elimina espacios de mas entre palabras
print(string2)  # Output: Hola Que Tal

string3 = ' '.join(string) # añade un espacio entre todos los caracteres
print(string3)

# --------------------------------------------------------------------------------------------

# Exceptions

# assert: se usa para verificar condiciones y lanzar una excepción si la condición no se cumple
passwd = input('password: ')
assert len(passwd) > 8, 'password cant be less than 8 characters' # si el input es menor de 8 caracteres, lanza error

# try-except: se usa para manejar excepciones y evitar que el programa se detenga
try:
    passwd1 = int(input('enter a number: '))
    print(f'you entered: {passwd1}')
except ValueError as e:
    print(f'Error: {e}. please enter a valid number.')

# finally: se usa para ejecutar código que siempre se ejecutará, independientemente de si se produjo una excepción o no
try:
    passwd2 = int(input('enter another number: '))
    print(f'you entered: {passwd2}')
except ValueError as e:
    print(f'Error: {e}. please enter a valid number.')
finally:
    print('this will always execute, regardless of whether an exception occurred or not.')

try:
    undefined = None
except NameError:
    print('variable not defined')
    undefined = True
finally:
    del undefined # remove the unused variable from memory to securize