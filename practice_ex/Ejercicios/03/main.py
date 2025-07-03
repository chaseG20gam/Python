
"""
- Ejercicio 03: Extraer partes de una palabra

Objetivo: Practicar slicing de strings, funciones personalizadas y return

Instrucciones:
1. Crea una función llamada `ex_start` que reciba un argumento
    - word_str
2. La función debe devolver los 3 primeros caracteres de ese string
3. El un argumento que espera lafunción debe ser `"developer"`
4. Guarda el resultado de la función en una variable llamada `result`
5. Imprime la variable `result`

Requisitos:
- Usar slicing de strings
- Usar return
- Usar un DocString para documentar la función
"""

# Tu programa empieza aquí:
def ex_start(word_str):
    return word_str[:3]  # use slicing

result = ex_start("developer")  
print(result)