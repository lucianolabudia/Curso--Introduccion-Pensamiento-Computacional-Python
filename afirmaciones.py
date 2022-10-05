""" AFIRMACIONES

Es un mecanismo por el cuál podemos determinar si una función se cumple o no se cumple. Y poder 
seguir adelante con la ejecución de nuestro programa o terminar dicha ejecución.

Programación defensiva
Pueden utilizarse para verificar que los tipos sean correctos en una función.
También sirven para debuguear.
Para generarlas tenemos que utlizar el keyword assert y dar una expresión boleana y un mensaje de error
"""


def primera_letra(lista_palabras):
    primeras_letras = []
    
    for palabra in lista_palabras:
        try:
            assert type(palabra) == str, f'{palabra} no es String'
            assert len(palabra) > 0 , 'No se permiten vacios'
            primeras_letras.append(palabra[0])
        except AssertionError as e:
            print(e)

    return primeras_letras