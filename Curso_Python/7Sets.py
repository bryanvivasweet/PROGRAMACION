# SETS

my_set = {}
print(type(my_set))

my_set = {'Python','JavaScript','C++'} #El set es set cuando definimos la variable
print(type(my_set))

print('My set es: ',my_set) #Nos imprime los valores dentro del set {}, de manera aleatoria.

# print(my_set[1]) Esto es un error

my_set.add('C++') #No agrega nada porque ya existe
my_set.add('C#') #Si agrega porque inicialmente no existe
print('Mi nuevo set es: ',my_set)

my_set_0 = {'Python','JavaScript','C++'}

my_set.difference_update(my_set_0)
print('La diferencia entre my_set y my_set_0 es: ',my_set)

