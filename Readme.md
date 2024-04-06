
README
Descripción

Este script de Python define una función is_palindrome(mistring) que determina si una cadena de texto dada es un palíndromo o no. Un palíndromo es una palabra, frase o secuencia que se lee igual de izquierda a derecha que de derecha a izquierda, ignorando los espacios en blanco.
Cómo Funciona

La función is_palindrome(mistring) recibe como argumento una cadena de texto (mistring). Retorna True si la cadena es un palíndromo y False en caso contrario.

El algoritmo funciona de la siguiente manera:

    Se elimina cualquier espacio en blanco de la cadena de texto utilizando el método replace(" ", "").
    Se itera sobre la mitad de la longitud de la cadena utilizando un bucle for y un rango basado en len(mistring) // 2.
        En cada iteración, se compara el carácter en la posición indice con el carácter correspondiente en la posición simétrica (-(indice + 1) desde el final de la cadena).
        Si estos caracteres son diferentes, la función retorna False, indicando que la cadena no es un palíndromo.
    Si el bucle termina sin retornar False, significa que todos los caracteres coinciden en sus posiciones simétricas, por lo que la cadena es un palíndromo y la función retorna True.

Uso

Aquí hay un ejemplo de cómo usar la función is_palindrome:

python

texto = "anita lava la tina"
if is_palindrome(texto):
    print(f'"{texto}" es un palíndromo.')
else:
    print(f'"{texto}" no es un palíndromo.')

Este código verificará si la cadena "anita lava la tina" es un palíndromo y, como resultado, imprimirá que es un palíndromo.

Requisitos

    Python 3.x
