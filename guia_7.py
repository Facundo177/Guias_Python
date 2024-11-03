# Ejercicio 1

import random


def pertenece(s:list[int], e:int) -> bool:
    """ 
    problema pertenece (in s: seq⟨Z⟩, in e: Z) : Bool {
        requiere: { True }
        asegura: { (res = true) <-> (existe un i ∈ Z tal que 0 ≤ i < |s| ∧ s[i] = e)}
    }
    Implementar al menos de 3 formas distintas este problema
    """
    
    for i in range(len(s)):
        if s[i] == e:
            return True

    return False


def pertenece2(s:list[int], e:int) -> bool:
    """ 
    Otra implementación diferente
    """
    
    for elem in s:
        if elem == e:
            return True

    return False


def pertenece3(s:list[int], e:int) -> bool:
    """ 
    Otra implementación diferente
    """
    
    if s.count(e) > 0:
        return True

    return False



def divide_a_todos(s:list[int], e:int) -> bool:
    """ 
    problema divide_a_todos (in s:seq⟨Z⟩, in e:Z) : Bool {
        requiere: {e ̸= 0 }
        asegura: { (res = true) <-> (para todo i ∈ Z si 0 ≤ i < |s| → s[i] mod e = 0)}
    }
    """
    
    for elem in s:
        if not (elem % e == 0):
            return False
    
    return True



def suma_total(s:list[int]) -> int:
    """ 
    problema suma_total (in s:seq⟨Z⟩) : Z {
        requiere: { True }
        asegura: { res es la suma de todos los elementos de s }
    }
    Nota: no utilizar la funcion sum() nativa
    """
    total:int = 0
    
    for elem in s:
        total += elem
    
    return total



def maximo(s:list[int]) -> int:
    """ 
    problema maximo (in s:seq⟨Z⟩) : Z {
        requiere: {|s| > 0 }
        asegura: { res = el mayor de todos los numeros que aparece en s }
    }
    """
    mayor:int = s[0]
    
    for elem in s:
        if elem > mayor:
            mayor = elem
    
    return mayor



def minimo(s:list[int]) -> int:
    """ 
    problema minimo (in s:seq⟨Z⟩) : Z {
        requiere: {|s| > 0 }
        asegura: { res = el menor de todos los numeros que aparece en s }
    }
    """
    menor:int = s[0]
    
    for elem in s:
        if elem < menor:
            menor = elem
    
    return menor



def ordenados(s:list[int]) -> bool:
    """ 
    problema ordenados (in s:seq⟨Z⟩) : Bool {
        requiere: { True }
        asegura: { res = true <-> (para todo i ∈ Z si 0 ≤ i < (|s| - 1) → s[i] < s[i + 1] }
    }
    """
    
    for i in range(1, len(s)):
        if not (s[i-1] < s[i]):
            return False
    
    return True



def pos_maximo(s:list[int]) -> int:
    """ 
    problema pos_maximo (in s:seq⟨Z⟩) : Z {
        requiere: { True }
        asegura: { (Si |s| = 0, entonces res = -1; si no, res = al indice de la posicion donde aparece el mayor elemento de s (si hay varios es la primera aparicion)}
    }
    """
    
    if len(s) > 0:
        posicion_del_mayor:int = 0
        
        for i in range(len(s)):
            if s[i] > s[posicion_del_mayor]:
                posicion_del_mayor = i
        
        return posicion_del_mayor
    
    return -1



def pos_maximo(s:list[int]) -> int:
    """ 
    problema pos_maximo (in s:seq⟨Z⟩) : Z {
        requiere: { True }
        asegura: { (Si |s| = 0, entonces res = -1; si no, res = al indice de la posicion donde aparece el mayor elemento de s (si hay varios es la primera aparicion)}
    }
    """
    
    if len(s) > 0:
        posicion_del_mayor:int = 0
        
        for i in range(len(s)):
            if s[i] > s[posicion_del_mayor]:
                posicion_del_mayor = i
        
        return posicion_del_mayor
    
    return -1



def pos_minimo(s:list[int]) -> int:
    """ 
    problema pos_minimo (in s:seq⟨Z⟩) : Z {
        requiere: { True }
        asegura: { (Si |s| = 0, entonces res = -1; si no, res = al indice de la posicion donde aparece el menor elemento de s (si hay varios es la ultima aparicion)}
    }
    """
    
    if len(s) > 0:
        posicion_del_menor:int = 0
        
        for i in range(len(s)):
            if s[i] < s[posicion_del_menor]:
                posicion_del_menor = i
        
        return posicion_del_menor
    
    return -1



