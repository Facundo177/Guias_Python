"""
ENUNCIADO


1) Ejercicio 1 [2.25 puntos]
Implementar la función subsecuencia_mas_larga especificada.

problema subsecuencia_mas_larga (in v: seq⟨Z⟩) : ZxZ {
    requiere: { La longitud de v es distinto de 0 }
    asegura: { Sea x la primera subsecuencia más larga en v tal que vale todos_consecutivos(x), 
                la primera componente de res es igual a |x| y la segunda es igual al índice en v donde comenzaría x }
}

problema todos_consecutivos (in v: seq⟨Z⟩) : Bool {
    asegura: { res == True <==> cada par de elementos adyacentes en v son números consecutivos,
                es decir, que su diferencia es igual a 1 }
}


2) Ejercicio 2 [2.25 puntos]
Ana tiene exámenes de respuesta Verdadero ó Falso. 
Ella sabe que en cada examen la cantidad de respuestas correctas cuyo valor es Falso es igual a la cantidad de respuestas correctas cuyo valor es Verdadero. 
Tenemos el historial de las respuestas de cada exámen dados por Ana en una cola. 
En cada uno Ana respondió todas las preguntas.

problema mejor_resultado_de_ana (in examenes: Cola⟨ seq⟨Bool⟩ ⟩) : seq⟨Z⟩ {
    requiere:{ Cada elemento de examenes es no vacío y tiene longitud par }
    asegura: { res tiene la misma cantidad de elementos que examenes }
    asegura: { res[i] es igual a la máxima cantidad de respuestas correctas que Ana podría haber respondido 
                en el i-ésimo exámen resuelto en examenes, para 0 <= i < cantidad de elementos de examenes }
}


3) Ejercicio 3 [2.25 puntos]
problema cambiar_matriz(inout A: seq⟨seq⟨Z⟩⟩) {
    requiere: { Todas las filas de A tienen la misma longitud }
    requiere: { El mínimo número que aparece en A es igual a 1 }
    requiere: { El máximo número que aparece en A es igual a #filas de A por #columnas de A }
    requiere: { No hay enteros repetidos en A }
    requiere: { Existen al menos dos enteros distintos en A }
    modifica: { A }
    asegura: { A tiene exactamente las mismas dimensiones que A@pre }
    asegura: { El conjunto de elementos que aparecen en A es igual al conjunto de elementos que aparecen en A@pre }
    asegura: { A[i][j] != A@pre[i][j] para todo i, j en rango }
}


4) Ejercicio 4 [2.25 puntos]
Tenemos un texto que contiene palabras. Por simplicidad, las palabras están separadas únicamente por uno o más espacios.

problema palabras_por_vocales (in texto: string): Diccionario⟨Z,Z⟩ {
    requiere: { Si existe una letra vocal en texto, esta no lleva tildes, diéresis, ni ningún otro símbolo }
    asegura: { Si existe una palabra en texto con x vocales en total, x es clave de res }
    asegura: { Las claves de res representan la cantidad total de vocales de una palabra, 
                y cada valor corresponde a la cantidad de palabras en texto con ese número de vocales. }
    asegura: { Los valores de res son positivos }
}


5) Pregunta teórica (1 punto)
Conteste marcando la opción correcta.

¿Por qué en Paradigma Imperativo no existe la transparencia referencial?
    Utilizamos otro mecanismo de repetición de código, en lugar de recursión usamos la iteración (FOR, WHILE, DO WHILE).
●   Tenemos una nueva instrucción, la asignación, que nos permite cambiar el valor de una variable
    El orden en que se ejecutan las instrucciones del programa es diferente
"""


from queue import Queue as Cola
from queue import LifoQueue as Pila


# Auxiliares
def todos_consecutivos(v:list[int]) -> bool:
    """
    cada par de elementos adyacentes en v son números consecutivos, 
    es decir, que su diferencia es igual a 1
    """
    # Un ayudante dijo que consecutivos cuenta +1 y -1 
    # osea [1,2,3] y [3,2,1] se consideran consecutivos los dos
    # entonces tomo que el modulo de la diferencia es 1
    
    for i in range(len(v)-1):
        if modulo(v[i] - v[i+1]) != 1:
            return False
    return True

