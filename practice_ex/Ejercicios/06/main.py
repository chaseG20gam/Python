"""
Ejercicio 06: Verificando la integridad de un mensaje con funciones hash

Objetivo: Usar funciones hash para verificar que un mensaje no ha sido alterado durante su transmisión

Instrucciones:
1. Crea una función llamada `calc_hash` que reciba un string `mensaje` y devuelva su hash SHA256 como string hexadecimal
2. Crea una función llamada `v_message` que reciba:
   - `mensaje_original`: string original
   - `hash_recibido`: string hash que acompaña al mensaje
   - La función debe calcular el hash del mensaje y compararlo con `hash_recibido`
   - Si coinciden, devuelve `True`. Si no, devuelve `False`
3. Guarda el resultado de `verificar_mensaje("Hola mundo", "<hash_correcto>")` en una variable llamada `verificacion`
4. Imprime el contenido de `verificacion`

Requisitos:
- Utiliza `hashlib` y SHA256
- Documenta tus funciones con DocStrings
"""

# Tu programa empieza aquí:
import hashlib

def calc_hash(mensaje):
      
      hash_object = hashlib.sha256(mensaje.encode())
      return hash_object.hexdigest()

def v_message(mensaje_original, hash_recibido):
      hash_calculado = calc_hash(mensaje_original)
      return hash_calculado == hash_recibido

verificacion = v_message("Hola mundo", " ")
print(verificacion)