        ### DICCIONARIOS ###
# Un diccionario es una estructura de datos que almacena pares CLAVE:VALOR
# las claves deben ser unicas e inmutables(string, numeros, tuplas)
# los valores pueden ser cualquier tipo de dato(listas, otros diccionarios, etc)

# Dos formas de crear un diccionario vacio
mi_dict = dict()
otro_dict = {}

print(type(mi_dict))
print(type(otro_dict))

# diccionario con elementos
mi_dict = {"nombre": "harry", "apellido": "gonzalez", "edad": 20, "lenguaje": "python"}

# tambien se ouede escribir en varias lineas para mayor legibilidad
otro_dict = {

    "nombre": "harry",
    "apellido": "gonzalez",
    "edad": 20,
    "lenguajes": ("python", "go", "c++")
}

print(mi_dict)
print(otro_dict)
