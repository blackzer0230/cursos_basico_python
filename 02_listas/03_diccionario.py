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

# tambien se puede escribir en varias lineas para mayor legibilidad
otro_dict = {

    "nombre": "harry",
    "apellido": "gonzalez",
    "edad": 20,
    "lenguajes": ("python", "go", "c++")
}

print(mi_dict)
print(otro_dict)


# acceder a los valores
print(otro_dict["nombre"])
# si la clave no existe puede dar un error, para evitar eso podemos usar el metodo .get()
print(otro_dict.get("email")) # Si la clave no existe, devuelve None por defecto


# modificar valores existentes
otro_dict["nombre"] = "choso"
print(otro_dict["nombre"])


# agregar nuevos pares CLAVE:VALOR
otro_dict["email"] = "prontonmail"
print(otro_dict)


# comprovar si existe
print("gonzalez" in otro_dict) # gonzalez es un valor no una clave
print("apellido" in otro_dict)

# eliminar elementos
del mi_dict["apellido"]
print(mi_dict)

valor_eliminado = otro_dict.pop("edad")
print(valor_eliminado)

mi_dict.clear()
print(mi_dict)


# metodos principales mas usados
print(otro_dict.items()) # devuelve un vista de pares

print(otro_dict.keys()) # devuelve una vista de las claves

print(otro_dict.values()) # devuelve una vista de los valores

# un metodo que es un poco raro pero la ia me lo explico muy bien
# el fromkeys es un metodo para crear un nuevo diccionario a partir de una secuencia de claves y una valor por defecto(opcional)
nuevo_dict = dict.fromkeys(["nombre", "edad", "ciudad"])
print(nuevo_dict) # se crear las claves con valores none por defecto
nuevo_dict = dict.fromkeys(["nombre", "edad"], "desconocido")
print(nuevo_dict) # crea las claves con le valor predeterminado "desconocido"


# metodos un poco utiles
otro_dict.update({"pais": "México", "edad": 21})   # edad se actualiza, pais se agrega
print(otro_dict)
valor = otro_dict.setdefault("telefono", "000-0000")  # como no existe, lo crea
print(otro_dict)   # ahora incluye 'telefono': '000-0000'


# diccionario anidados 
usuarios = {
    "user1": {"nombre": "harry", "edad": 20},
    "user2": {"nombre": "sthefanny", "edad": 19}
}
print(usuarios["user1"]["nombre"])
print(usuarios["user2"]["edad"])



# algo que estaba inventando
print(f"en la base de datos tenemos al usuario {usuarios['user1']["nombre"]} y al usuario {usuarios['user2']["nombre"]}")