def cant_de_trues(lista:list[bool]) -> int:
    contador:int = 0
    for elem in lista:
        if elem:
            contador += 1
    return contador

def modulo(numero:int) -> int:
    if numero < 0:
        numero = -numero
    return numero

def separar_en_palabras(texto:str) -> list[str]:
    res:list[str] = []
    palabra:str = ""
    for letra in texto:
        if letra == " ":
            res.append(palabra)
            palabra = ""
        else:
            palabra += letra
    res.append(palabra)
    
    return res

def pertenece(elemento, lista:list) -> bool:
    for elem in lista:
        if elem == elemento:
            return True
    return False



# Ejercicio 1
def subsecuencia_mas_larga(v: list[int]) -> tuple[int,int]:
    subsecuencias_ordenadas:dict[int, list[int]] = {}
    
    # Un ayudante dijo que consecutivos cuenta +1 y -1 
    # osea [1,2,3] y [3,2,1] se consideran consecutivos los dos
    # entonces tomo que el modulo de la diferencia es 1
    subsecuencia:list[int] = []
    for i in range(len(v)-1):
        subsecuencia.append(v[i])
        if modulo(v[i] - v[i+1]) != 1:
            subsecuencias_ordenadas[i+1-len(subsecuencia)] = subsecuencia
            subsecuencia = []
            
    if subsecuencia != []:
        subsecuencia.append(v[len(v)-1])
        subsecuencias_ordenadas[len(v)-len(subsecuencia)] = subsecuencia
        subsecuencia = []
    else:
        subsecuencias_ordenadas[len(v)-1] = [v[len(v)-1]]
    
    subsec_mayor:tuple[int, list[int]] = (0, subsecuencias_ordenadas[0])
    for indice, subsec in subsecuencias_ordenadas.items():
        if len(subsec) > len(subsec_mayor[1]):
            subsec_mayor = (indice, subsec)
    
    res:tuple[int, int] = (len(subsec_mayor[1]), subsec_mayor[0])
        
    return res



