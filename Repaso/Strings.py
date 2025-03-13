#Cadenas de texto#

"""

Las cadenas de texto o "Strings" pueden escribirse de varias maneras:
O con comillas simples
O con comillas dobles

"""
print('Hola soy phyton')
print("Hola soy phyton")

#Puedes poner comillas dobles dentro de comillas simples
print('Los "strings" son mi pasión')

#Si quieres poner comillas simples dentro de comillas simples lo haces así:
print('Los \'strings\' son secuencias de caracteres')

#Esto es un conjunto vacio
print("")

#Puedes transformar tipos booleanos, enteros o flotantes a un string con str()
print(str(True))
print(str(5))
print(str(21.7))
print("")

#Secuencias de escape
#Salto de línea
msg = "Mi primer mensaje es:\nOs quiero mucho"
print(msg)
#Tabulador
msg = "Valor =\t40"
print(msg)
#Comillas simples
msg = "Necesitamos\'escapar\' las comillas simples"
print(msg)
#Barra invertida
msg = "Queremos \\ separar \\ el texto"
print(msg)
print("")
#Si quieres escribir literalmente el \n el \t o los \\ usas el raw anteponiendo una r a la cadena de texto
text = r'abc\ndef'
print(text)
text = r'a\tb\tc'
print(text)
text = r'Encabezado\\Main\\Footer'
print(text)
print("")

#Por ahora usamos print de manera sencilla pero admite más funciones

#Puedes imprimir dos variables separadas por un separador definido por ejemplo:
text = "El lado luminoso fuerte en mi es"
msg = "El lado oscuro fuerte en ti es"
print(text, msg, sep="||")
#Puedes imprimir variables terminadas en lo que quieras.
print(text, end="!!")
print("")
#Obtener un caracter:
#Los strings están indexados y los caracteres tienen su propia posición, para saberla debemos indicar su índice entre corchetes.
sentence = "Hola, Mundo"
print(sentence[-1])
print(sentence[1])
print(sentence[2])
print(sentence[3])
print(sentence[4])
print(sentence[5])
print(sentence[6])
print(sentence[7])
print(sentence[8])
print(sentence[9])
print(sentence[10])
print("")
# Formateo #

#En phyton podemos formatear strings de muchas maneras. Para formatear podemos usar el operador %.
#Este operador es usado para formatear una serie de variables de una tupla, juntos como strings.
#Existen símbolos especiales como: %s,%d,%f.
# %s: for Strings.
# %d: Para enteros.
# %f: Para floats.


name, surname, age = "Mateo", "Castro", 18
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

