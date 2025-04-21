### la funcion print y sus argumentos

### ejercicio 1
print("Programming","Essentials","in", sep="***", end="...")
print("Python")

#la salida por pantalla es :# Programming***Essentials***in...Python

### ejercicio 2
### dando formato a la salida

# minimizar el número de invocaciones de la función print() insertando \n en las cadenas;
# hacer que la flecha sea el doble de grande (pero mantener las proporciones)
# duplica la flecha, colocando ambas flechas una al lado de la otra; nota: una cadena se puede multiplicar usando el siguiente truco: "string" * 2 producirá "stringstring" (pronto contaremos más al respecto)
# elimina cualquiera de las comillas y observe detenidamente la respuesta de Python; presta atención a dónde Python ve un error - ¿es este el lugar donde realmente existe el error?
# haz lo mismo con algunos de los paréntesis;
# cambia cualquiera de las palabras print por otra cosa, que difiera solo en mayúsculas y minúsculas (por ejemplo, Print) - qué sucede ahora?
# reemplaza algunas de las comillas con apóstrofes; observa lo que sucede con cuidado.

print("original:")
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")


### resultados
print("Pequena con pocos prints:")
print("    *\n","  * *\n", " *   *\n","*     *\n",end="")
print("***   "*2,"\n  *   *"*2,"\n ","*"*5)

print("Grande y con pocos prints:")
print("           *\n","         * *\n","        *   *\n","       *     *\n","      *       *\n","     *         *\n", "    *           *\n","   *             *\n",end="")
print("   ******  "*2,"\n        *     *"*6,"\n       ","*"*7)

#falto la flecha doble por completar
#python muestra el error en el final de la linea de codigo, no exactamente donde se encuentra el error, sino donde se da cuenta de que no puede continuar.
#lo mismo pasa con los parentesis
#cambiando la palabra print el error es que no encuentra la funcion, dice que no esta definida y pregunta si acaso se refiere a la funcion print.
#al intercambiar una de las comillas por un apostrofe, el error que nos da es de sintaxis, ya que no encuentra el cierre de la cadena.
#el apostrofe debe ir desde inicio a final, si no, no se puede cerrar la cadena.


#cuestionario

#1

print("Mi\nnombre\nes\nBond.", end=" ")
print("James Bond.")

# Mi
# nombre
# es
# Bond. James Bond.

#2

print(sep="&", "fish", "chips")

# Recuerda: Los argumentos de palabras clave deben pasarse después de cualquier argumento posicional requerido.

#3

print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")
print('"Greg's book."')
      
# La línea 5 generará un SyntaxError, porque el símbolo ' en la cadena Greg's book. requiere un carácter de escape.