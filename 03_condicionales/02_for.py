    ### FOR ###
# es una estructura de control que repite codigo varias veces recorriendo una coleccion de elementos

frutas = ["manzanas", "peras", "uva"]

for fruta in frutas: # recorre imprimiendo la cantidad de elementos que alla
    print(fruta)

# en una string
palabra = "hola"

for letras in palabra:
    print(letras)


# probando en un diccionario
usuario = {
    "nombre": "sthefanny", 
    "apellido": "negodov", 
    "edad": 19
    }

for clave in usuario:
    print(clave)

# mostrar valor 
for valor in usuario.values():
    print(valor)

# que muestre clave y valor 
for clave, valor in usuario.items():
    print(clave, "->", valor)

# repetir un numero fijo de veces
for i in range(5):
    print(i)

# se puede usar el break y el continue en los for 
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)