    ### IF, ELIF, ELSE ###
# las condicionales permiten ejecutar bloques de codigo solo si se cumple una condicion

condicionverdadera = True
condicionfalsa = False

if condicionverdadera:
    print("la condicion es verdadera entonces este bloque se ejecuta")

if condicionfalsa:
    print("la condicion es falsa y no se ejecuta")



# agregando el else
edad = 17

if edad >= 18:
    print("eres mayor de edad")
else: # solo se ejecuta cuando todas las demas no se cumplen
    print("eres menor de edad")


# multiples condiciones con elif
nota = 85
if nota >= 90:
    print("Sobresaliente")
elif nota >= 70: # se evaluna en orden, cuando la primer condicion es verdadeera se ejecuta el bloque
    print("Notable")
elif nota >= 50:
    print("Aprobado")
else:
    print("suspenso")

# con operadores logicos 
edad = 18 
tiene_dinero = True

     # forma anidada
if edad >= 18:
    if tiene_dinero:
        print("puedes ir al cine :)")
    else:
        print("no tienes dinero para el cine, vago!")
else:
    print("eres menor para entrar al cine solo")

    # con operadores logicos 
if edad >= 18 and tiene_dinero:
    print("puedes entrar al cine :)")
elif edad >= 18 and not tiene_dinero:
    print("no tienes dinero, vago!")
else:
    print("eres menor amigos, sal de aca ya!!")


# operador ternario
edad = 17 
mensaje = "mayor de edad" if edad >= 18 else "eres menor de edad carajito de mierda"
print(mensaje)
    # equivalente a 
if edad >= 18:
    mensaje = "Mayor de edad"
else:
    mensaje = "Menor de edad"