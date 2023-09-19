# DICCIONARIOS

my_dict = {'a','b'}
print('Esta es un set: ',type(my_dict)) #Por la sintaxis me muestra que es un set

my_dict = {'Nombres':'Bryan',
           'Apellido':'Vivanco',
           'Apodo':'Vivi',
           True:'Hola',
           5:False}
print('Este es un diccionario: ',type(my_dict)) #Imprime como diccionario por la sintaxis
print(my_dict)

print(my_dict['Apodo']) #Con dict se busca por LLAVES, puede ser entero, string o booleano
print(my_dict['Nombres'])

#print(my_dict[1]) Busca por posici+on pero no funciona
#Usando diccionarios, cuando queremos buscas nos aparece automáticamente lo que se encuentra en él

print(my_dict['Apellido']) 
print(my_dict[True])
print(my_dict[5])

#Funciones

print('Todas las llaves son: ',my_dict.keys())
print('Todos los valores son: ',my_dict.values())

my_dict = list(my_dict) #Convertimos a lista
print(type(my_dict),my_dict) #Imprime solo las llaves

my_dict = set(my_dict) #Convertimos a sets
print(type(my_dict),my_dict) #Imprime en orden aleatorio las llaves

my_dict = tuple(my_dict) #Convertimos a tupla
print(type(my_dict),my_dict) #Imprime solo las llaves








