#1. OPERADORES ARITMENTICOS

a = 7

print('La suma es:',6+5)
print('La resta es:',6-5)
print('La multiplicación es:',6*5)
print('La división es:',6/5) 

print('El excedente es:',a%3) # el %: suma el '% número' entre sí tantas veces  hasta llegar a 'número %' y mostrar o imprimir el sobrante

print('La potencia es:',a ** 3) #Exponencia

print('La división float es:',a//3) #División solo entera flor

#1.1. OPERADORES ARITMÉTICOS CON STRINGS

print('String + string: ','hola ' + 'mundo')
print('string * entero: ','hola ' * 6)
print('String + str(numero): ','hola ' + str(6)) #str sirve para decirle a python que 6 será un string

#2. OPERADORES COMPARTIVOS
#Aqui se utiliza la lógica compartiva o Booleanos (0 o 1) (Falso o Verdadero)

print('4<8: ',4<8)
print('4>8: ',4>8)
print('4=8: ',4==8) #Con "==" preguntamos si son iguales. Solo con "=" estamos igualando
print('4<=8: ',4<=8) #Menor o igual
print('4>=8: ',4>=8) #Mayor o igual
print('4 diferente de 8: ',4!=8) #Diferente de (!=)

#2.2. OPERADORES COMPARATIOS CON STRINGS

print('Hola < mundo: ','HolA' < 'mundo') 
print('hola < Bolas: ','hola' < 'Bolas')
print('a<b: ','a'<'b') #Compara el orden de las letras del abecedario

#3. OPERADORES LÓGICOS

print('True and False: ', 4 < 6 and 7 > 9) #And
print('True or False: ', 4 < 6 or 7 > 9) #Or
print('not(4<6): ',not(4<6))

print('True and (True or False): ',True and (True or False)) #Puedo meter operadores logicos dentro de otros

#4. Tarea

print('(not(7!=7) and 6>5) and (rozar<rotar or not(3==5)): ',(not(7!=7) and 6>5) and ('rozar'<'rotar' or not(3==5)))