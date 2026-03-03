    ### EXCEPCIONES ### 
# es una forma de manejar los errores de nuestro programa para que tome cierta condicion si pasa algo malo
# se usa la palabra reservada try que encierra el codigo peligroso
# el except si ocurre cualquier error, se ejecuta es bloque de codigo

numero_uno = 5
numero_dos = 4

try:
    print(numero_uno + numero_dos) # si hay un error no lo ejecuta 
    print("el codigo se ejecuto sin error")
except:
    print("se ha ejecutado un error en la suma")

# si creamos un error
numero_dos = "4"
try:
    print(numero_uno + numero_dos) # aqui hay un error y el codigo no se va a ejecutar
    print("el codigo se ejecuta sin problemas")
except:
    print("hay un problema con el codigo de la suma!!!!!") # este si se ejecuta


# agregando el else y el finally

try:
    print(numero_uno + numero_dos)
    print("no se producio ningun error")
except:
    print("se producio un error en el codigo!!!")
else:
    print("la ejecucion continua correctamente") # solo si no hay ningun error 
finally:
    print("la ejecucion continua") # siempre se ejecuta, alla o no errores


# captura de excepciones especificas, podemos capturar errores especificos 
try:
    print(numero_uno + numero_dos)
except TypeError:
    print("el tipo de error es un typeError")
except ValueError:
    print("el tipo de error es un ValueError")

"""
lista de errores comunes: 
TypeError	       -    Operación entre tipos incompatibles
ValueError	       -    Función recibe argumento de tipo correcto pero valor inapropiado
ZeroDivisionError  -    División por cero
IndexError	       -    Índice de lista fuera de rango
KeyError	       -    Clave de diccionario no existe
FileNotFoundError  -    Archivo no encontrado
ImportError        -    Error al importar módulo
"""


# capturar la informacion de un error

try:
    print(10 / 0)
except ZeroDivisionError as error:
    print(error)
except Exception as error:
    print(error)