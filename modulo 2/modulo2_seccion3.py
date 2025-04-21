print(2+2)
#el resuiltado es 4, ya que es una suma de dos numeros enteros.

#EXPONENCIACION
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

#MULTIPLICACION
#Un símbolo de * (asterisco) es un operador de multiplicación.
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

#DIVISION
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

#El valor después de la diagonal es el dividendo, el valor antes de la diagonal es el divisor.

#DIVISION ENTERA
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

#el resultado es 1 y 1.0

print(6 // 4)
print(6. // 4)

# el resultado es -2 y -2.0

#RESIDUO(MODULO)
print(14 % 4)
#EL RESULTADO ES 2
# Como puedes observar, el resultado es dos. Esta es la razón:

# 14 // 4 da como resultado un 3 → esta es la parte entera, es decir el cociente;
# 3 * 4 da como resultado 12 → como resultado de la multiplicación entre el cociente y el divisor;
# 14 - 12 da como resultado 2 → este es el residuo.

print(12 % 4.5)

# 3.0 – no 3 pero 3.0. La regla aun funciona:

# 12 // 4.5 da 2.0,
# 2.0 * 4.5 da 9.0,
# 12 - 9.0 da 3.0.

#SUMA
print(-4 + 4)
print(-4. + 8)
#EL RESULTADO ES 0 Y 4.0


#OPERADOR DE RESTA, BINARIO Y UNARIOS


print(-4 - 4)
print(4. - 8)
print(-1.1)


#### el resultado es -8 y -4.0 y -1.1

print(+2)
# Por cierto: también hay un operador + unario

# OPERADORES Y SUS ENLACES
print(9 % 6 % 2)

# Existen dos posibles maneras de evaluar la expresión:

# De izquierda a derecha: primero 9 % 6 da como resultado 3, y entonces 3 % 2 da como resultado 1;
# De derecha a izquierda: primero 6 % 2 da como resultado 0, y entonces 9 % 0 causa un error fatal.

# El resultado debe ser 1. El operador tiene un enlazado del lado izquierdo. Pero hay una excepción interesante.

# Repite el experimento, pero ahora con exponentes.

print(2 ** 2 ** 3)

# Los dos posibles resultados son:

# 2 ** 2 → 4; 4 ** 3 → 64
# 2 ** 3 → 8; 2 ** 8 → 256

print(-3 ** 2)
print(-2 ** 3)
print(-(3 ** 2))

#LISTA DE PRIORIDADES
print(2 * 3 % 5)


#OPERADORES Y PARENTESIS
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
    
# CUESTIONARIO

1.-print((2 ** 4), (2 * 4.), (2 * 4))

2.-print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))

3.-print((2 % -4), (2 % 4), (2 ** 3 ** 2))
