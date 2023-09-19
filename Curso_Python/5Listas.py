#LISTAS

my_list = ['Python',53,False,43,'Hola mundo'] #La lista solo puede tener valores verificables, no cualquier valor
#print(type(my_list))

print(my_list)
print(my_list[1]) #Imprime el 53, en programación se cuenta desde el 0
print(my_list[-1]) #con negativos buscamos desde la derecha hacia la izquierda pero aqui funciona desde -1,-2,-3,etc

my_list.append(40) #append funcion de agregar
print(my_list)

my_list.insert(3,'Hello') #append funcion de agregar en el lugar (3) designado
print(my_list)

my_list.remove('Hola mundo') #Remover
print(my_list)

my_list.pop(1) #Remueve la posición (1)
print(my_list)

print(my_list.pop(1)) #Nos devuelve lo que borró

print(my_list.count(53)) #Nos cuenta lo que hay en la lista según lo que busquemos

my_list.reverse() #Da vuelta a la lista
print(my_list)