def hay_palabra_larga(s:list[str]) -> bool:
    """ 
    Dada una lista de palabras (seq⟨seq⟨Char⟩⟩), devolver verdadero si alguna palabra tiene longitud mayor a 7. 
    \nEjemplo: ["termo", "gato", "tener", "jirafas"], devuelve falso.
    """
    
    for palabra in s:
        if len(palabra) > 7:
            return True
    
    return False



def es_palindromo(texto:str) -> bool:
    """ 
    Dado un texto en formato string, devolver verdadero si es palindromo (se lee igual en ambos sentidos), falso en caso contrario. 
    Las cadenas de texto vacias o con 1 solo elemento son palindromo
    """
    
    return texto == texto[::-1]



def hay_tres_iguales_consecutivos(numeros:list[int]) -> bool:
    """ 
    Recorrer una seq⟨Z⟩ y devolver verdadero si hay 3 numeros iguales consecutivos, en cualquier posicion y False en caso contrario.
    """
    for i in range(len(numeros) - 2):
        if numeros[i] == numeros[i+1] == numeros[i+2]:
            return True
    
    return False



def tiene_tres_vocales_distintas(palabra:str) -> bool:
    """ 
    Recorrer una palabra en formato string y devolver True si esta tiene al menos 3 vocales distintas y False en caso contrario.
    """
    vocales:list[str] = ['a', 'e', 'i', 'o', 'u']
    vocales_en_palabra:list[str] = []
    
    for letra in palabra:
        if letra in vocales and letra not in vocales_en_palabra:
            vocales_en_palabra.append(letra)
    
    return len(vocales_en_palabra) >= 3



def posicion_de_la_secuencia_mas_larga(numeros:list[int]) -> int:
    """ 
    Recorrer una seq⟨Z⟩ y devolver la posicion donde inicia la secuencia de numeros ordenada mas larga.\n
    Si hay dos subsecuencias de igual longitud devolver la posicion donde empieza la primera.\n
    La secuencia de entrada es no vacia.
    """
    contador_secuencia:int = 0
    maximo_contador:int = 0
    posicion:int = 0
    
    for i in range(len(numeros) - 1):
        if numeros[i] <= numeros[i+1]:
            contador_secuencia += 1
        else:
            if contador_secuencia > maximo_contador:
                maximo_contador = contador_secuencia
                posicion = i-contador_secuencia
                contador_secuencia = 0
            else:
                contador_secuencia = 0
    
    if contador_secuencia > maximo_contador:
        maximo_contador = contador_secuencia
        posicion = i-contador_secuencia
    
    return posicion



def cantidad_digitos_impares(numeros:list[int]) -> int:
    """ 
    problema cantidad_digitos_impares (in s:seq⟨Z⟩) : Z {
        requiere: {Todos los elementos de numeros son mayores o iguales a 0}
        asegura: {res es la cantidad total de digitos impares que aparecen en cada uno de los elementos de n´umeros}
    }
    Por ejemplo, si la lista de numeros es [57, 2383, 812, 246], entonces el resultado esperado seria 5 
    (los digitos impares son 5, 7, 3, 3 y 1).
    """
    contador_impares:int = 0
    
    for num in numeros:
        
        while num > 9:
            if (num % 10) % 2 == 1:
                contador_impares += 1
            num = num // 10
            
        if num % 2 == 1:
            contador_impares += 1
    
    return contador_impares



# Ejercicio 2

def ceros_en_posiciones_pares(s:list[int]):
    """ 
    problema CerosEnPosicionesPares (inout s:seq⟨Z⟩) {
        requiere: { True }
        modifica: {s}
        asegura: { (|s| = |s@pre|) y (para todo i entero, con 0 <= i < |s|, 
        si i es impar entonces s[i] = s@pre[i] y, 
        si i es par, entonces s[i] = 0)}
    }
    """
    for i in range(len(s)):
        if i % 2 == 0:
            s[i] = 0


def ceros_en_posiciones_pares_2(s:list[int]) -> list[int]:
    """ 
    problema CerosEnPosicionesPares2 (in s:seq⟨Z⟩) : seq⟨Z⟩ {
        requiere: { True }
        asegura: { (|s| = |res|) y (para todo i entero, con 0 <= i < |res|, 
        si i es impar entonces res[i] = s[i] y, 
        si i es par, entonces res[i] = 0) }
    }
    """
    res:list[int] = []
    
    for i in range(len(s)):
        if i % 2 == 0:
            res.append(0)
        else:
            res.append(s[i])
    
    return res


