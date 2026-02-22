### SETS ###
my_set = set()
mi_otro_set = {}

print(type(my_set))
print(type(mi_otro_set)) #inicialmente dice que es diccionario


mi_otro_set = {"choso", "gonlez", 20}
print(type(mi_otro_set)) #ahora cambia a set

print(len(mi_otro_set))


mi_otro_set.add("sthefanny")

print(mi_otro_set) # un set o es una estructura ordenada


mi_otro_set.add("choso") # un set no admite repetidos 
print(mi_otro_set)

# para comprobar asi un elemento existe en un set 
print("choso" in mi_otro_set)
print("chosi" in mi_otro_set)


mi_otro_set.remove("gonlez")
print(mi_otro_set)


mi_otro_set.clear()
print(mi_otro_set)
print(len(mi_otro_set))






# ventajas del set?