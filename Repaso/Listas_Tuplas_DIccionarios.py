
#Listas, tuplas y diccionarios.

#1.listas
calificaciones = [10, 9, 8, 7.5, 6]
nombres = ["María", "Paco", "Manuel", "Pablo", "Tania"]
#Las listas nos permiten mezclar tipos de datos y hasta otras listas dentro de ellas.
mezcla = [True, "abc", 10.5, [4,5,6]]

print(calificaciones)
print(nombres)
print(mezcla)
print("")

#Las listas son itinerables por lo que cada posicion tiene un índice del 0 a 4, siendo ejemplo la lista nombres.
print(nombres[2])
print(nombres[4])
print("")

#Las listas se pueden modificar al eliminar o añadir datos esto se hace con remove o append.

#Append añade valores a la lista:
nombres.append("Chencho")
nombres.append("Conchi")
print(nombres)
print("")
#Remove elimina valores de la lista.
nombres.remove("Manuel")#Si al usar el remove el valor no existe Python devolverá un ValueError.
print(nombres)
print("")

#2. Tuplas:
#Las tuplas son iguales a las listas, pero más restrictivas, ya que no nos permiten modificarlas.

#Para crearla es igual que las listas, pero en vez de corchetes usamos paréntesis.
colores = ("Azul", "Rojo", "Amarillo", "Rosa", "Magenta",)
#Las tuplas también son itinerables, entonces también podemos mostrar datos en base, a sus índices.
print(colores)
print(colores[-4])
print(colores[4])
print("")
#Las tuplas no se pueden modificar, entonces el remove y el append no se usan.

#3.Diccionarios

#Los diccionarios son estructuras que nos permiten darle valores a unas claves predefinidas con el formato clave:valor.
edades = {"Ale": 9,"Mateo": 18, "Mercedes": 25}
#Los diccionarios van entre llaves, las claves deben ser únicas y los valores de cualquier tipo.
print(edades["Ale"])
print("La edad de Ale en un año será: " + str((edades["Ale"]+1)))
print("Las edades de Ale y Mateo sumadas son: " + str((edades["Ale"] + edades["Mateo"])))