def sin_vocales(texto:str) -> str:
    """ 
    Dada una cadena de caracteres devuelva una cadena igual a la anterior, pero sin las vocales. 
    No se agregan espacios, sino que borra la vocal y concatena a continuacion.
    """
    vocales:list[str] = ['a', 'e', 'i', 'o', 'u']
    res:str = ""
    
    for letra in texto:
        if letra not in vocales:
            res += letra
    
    return res


def reemplaza_vocales(texto:str) -> str:
    """ 
    problema reemplaza vocales (in s:seq⟨Char⟩) : seq⟨Char⟩ {
        requiere: { True }
        asegura: {|res|= |s|}
        asegura: {Para todo i ∈ Z, si 0 ≤ i < |res| → (pertenece(<'a','e','i','o','u'>, s[i]) ∧ res[i] = '_') 
        ∨ (¬ pertenece(<'a','e','i','o','u'>, s[i]) ∧ res[i] = s[i] ) ) }
    }
    """
    vocales:list[str] = ['a', 'e', 'i', 'o', 'u']
    res:str = ""
    
    for letra in texto:
        if pertenece(vocales, letra):
            res += '_'
        else:
            res += letra
    
    return res


def da_vuelta_str(texto:str) -> str:
    """ 
    problema da vuelta str (in s:seq⟨Char⟩) : seq⟨Char⟩ {
        requiere: { True }
        asegura: {|res|= |s|}
        asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → res[i] = s[|s|−i −1]}
    }
    """
    res:str = ""
    largo_del_str:int = len(texto)
    
    for i in range(largo_del_str):
        res += texto[largo_del_str - i - 1]
    
    return res


def eliminar_repetidos(texto:str) -> str:
    """ 
    problema eliminar repetidos (in s:seq⟨Char⟩) : seq⟨Char⟩ {
        requiere: { True }
        asegura: {(|res| ≤ |s|) ∧ (para todo i ∈ Z si 0 ≤ i < |s| → pertenece(s[i], res)) ∧ (para todo i, j ∈ Z si (0 ≤ i, j < |res| ∧ i ̸= j) → res[i] ̸= res[j])}
    }
    """
    res:str = ""
    
    for letra in texto:
        if pertenece(res, letra):
            continue
        else:
            res += letra
    
    return res



# Ejercicio 3

def resultadoMateria(notas:list[int]) -> int:
    """ 
    problema resultadoMateria (in notas: seq⟨Z⟩) : Z{
        requiere: {|notas| > 0}
        requiere: {Para todo i ∈ Z si 0 ≤ i < |notas| → 0 ≤ notas[i] ≤ 10)}
        asegura: {res = 1 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio es mayor o igual a 7}
        asegura: {res = 2 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio esta entre 4 (inclusive) y 7}
        asegura: {res = 3 ↔ alguno de los elementos de notas es menor a 4 o el promedio es menor a 4}
    }
    """
    def todos_mayores_o_iguales_a(lista:list[int], numero:int) -> bool:
        for elem in lista:
            if elem < numero:
                return False
        
        return True

    def promedio(lista:list[int]) -> float:
        total:float = 0.0
        for elem in lista:
            total += elem
        
        return  (total / len(lista))

    
    if todos_mayores_o_iguales_a(notas, 4):
        if promedio(notas) >= 7:
            return 1
        elif 4 <= promedio(notas) < 7:
            return 2

    return 3



# Ejercicio 4

def saldo_actual(historial:list[tuple[str, int]]) -> int:
    """ 
    Dada una lista de tuplas, que representa un historial de movimientos en una cuenta bancaria, devolver el saldo actual. Asumir que el saldo inicial es 0. Las tuplas tienen una letra que nos indica el tipo de movimiento “I” para ingreso de dinero y “R” para retiro de dinero, y adem ́as el monto de cada operaci ́on. Por ejemplo, si la lista de tuplas es [("I", 2000), ("R", 20),("R", 1000),("I", 300)] entonces el saldo actual es 1280.
    """
    
    saldo:int = 0
    
    for movimiento in historial:
        if movimiento[0] == 'I':
            saldo += movimiento[1]
        elif movimiento[0] == 'R':
            saldo -= movimiento[1]

    return saldo



