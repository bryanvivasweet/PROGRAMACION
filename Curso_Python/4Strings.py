#STRINGS

my_first_string = "Mi primer string con comillas dobles"
my_second_string = 'Mi segundo string con comillas simples'

print('1. ',my_first_string)
print('Esto es 1 string ' + my_first_string + 'Esto es 2 string ' + my_second_string) #Contraintituivo y pesado

print(f'Esto es un texto de una variable {my_first_string} asdasd') #Esto es para evitar colocar repetidamente '',+. con ayuda de la "f"

other_string = 'Hola'
a,b,c,d = other_string

print(b) #Imprime la letra asignada a la b que es la "o"

print(f'Eso es un {a}{b}{c}{d} y nada mas')

#1 FUNCIONES para Strings

print(my_first_string.upper()) #Pones las letras en MAYUSCULAS
print(my_first_string.capitalize()) #Pone la PRIMERA LETRA en mayúsculas
print(my_first_string.lower()) #Pone todo en MINISCULA
print(len(my_first_string)) #CUENTA las letras o caracteres de la variable del string
print(my_first_string.find('r')) #ENCUENTRA la letra contando las posiciones desde el principio hasta encontrarla
print(my_first_string.count('m')) #CONTAR la cantidad de veces de la variable
print(my_first_string.upper().count('r')) #Utilizo varias funciones en una