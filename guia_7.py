# Ejercicio 1

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
    Ejemplo: ["termo", "gato", "tener", "jirafas"], devuelve falso.
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
    vocales:list[chr] = ['a', 'e', 'i', 'o', 'u']
    vocales_en_palabra:list[chr] = []
    
    for letra in palabra:
        if letra in vocales and letra not in vocales_en_palabra:
            vocales_en_palabra.append(letra)
    
    return len(vocales_en_palabra) >= 3



def posicion_de_la_secuencia_mas_larga(numeros:list[int]) -> int:
    """ 
    Recorrer una seq⟨Z⟩ y devolver la posicion donde inicia la secuencia de numeros ordenada mas larga. 
    Si hay dos subsecuencias de igual longitud devolver la posicion donde empieza la primera. 
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


print("\nEjercicio 2:")
