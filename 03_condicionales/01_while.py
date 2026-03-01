    ### WHILE ###
# se ejecuta ese bloque de codigo mientras una condicion sea verdadera
# while condicion:
#   codigo a repetir
# else:
#   opcional solo se ejecuta si se vuelve falsas con while


mi_condicion = 0 

while mi_condicion < 10:
    print(mi_condicion)
    mi_condicion += 2
else: # solo se ejecuta si la condion se vuelve falsa de forma natural
    print("mi condicion es igual o mayor a 10")



# BREAK para salir anticipadamente
mi_condicion = 0

while mi_condicion < 20:
    mi_condicion += 2
    if mi_condicion == 16:
        print("se detiene porque quiero hasta el 16")
        break
    print(f"mi condicion es menor o igual que 20 {mi_condicion}")



# CONTINUE  para saltar una iteracion
contador = 0

while contador < 5:
    contador += 1
    if contador == 3:
        continue # salta esa ejecucion para la siguiente si se cumple esa condicion
    print(contador)
