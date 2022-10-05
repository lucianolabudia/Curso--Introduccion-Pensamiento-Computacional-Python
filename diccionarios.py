"""
CLASE: DICCIONARIOS 
"""
# IMPORTANTE: Para definir los diccionarios usaremos {}

my_dict = {
    'David' : 35,
    'Erika' : 32,
    'Jaime' : 50,
}

#acceder a un valor 
print(my_dict['David'])

#Cuando queremos acceder al diccionario y no sabemos que una llave existe, y si no existe queremos evitar un error podemos hacer que nos regrese un valor mediante el metodo get 

print(my_dict.get('Piero', 21))
#Regresa el valor 21 ya que Piero no existe


"""
Reasignar un valor 
"""

my_dict['Jaime'] = 20
print(my_dict['Jaime'])
#Ahora Jaime es más joven

"""¿Como asignar un nuevo valor al dic?"""

my_dict['Pedro'] = 70
print(my_dict)

""" Borrar """
del my_dict['Jaime']
print(my_dict)
#Bye Jaime

"""¿Como iterar a lo largo de este dic?"""

#Podemos iterar a lo largo de las llaves, los valores o en ambos. 

#Iteracion por llave

for llave in my_dict.keys (): #el metodo keys nos permite imprimir las llaves, keys = llaves
    print(llave)


#Iteracion por valor

for valor in my_dict.values (): #el metodo values nos permite imprimir los valores, values = valores
    print(valor)


#Iteracion por llave y valor 

for llave, valor in my_dict.items():
    print('Para la llave ' + llave + ' el valor es ' + str(valor))



"""¿Como saber si existe una llave en el dic?"""

print('David' in my_dict)
print('Tom' in my_dict)