# Matrices

# Ejercicio 6

def es_matriz(s:list[list[int]]) -> bool:
    """ 
    problema es matriz (in s:seq⟨seq⟨Z⟩⟩) : Bool {
        requiere: { True }
        asegura: { res = true ↔ (|s| > 0) ∧ (|s[0]| > 0) ∧ (Para todo i ∈ Z si 0 ≤ i < |s| → |s[i]|= |s[0]|)}
    }
    """
    
    if len(s) > 0:
        if len(s[0]) > 0:
            largo_fila:int = len(s[0])
            
            for fila in s:
                if len(fila) != largo_fila:
                    return False
                
            return True
        
    return False


def filas_ordenadas(m:list[list[int]], res:list[bool]):
    """ 
    problema filas ordenadas (in m:seq⟨seq⟨Z⟩⟩, out res: seq⟨Bool⟩) {
        requiere: { esMatriz(m) }
        asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → (res[i] = true ↔ ordenados(s[i])) }
    }
    """
    res.clear()
    
    for fila in m:
        if ordenados(fila):
            res.append(True)
        else:
            res.append(False)


def columna(m:list[list[int]], c:int) -> list[int]:
    """ 
    problema columna (in m:seq⟨seq⟨Z⟩⟩, in c: Z) : seq⟨Z⟩ {
        requiere: { esMatriz(m) }
        requiere: { c < |m[0]| }
        requiere: { c ≥ 0 }
        asegura: { Devuelve una secuencia con exactamente los mismos elementos de la columna c de la matriz m, en el mismo orden que aparecen}
    }
    """
    res:list[int] = []
    
    for fila in m:
        res.append(fila[c])
    
    return res


def columnas_ordenadas(m:list[list[int]]) -> list[bool]:
    """ 
    problema columnas ordenadas (in m:seq⟨seq⟨Z⟩⟩) : seq⟨Bool⟩ {
        requiere: { esMatriz(m) }
        asegura: { Para toda columna c ∈ m → (res[c] = true ↔ ordenados(columna(m, c))) }
    }
    """
    res:list[bool] = []
    
    for c in range(len(m[0])):
        if ordenados(columna(m, c)):
            res.append(True)
        else:
            res.append(False)
    
    return res


def transponer(m:list[list[int]]) -> list[list[int]]:
    """ 
    problema transponer (in m:seq⟨seq⟨Z⟩⟩) : seq⟨seq⟨Z⟩⟩ {
        requiere: { esMatriz(m) }
        asegura: { Devuelve mt (o sea la matriz transpuesta)}
    }
    """
    res:list[list[int]] = []
    
    for c in range(len(m[0])):
        res.append(columna(m, c))
    
    return res


