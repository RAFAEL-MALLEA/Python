### Literales

print("2")
print(2)

# el resultado es el mismo, pero el primero es un string y el segundo un entero.

# encuentras dos tipos diferentes de literales:

# Una cadena, la cual ya conoces,
# Y un número entero, algo completamente nuevo.

print(0o123) #el resultado es 83
# el resultado es 83, ya que es un numero octal, y el 0o indica que es un numero en base 8.

print(0x123) #el resultado es 291
# el resultado es 291, ya que es un numero hexadecimal, y el 0x indica que es un numero en base 16.


###CADENAS

print('Me gusta \"Monty Python\"')

# el resultado es Me gusta "Monty Python", ya que las comillas dobles dentro de la cadena son escapadas con el caracter de escape \, lo que permite que se muestren en la salida sin causar un error de sintaxis.
# el resultado es el mismo si se usan comillas simples, pero es mas comun usar comillas dobles para cadenas que contienen comillas simples.


# ¿Cómo se puede insertar un apóstrofe en una cadena la cual está limitada por dos apóstrofes?

# A estas alturas ya se debería tener una posible respuesta o dos.

# Intenta imprimir una cadena que contenga el siguiente mensaje:
print('I\'m Monty Python.')

#SOLUCIONES 1 Y 2
print('I\'m Monty Python.')
print("I'm Monty Python.")


###VALORES BOOLEANOS
print(True > False)
print(True < False)

# True
# False


###LAB DE SECCION

#ejercicio 1

# Escriba un fragmento de código de una línea, utilizando la función print(), 
# así como los caracteres de nuevalínea y de escape, 
# para que coincida con el resultado esperado que se muestra en la salida.

# "Estoy"
# ""aprendiendo""
# """Python"""

print('"estoy"\n ""aprendiendo""\n """python"""')

#resultado

# "estoy"
#  ""aprendiendo""
#  """python"""

# solucion dada por maquina
print("\"I'm\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")


#ejercicio 2