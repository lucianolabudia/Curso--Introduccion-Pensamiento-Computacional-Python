# numero al que se le calculara la raiz cuadrada
objetivo = int(input('Escoge un numero: '))

# margen de error para encontrar esa raiz cuadrada
epsilon = 0.01

# valor que se ira sumando secuencialmente hasta encontrar la raiz cuadrada
paso = epsilon**2

# se comenzara a buscar a la raiz cuadrada desde 0.0 en adelante
respuesta = 0.0

# mientras que respuesta al cuadrado no sea igual al objetivo (con un margen de error de 0.01, es decir
# epsilon), este while no seguira ejecutando.
#respuesta <= objetivo: codigo defensivo; si respuesta es mayor a objetivo, el while seguira infinitamente,
# y nunca encontrara la raiz cuadrada (la raiz cuadrada nunca seria mas grande que el objetivo)
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada de {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')