def quien_gana_tateti(m:list[str]) -> int:
    """ 
    problema quien gana tateti (in m:seq⟨seq⟨Char⟩⟩) : Z{
        requiere: {esMatriz(m)}
        requiere: {|m|= 3}
        requiere: {|m[0]|= 3}
        requiere: {En la matriz si hay 3 X alineadas verticalmente ⇒ no hay 3 O alineadas verticalmente}
        requiere: {En la matriz si hay 3 O alineadas verticalmente ⇒ no hay 3 X alineadas verticalmente}
        requiere: {En la matriz si hay 3 X alineadas horizontalmente ⇒ no hay 3 O alineadas horizontalmente}
        requiere: {En la matriz si hay 3 O alineadas horizontalmente ⇒ no hay 3 X alineadas horizontalmente}
        requiere: {(Para todo i, j ∈ {0, 1, 2}) (m[i][j] = X V m[i][j] = O V m[i][j] = ” ”)}
        asegura: {Si hay 3 O alineadas verticalmente, horizontalmente o en diagonal, devuelve 0}
        asegura: {Si hay 3 X alineadas verticalmente, horizontalmente o en diagonal, devuelve 1}
        asegura: {Si no hay ni 3 X, ni 3 O alineadas verticalmente, horizontalmente o en diagonal, devuelve 2}
    }
    """

    # Horizontal
    # Primera fila
    if (m[0][0] == "O" and m[0][1] == "O" and m[0][2] == "O"):
        return 0
    elif (m[0][0] == "X" and m[0][1] == "X" and m[0][2] == "X"):
        return 1
    # Segunda fila
    elif (m[1][0] == "O" and m[1][1] == "O" and m[1][2] == "O"):
        return 0
    elif (m[1][0] == "X" and m[1][1] == "X" and m[1][2] == "X"):
        return 1
    # Tercera fila
    elif (m[2][0] == "O" and m[2][1] == "O" and m[2][2] == "O"):
        return 0
    elif (m[2][0] == "X" and m[2][1] == "X" and m[2][2] == "X"):
        return 1
    # Vertical
    # Primera columna
    elif (m[0][0] == "O" and m[1][0] == "O" and m[2][0] == "O"):
        return 0
    elif (m[0][0] == "X" and m[1][0] == "X" and m[2][0] == "X"):
        return 1
    # Segunda columna
    elif (m[0][1] == "O" and m[1][1] == "O" and m[2][1] == "O"):
        return 0
    elif (m[0][1] == "X" and m[1][1] == "X" and m[2][1] == "X"):
        return 1
    # Tercera columna
    elif (m[0][2] == "O" and m[1][2] == "O" and m[2][2] == "O"):
        return 0
    elif (m[0][2] == "X" and m[1][2] == "X" and m[2][2] == "X"):
        return 1
    # Diagonal
    # Desde arriba-izquierda 
    elif (m[0][0] == "O" and m[1][1] == "O" and m[2][2] == "O"):
        return 0
    elif (m[0][0] == "X" and m[1][1] == "X" and m[2][2] == "X"):
        return 1
    # Desde arriba-derecha 
    elif (m[0][2] == "O" and m[1][1] == "O" and m[2][0] == "O"):
        return 0
    elif (m[0][2] == "X" and m[1][1] == "X" and m[2][0] == "X"):
        return 1
    
    return 2




# FALTA HACER
""" 
Opcional: Implementar una funci ́on que tome un entero d y otro p y eleve una matriz cuadrada de tama ̃no d con
valores generados al azar a la potencia p. Es decir, multiplique a la matriz generada al azar por s ́ı misma p veces.
Realizar experimentos con diferentes valores de d. ¿Qu ́e pasa con valores muy grandes?
Nota 1: record ́a que en la multiplicaci ́on de una matriz cuadrada de dimensi ́on d por si misma cada posici ́on se calcula
como res[i][j] = ∑d−1
k=0(m[i][k] ×m[k][j])
Nota 2: para generar una matriz cuadrada de dimensi ́on d con valores aleatorios hay muchas opciones de implemen-
taci ́on, analizar las siguientes usando la biblioteca numpy (ver recuadro):
Opci ́on 1:
import numpy as np
m = np.random.random((d, d))1
Opci ́on 2:
import numpy as np
m = np.random.randint(i,f, (d, d))2
Para poder importar la biblioteca numpy es necesario instalarla primero. Y para ello es necesario tener instalado
un gestor de paquetes, por ejemplo pip3 (Ubuntu: sudo apt install pip3. Windows: se instala junto con
Python). Una vez instalado pip3 se ejecuta pip3 install numpy.
4. Programas interactivos usando secuencias
Ejercicio 7. Vamos a elaborar programas interactivos (usando la funci ́on input()3) que nos permita solicitar al usuario
informaci ́on cuando usamos las funciones.
1. Implementar una funci ́on para construir una lista con los nombres de mis estudiantes. La funci ́on solicitar ́a al usuario
los nombres hasta que ingrese la palabra “listo”, o vac ́ıo (el usuario aprieta ENTER sin escribir nada). Devuelve la
lista con todos los nombres ingresados.
2. Implementar una funci ́on que devuelve una lista con el historial de un monedero electr ́onico (por ejemplo la SUBE).
El usuario debe seleccionar en cada paso si quiere:
“C” = Cargar cr ́editos,
“D” = Descontar cr ́editos,
“X” = Finalizar la simulaci ́on (terminar el programa).
En los casos de cargar y descontar cr ́editos, el programa debe adem ́as solicitar el monto para la operaci ́on. Vamos a
asumir que el monedero comienza en cero. Para guardar la informaci ́on grabaremos en el historial tuplas que representen
los casos de cargar (“C”, monto a cargar) y descontar cr ́edito (“D”, monto a descontar).
1https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random2https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html3https://docs.python.org/es/3/library/functions.html?highlight=input#input
P ́agina 5 de 6 Compilado el 2024/10/16 a las 14:56:20
"""



# Programas interactivos usando secuencias

# Ejercicio 7

