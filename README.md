# Cifrado de Hill

# Descripción

El cifrado Hill fue propuesto por Lester S. Hill en 1929 y es un criptosistema que se basa en emplear una matriz como clave para cifrar un texto en claro y su inversa para descifrar el criptograma correspondiente.

# Requisitos

* [Python3](https://www.python.org/downloads/).
* Librerias : ```python -m pip install -r requirements.txt```

#

# Funcionamiento

Consultar Wikipedia [Cifrado de Hill](https://es.wikipedia.org/wiki/Cifrado_Hill)

Se ha usado un alfabeto de 41 caracteres, 26 letras del abecedario en inglés, 10 dígitos numéricos, del 0 al 9, así como los 4 caracteres siguientes: "\.", "\,", "\:", "\?" y el espacio en blanco, en ese orden.

Cada letra está representada por un número (diccionario).

## Funciones:

### Generar la clave

Se generará una matriz cuadrada (n x n) con valores aleatorios.

#

### Encriptación

Cada bloque de n letras (considerados como un vector) es convertido en un vector de números (su representación correspondiente en el diccionario), este  se multiplica por una matriz invertible n×n (key) a la que su producto se le aplica el módulo 41 y posteriormente se le aplica el diccionario inverso, devolviendo así una cadena de texto con el mensaje cifrado por esa clave.

Hay que considerar que en caso de que el texto a cifrar sea menor que el tamaño de la clave, realizaremos padding con el carácter 'X'. En el caso de que el texto a cifrar sea más grande que el tamaño de la clave, dividiremos el texto en bloques del tamaño de la clave y los cifraremos uno por uno y unificandolo en una sola variable.

Ejemplo :

```
key: [[33, 1, 7], [40, 32, 24], [12, 22, 19]]
message: SECRET TEXT
retorna: :9OB8:OI5,4Y
```
#

### Desencriptación

Cada bloque es convertido un vector de letras con el diccionario y este es multiplicado por el inverso de la matriz usada para la encriptación y posteriormente a cada término se le aplica el modulo 41 y finalmente se desencripta empleando el diccionario inverso.

Hay que considerar que se deben eliminar las 'X' empleadas en la encriptación.

```
key: [[33, 1, 7], [40, 32, 24], [12, 22, 19]]
ciphertext: :9OB8:OI5,4Y
retorna: SECRET TEXT
```

# Entorno de Pruebas

Se proporciona el archivo ```Test_Hill.py```, el cual contiene varios test de las diversas funciones.