# Ejercicio 2
def mejor_resultado_de_ana(examenes: Cola[list[bool]]) -> list[int]:
    """
    En cada examen la cantidad de respuestas correctas cuyo valor es Falso 
    es igual a la cantidad de respuestas correctas cuyo valor es Verdadero. 
    Tenemos el historial de las respuestas de cada exámen dados por Ana en una cola. 
    En cada uno Ana respondió todas las preguntas.
    """
    res:list[int] = []
    auxiliar:Cola = Cola()
    while not examenes.empty():
        examen:list[bool] = examenes.get()
        auxiliar.put(examen)
        
        cant_preguntas:int = len(examen)
        respuestas_V:int = cant_de_trues(examen)
        errores:int = modulo((cant_preguntas // 2) - respuestas_V)
        
        max_correctas:int = cant_preguntas - errores 
        res.append(max_correctas)
    
    while not auxiliar.empty():
        examenes.put(auxiliar.get())
    
    return res



# Ejercicio 3
def cambiar_matriz(A: list[list[int]]) -> None:
    """
    A[i][j] != A@pre[i][j] para todo i, j en rango
    No hay enteros repetidos en A 
    """
    # pienso intercambiar en cada fila un elemento con el siguiente
    # para que no se repita la posicion de ninguno
    for fila in A:
        for i in range(len(fila)-1):
            auxiliar:int = fila[i]
            fila[i] = fila[i+1]
            fila[i+1] = auxiliar



# Ejercicio 4
def palabras_por_vocales(texto: str) -> dict[int, int]:
    """
    Tenemos un texto que contiene palabras. 
    Por simplicidad, las palabras están separadas únicamente por uno o más espacios.
    Las vocales en el texto no llevan tildes, diéresis, ni ningún otro símbolo.
    
    Las claves de res representan la cantidad total de vocales de una palabra, 
    y cada valor corresponde a la cantidad de palabras en texto con ese número de vocales.
    """
    res:dict[int, int] = {}
    palabras:list[str] = separar_en_palabras(texto)
    vocales:list[str] = ["a","A","e","E","i","I","o","O","u","U"]
    
    for palabra in palabras:
        cant_vocales:int = 0
        for letra in palabra:
            if pertenece(letra, vocales):
                cant_vocales += 1
        if cant_vocales == 0:
            continue
        if not pertenece(cant_vocales, list(res.keys())):
            res[cant_vocales] = 1
        else:
            res[cant_vocales] += 1
    
    return res




## EJEMPLOS
#
## Ej 1
#print("Ejercicio 1")
#secuencia:list[int] = [7,8,9,4,3,2,1,9,10,11,12]
#print(subsecuencia_mas_larga(secuencia))
#secuencia:list[int] = [7,8,9,4,3,2,1,9,10,11]
#print(subsecuencia_mas_larga(secuencia))
#secuencia:list[int] = [7,8,9,10,4,3,2,1,9,10,11,12]
#print(subsecuencia_mas_larga(secuencia))
#secuencia:list[int] = [-8,-7,-6,-5,-11,-10,-9,-8,-7]
#print(subsecuencia_mas_larga(secuencia))
#secuencia:list[int] = [-8,-7,-6,-5,-6,-7,-11,-10,-9,-8,-7]
#print(subsecuencia_mas_larga(secuencia))
#secuencia:list[int] = [1,2,3,7,6,5,4,5,6,7]
#print(subsecuencia_mas_larga(secuencia))
#secuencia:list[int] = [1]
#print(subsecuencia_mas_larga(secuencia))
#
#print()
#
#
## Ej 2
#print("Ejercicio 2")
#examenes1:Cola[list[bool]] = Cola()
#examenes1.put([True,True,False,False]) # 4 res max
#examenes1.put([True,True,False,False,True,True]) # 5 res max
#examenes1.put([True,True,False,False,True,False]) # 6 res max
#examenes1.put([True,True,True,True,True,True]) # 3 max
#print(mejor_resultado_de_ana(examenes1))
#
#examenes2:Cola[list[bool]] = Cola()
#examenes2.put([True,True]) # 1 res max
#examenes2.put([False,False]) # 1 res max
#examenes2.put([False,False,False,False,True,True]) # 5 res max
#examenes2.put([False,False,False,False]) # 2 res max
#print(mejor_resultado_de_ana(examenes2))
#
#examenes3:Cola[list[bool]] = Cola()
#print(mejor_resultado_de_ana(examenes3))
#
#print()
#
#
## Ej 3
#print("Ejercicio 3")
#matriz1:list[list[int]] = [
#    [1,4,5],
#    [7,9,2],
#    [3,6,8]
#]
#print(matriz1)
#cambiar_matriz(matriz1)
#print(matriz1)
#
#matriz2:list[list[int]] = [
#    [1, 4, 5, 16],
#    [7, 9, 2, 11],
#    [3, 6, 8, 15],
#    [10,12,14,13]
#]
#print(matriz2)
#cambiar_matriz(matriz2)
#print(matriz2)
#
#matriz3:list[list[int]] = [
#    [1, 4, 5, 6],
#    [7, 3, 2, 8],
#]
#print(matriz3)
#cambiar_matriz(matriz3)
#print(matriz3)
#
#print()
#
#
## Ej 4
#print("Ejercicio 4")
#texto:str = "Hola Don Pepito hola Don Jose"
##              2   1     3     2   1    2
#print(palabras_por_vocales(texto))
#
#texto:str = "Habia una casa en el bosque"
##              3    2   2   1  1    3    
#print(palabras_por_vocales(texto))
#
#texto:str = "   Habia    una   casa en    el bosque"
##                 3       2     2   1     1    3    
#print(palabras_por_vocales(texto))
#
#texto:str = "  aaaaaa   abcaio ooiioiu yuionsd"
##                6        4       7       3      
#print(palabras_por_vocales(texto))
#
#texto:str = ""     
#print(palabras_por_vocales(texto))