def nombres_estudiantes() -> list[str]:
    """ 
    Implementar una funcion para construir una lista con los nombres de mis estudiantes. La funcion solicitara al usuario los nombres hasta que ingrese la palabra “listo”, o vacio (el usuario aprieta ENTER sin escribir nada). Devuelve la lista con todos los nombres ingresados.
    """
    res:list[str] = []
    
    while True:
        nombre:str = input("Ingrese el nombre de un estudiante ('listo' o ENTER para salir): ")
        
        if nombre == "listo" or nombre == "":
            break
        
        res.append(nombre)
    
    return res


def historial_monedero() -> list[tuple[str, int]]:
    """ 
    Implementar una funcion que devuelve una lista con el historial de un monedero electronico (por ejemplo la SUBE).
    El usuario debe seleccionar en cada paso si quiere:
    \n
        “C” = Cargar creditos,
        “D” = Descontar creditos,
        “X” = Finalizar la simulacion (terminar el programa).
    
    En los casos de cargar y descontar creditos, el programa debe ademas solicitar el monto para la operacion. Vamos a asumir que el monedero comienza en cero. Para guardar la informacion grabaremos en el historial tuplas que representen los casos de cargar (“C”, monto a cargar) y descontar credito (“D”, monto a descontar).
    """
    saldo:int = 0
    historial:list[tuple[str,int]] = []
    menu:str = "\nC = Cargar creditos,\nD = Descontar creditos,\nX = Salir"
    
    while True:
        opcion:str = input(menu + "\nIngrese la opcion deseada: ")
        
        if opcion == "X":
            break
        elif opcion == "C":
            monto:int = int(input("Ingrese el monto a cargar: "))
            saldo += monto
            historial.append(("C", monto))
        elif opcion == "D":
            monto:int = int(input("Ingrese el monto a descontar: "))
            saldo -= monto
            historial.append(("D", monto))
    
    return historial


def siete_y_medio() -> list[int]:
    """ 
    Vamos a escribir un programa para simular el juego conocido como 7 y medio. El mismo debera generar un numero aleatorio entre 0 y 12 (excluyendo el 8 y 9) y debera luego preguntarle al usuario si desea seguir sacando otra “carta” o plantarse. En este ultimo caso el programa debe terminar. \n
    Los numeros aleatorios obtenidos deberan sumarse segun el numero obtenido salvo por las “figuras” (10, 11 y 12) que sumaran medio punto cada una. \n
    El programa debe ir acumulando los valores y si se pasa de 7.5 debe informar que el usuario ha perdido. \n 
    Al finalizar la funcion devuelve el historial de “cartas” que hizo que el usuario gane o pierda. \n 
    Para generar numeros pseudo-aleatorios entre 1 y 12 utilizaremos la funcion random.randint(1,12). Al mismo tiempo, la funcion random.choice() puede ser de gran ayuda a la hora de repartir cartas.
    """
    
    def pedir_una_carta() -> int:
        carta:int = random.randint(1, 12)
        while pertenece([8, 9], carta):
            carta = random.randint(1, 12)
        return carta
    
    def valor_carta(carta:int) -> float:
        valor:float = 0.0
        if pertenece([10, 11, 12], carta):
            valor = 0.5
        else:
            valor = float(carta)
        return valor

    primera_carta:int = pedir_una_carta()
    historial:list[int] = []
    historial.append(primera_carta)
    suma_de_cartas:float = valor_carta(primera_carta)
    
    while True:
        print("La suma del valor de sus cartas es", suma_de_cartas)
        opcion:str = input("-'carta': Para sacar otra carta,\n-'plantarme': Para plantarse y terminar el juego")
        
        if opcion == "plantarme":
            print("El total se sus cartas queda en", suma_de_cartas)
            break
        elif opcion == "carta":
            nueva_carta = pedir_una_carta()
            historial.append(nueva_carta)
            suma_de_cartas += valor_carta(nueva_carta)
        
        if suma_de_cartas > 7.5:
            print("Perdiste, la suma de tus cartas es", suma_de_cartas)
            break
    
    return historial


