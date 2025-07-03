
"""
- Ejercicio 02: Analizador de palabras

Objetivo: Practicar funciones personalizadas, uso de strings, `len()` y `return`

Instrucciones:
1. Crea una función llamada `analyze_word` que reciba un string llamado `word_case`
2. La función debe devolver un string que diga:
   "La palabra <word_case> tiene <n> letras."
   Donde `<n>` es la cantidad de letras de la palabra (usa `len()`)
3. Guarda el resultado de llamar a la función con `"murcielago"` en una variable llamada `result`
4. Imprime el contenido de `result`

Requisitos:
- Usar una función con `return`
- Utilizar `len()` correctamente
- Documentar la función con un DocStrings
"""

# Tu programa empieza aquí:
def analyze_word(word_case):
   n = len(word_case)
   return f"La palabra {word_case} tiene {n} letras."

result = analyze_word("murcielago") 
print(result)  # print result