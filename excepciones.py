"""Manejo de EXCEPCIONES

- Las excepciones se manejan con los keywords: try, except, finally
- Se pueden utilizar tambien para ramificar programas.
- No deben manejarse de manera silenciosa (ej, con print statements)
- Para aventar tu propia excepcion utiliza el keyword raise
"""

# Creamos una función en donde cada elemento de  una lista es dividida por un divisor definido
def divide_elementos_de_lista(lista, divisor):
    # El programa intentara realizar la división
    try:
        return [i / divisor for i in lista]
    # En caso de error de tipo ZeroDivisionError que significa error al dividir en cero, el programa
    # ejecutara la siguiente instrucción
    except ZeroDivisionError as e:
        return lista


lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))