def analizar_contraseña(password:str) -> str:
    """ 
    Analizar la fortaleza de una contrasena. Solicitar al usuario que ingrese un texto que sera su contrasena. Armar una funcion que tenga de parametro de entrada un string con la contrasena a analizar, y la salida otro string con tres posibles valores: VERDE, AMARILLA y ROJA. Nota: en python la “ñ/Ñ” es considerado un caracter especial y no se comporta como cualquier otra letra. String es seq⟨Char⟩. Consejo: para ver si una letra es mayuscula se puede ver si esta ordenada entre A y Z.
    \n
    La contrasena sera VERDE si:\n
        a) la longitud es mayor a 8 caracteres.
        b) tiene al menos 1 letra minuscula.
        c) tiene al menos 1 letra mayuscula.
        d) tiene al menos 1 digito numerico (0..9)
    La contrasena sera ROJA si:\n
        a) la longitud es menor a 5 caracteres.\n
    En caso contrario sera AMARILLA.
    """
    def tiene_minuscula(password:str) -> bool:
        for caracter in password:
            if 'a' <= caracter <= 'z':
                return True
        return False
    
    def tiene_mayuscula(password:str) -> bool:
        for caracter in password:
            if 'A' <= caracter <= 'Z':
                return True
        return False
    
    def tiene_digito(password:str) -> bool:
        for caracter in password:
            if '0' <= caracter <= '9':
                return True
        return False
    
    if len(password) > 8:
        if tiene_minuscula(password) and tiene_mayuscula(password) and tiene_digito(password):
            return "VERDE"
    elif len(password) < 5:
        return "ROJA"
    
    return "AMARILLA"




print("Ejercicio 1:")

print("\n1.")
print(pertenece([1,4,6,7], 4))
print(pertenece2([1,4,6,7], 7))
print(pertenece3([1,4,6,7], 1))
print(pertenece([1,4,6,7], 2))
print(pertenece2([1,4,6,7], 3))
print(pertenece3([1,4,6,7], 5))

print("\n2.")
print(divide_a_todos([4,8,12,40], 4))
print(divide_a_todos([4,8,12,41], 4))

print("\n3.")
print(suma_total([4,8,12,41]))

print("\n4.")
print(maximo([4,8,12,41]))

print("\n5.")
print(minimo([4,8,2,12,41]))

print("\n6.")
print(ordenados([2,4,8,12,41]))
print(ordenados([4,8,2,12,41]))

print("\n7.")
print(pos_maximo([4,8,82,12,41]))
print(pos_maximo([4,8,82,12,41,82]))
print(pos_maximo([]))

print("\n8.")
print(pos_minimo([4,8,82,12,41]))
print(pos_minimo([4,8,82,12,41,4]))
print(pos_minimo([]))

print("\n9.")
print(hay_palabra_larga(["termo", "gato", "tener", "jirafas"]))
print(hay_palabra_larga(["termo", "gato", "tener", "jirafas", "elefante"]))
print(hay_palabra_larga([]))

print("\n10.")
print(es_palindromo("asdfdsa"))
print(es_palindromo("hola"))
print(es_palindromo("a"))
print(es_palindromo(""))

print("\n11.")
print(hay_tres_iguales_consecutivos([4,8,82,12,41]))
print(hay_tres_iguales_consecutivos([4,8,12,12,12,4]))
print(hay_tres_iguales_consecutivos([]))

print("\n12.")
print(tiene_tres_vocales_distintas("frutilla"))
print(tiene_tres_vocales_distintas("abecedario"))
print(tiene_tres_vocales_distintas("elefante"))
print(tiene_tres_vocales_distintas(""))

print("\n13.")
print(posicion_de_la_secuencia_mas_larga([4,3,8,82,12,41,53,64]))
print(posicion_de_la_secuencia_mas_larga([4,8,12,12,12,4]))
print(posicion_de_la_secuencia_mas_larga([]))

print("\n14.")
print(cantidad_digitos_impares([4,3,8,82,12,41,53,64]))
print(cantidad_digitos_impares([57, 2383, 812, 246]))
print(cantidad_digitos_impares([]))



print("\nEjercicio 2:")

print("\n1.")
lista:list[int] = [1,3,5,6,7,89,6,4,3,2]
print("Antes:", lista)
ceros_en_posiciones_pares(lista)
print("Después:", lista)

print("\n2.")
print(ceros_en_posiciones_pares_2([1,3,5,6,7,89,6,4,3,2]))

print("\n3.")
print(sin_vocales("frutilla"))
print(sin_vocales("abecedario"))
print(sin_vocales("elefante y cocodrilo"))
print(sin_vocales(""))

print("\n4.")


print("\n5.")


print("\n6.")

# FALTAN PROBAR VARIOS