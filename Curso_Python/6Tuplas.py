#TUPÑAS

my_tupla = (53,True,'Perro',7.4,True) #La diferencia es que aquí se usan los paréntesis y no los corchetes

print(type(my_tupla))

print('La posición 1 es: ',my_tupla[1]) #Imprime la posición 1
print('El # de 53 que hay en la tupla es: ',my_tupla.count(53)) #Cuenta cuántos 53 hay
print('El booleano True se encuentra en la posición: ',my_tupla.index(True)) #Encuentra lo que nosotros querramos y nos indica la posición
print('Mi Tupla es: ',my_tupla)

#Las Tuplas NO se pueden MODIFICAR

my_tupla = list(my_tupla) #Tipeado Fácil, se puede cambiar la variable
print('Ahora la clase es: ',type(my_tupla))

my_tupla.pop() #Ahora se usan las funciones de lista
print(my_tupla)

my_tupla = tuple(my_tupla) #Volvió a ser Tupla
print('Ahora la clase es: ',type(my_tupla))

