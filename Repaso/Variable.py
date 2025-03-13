#Variables.

#Variable String
my_String_Variable = "My variable String"
print(my_String_Variable)

#Variable Int
my_Int_variable = 5
print(my_Int_variable)
print(type(my_Int_variable))

#Para transformar un entero en una cadena de texto podemos usar la función str()
my_Int_To_String_variable = str(my_Int_variable)
print(my_Int_To_String_variable)
print(type(my_Int_To_String_variable))
#Variable Boolean
my_Boolean_variable = True

#Usando varios argumentos en el print podemos imprimir todas estas variables en una sola línea.
#A esto se le llama concatenación de cadenas.
print(my_String_Variable,",",my_Int_variable,",", my_Int_To_String_variable, ",",my_Boolean_variable)

#Puedes declarar varias variables en una misma linea.
name, surname, age, alias = "Mateo", "Castro", 18, "Nero"
print(name,surname,age,alias)



#Algunas funciones del sistema.
#len()
print(len(my_String_Variable))#Len nos mostrará la longitud de caracteres del dato.
#my_String_Variable tiene una longitud de 18 caracteres

#Len también puede darnos la longitud de variables concatenadas
print("Esta es la longitud del texto:", len(my_String_Variable))

#Otra función es el input(), que nos permite escribir nosotros el valor de las variables, por ejemplo;
first_name = input("Cual es tu nombre: ")
age = input("Cuantos años tienes: ")
#Después de definir las variables las imprimimos.
print("Tu nombre es: ", first_name)
print("Tienes:", age, "años")