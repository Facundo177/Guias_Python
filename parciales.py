from queue import Queue as Cola
from queue import LifoQueue as Pila

# AUXILIARES

def pertenece(elemento, lista:list) -> bool:
    for elem in lista:
        if elem == elemento:
            return True
    return False




# VARIANTE MAS DIFICIL

def esta_bien_balanceada(s:str) -> bool:
    """La idea es crear una pila con todos los signos que abren y cada vez que se encuentre uno de cierre comparar si coincide con el de arriba de la pila"""
    cola_apertura:Pila[str] = Pila()
    signos_apertura:list[str] = ["(","{","["]
    signos_cierre:list[str] = [")","}","]"]
    paridad:dict[str,str] = {
        "(":")",
        "[":"]",
        "{":"}"
    }
    for caracter in s:
        if pertenece(caracter, signos_apertura):
            cola_apertura.put(caracter)
        elif pertenece(caracter, signos_cierre):
            if cola_apertura.empty():
                return False
            else:
                simbolo:str = cola_apertura.get()
                if caracter != paridad[simbolo]:
                    return False

    return cola_apertura.empty()



print("[esta_bien_balanceada] True", esta_bien_balanceada("()"))  # True
print("[esta_bien_balanceada] True", esta_bien_balanceada("()({})[]"))  # True
print("[esta_bien_balanceada] False", esta_bien_balanceada("()({)}[]"))  # False
print("[esta_bien_balanceada] False", esta_bien_balanceada("()({})["))  # False








"""
1) Fila en ExactaBank (1 p)

En el banco ExactaBank los clientes hacen cola para ser atendidos por un representante. Los clientes son
 representados por las tuplas
(nombre, tipo afiliado) donde la primera componente es el nombre y el tipo afiliado puede ser "comun" o "vip".
Se nos pide implementar una función en Python que dada una cola de clientes del banco, devuelva 
una nueva cola con los mismos clientes, pero en donde
los clientes vipp están primero que los clientes comunes manteniendo el orden original de 
los clientes vips y los comunes entre sí.

problema reordenar_cola_priorizando_vips(in: filaClientes: Cola<String x String>): Cola<String> {
    requiere: {la longitud de los valores de la primera componentes de las tuplas de la cola filaClientes 
    es mayor a 0}
    requiere: {los valores de la segunda componente de las tuplas de la cola filaClientes son "comun" o "vip"}
    requiere: {no hay dos tuplas en filaClientes que tengan la primer componente iguales entre sí}
    asegura: {todo valor de res aparece como primera componente de alguna tupla de filaClientes}
    asegura: {|res| = |filaClientes|}
    asegura: {res no tiene elementos repetidos}
    asegura: {no hay ningun cliente "comun" antes que un "vip" en res}
    asegura: {para todo cliente c1 y cliente c2 de tipo "comun" pertenecientes a filaClientes, 
    si c1 aparece antes que c2 en filaClientes entonces el nombre de
    c1 aparece antes que el nombre de c2 en res}
    asegura: {para todo cliente c1 y cliente c2 de tipo "vip" pertenecientes a filaClientes, 
    si c1 aparece antes que c2 en filaClientes, entonces el nombre de
    c1 aparece antes que el nombre de c2 en res}
}
"""

def reordenar_cola_priorizando( filaClientes: Cola[str, str] ) -> Cola[str]:
    aux: Cola[str] = Cola()
    cola_vip : Cola[str] = Cola()
    cola_comun: Cola[str] = Cola()
    
    while not filaClientes.empty():
        cliente = filaClientes.get()

        if cliente[1] == "vip":
            cola_vip.put(cliente[0])
            aux.put(cliente)
        if cliente[1] == "comun":
            cola_comun.put(cliente[0])
            aux.put(cliente)


    while not cola_comun.empty():
        cola_vip.put(cola_comun.get())        
    while not aux.empty():
        filaClientes.put(aux.get())
        
    return cola_vip

filaClientes = Cola()
filaClientes.put(("Juan", "vip"))
filaClientes.put(("Ana", "comun"))
filaClientes.put(("Pedro", "vip"))
filaClientes.put(("Luis", "comun"))

filaClientes = reordenar_cola_priorizando(filaClientes)

#print(filaClientes.queue)

"""
2) Chicken Game (3p)

El juego de la gallina es una competición en la que dos participantes conducen un vehículo en dirección 
al del contrario; si alguno se desvía de la trayectoria
de choque pierde y es humillado por comportarse como un "gallina". Se hizo un torneo para ver quién es menos 
gallina. Juegan todos contra todos una vez y van
sumando puntos o restando. Si dos jugadores juegan y se chocan entre sí, entonces pierde cada uno 5 puntos por
 haberse dañado. Si ambos jugadores se desvían,
cada uno pierde 10 puntos por gallinas. Si uno no se desvía y el otro sí, el gallina pierde 15 puntos por ser
 humillado y el ganador suma 10 puntos! En este
torneo, cada persona que participa tiene una estrategia predefinida para competir: o siempre se desvía, o nunca
 lo hace. Se debe programar la función
"torneo_de_gallinas" que recibe un diccionario (donde las claves representan los nombres de los participantes 
que se anotaron en el torneo, y los valores
sus respectivas estrategias) y devuelve un diccionario con los puntajes obtenidos por cada jugador.

problema torneo_de_gallinas(in: estrategias: dict(String,String)) : dict(String, Z) {
    requiere: {estrategias tiene por lo menos 2 elementos (jugadores)}
    requiere: {las claves de estrategias tienen longitud mayor a 0}
    requiere: {los valores de estrategias sólo pueden ser los strings "me desvio siempre" o "me la 
    banco y no me desvio"}
    asegura: {las claves de res y las claves de estrategias son iguales}
    asegura: {para cada jugador p perteneciente a claves(estrategias), res[p] es igual a la cantidad de 
    puntos que obtuvo al finalizar el torneo, dado que
    jugó una vez contra cada otro jugador}
}
"""

def torneo_de_gallinas( estrategias: dict[str, str]) -> dict[str,int]:
    res:dict[str,int] = {}
    
    for participante_1, estrategia_1 in estrategias.items():
        for participante_2, estrategia_2 in estrategias.items():
            
            if participante_1 == participante_2:
                continue
            if not pertenece(participante_1, list(res.keys())):
                res[participante_1] = 0
            
            if estrategia_1 == estrategia_2 == "me la banco y no me desvio":
                res[participante_1] -= 5
            elif estrategia_1 == estrategia_2 == "me desvio siempre":
                res[participante_1] -= 10
            elif estrategia_1 == "me desvio siempre" and estrategia_2 == "me la banco y no me desvio":
                res[participante_1] -= 15
            elif estrategia_1 == "me la banco y no me desvio" and estrategia_2 == "me desvio siempre":
                res[participante_1] += 10
    
    return res


torneo_de_gallinas({"Juan": "me desvio siempre", "Pedro": "me la banco y no me desvio", "Maria": "me desvio siempre", "Jose": "me la banco y no me desvio"})
print("[torneo_de_gallinas]",torneo_de_gallinas({"Juan": "me desvio siempre", "Pedro": "me la banco y no me desvio", "Maria": "me desvio siempre", "Jose": "me la banco y no me desvio"}))



"""
3) Cuasi Ta-Te-Ti (2 puntos)
Ana y Beto juegan al Ta-Te-Ti-Facilito. El juego es en un tablero cuadrado de lado entre 5 y 10. Cada jugador va poniendo su
ficha en cada turno. Juegan intercaladamente y comienza Ana. Ana pone siempre una "X" en su turno y Beto pone una "O" en 
el suyo. Gana la persona que logra poner 3 fichas suyas consecutivas en forma vertical. SI el tablero está completo y no ganó
nadie, entonces se declara un empate. El tablero comienza vacío, representado por " " en cada posición.
Notar que dado que juegan por turnos y comienza Ana poniendo una "X" se cumple que la cantidad de "X" es igual a la 
cantidad  de "O" o bien la cantidad de "X" son uno más que la cantidad de "O".
Se nos pide implementar una función en pyhon 'problema_quien_gano_el_tateti_facilito' que determine si ganó alguno, o si
Beto hizo trampa (puso una 'O' cuando Ana ya había ganado).

problema quien_gano_el_tateti_facilito(in tablero: sez<seq<Char>>) : Z{
    requiere: {tablero es una matriz cuadrada}
    requiere: {5 <= |tablero[0]| <= 10]}
    requiere: {tablero sólo tiene 'X', 'O' y '' (espacio vacío) como elementos}
    requiere: {En tablero la cantidad de 'X' es igual a la cantidad de 'O' o bien la cantidad de 'X' es uno más que la cantidad de
    'O'}
    asegura: {res = 1 <==> hay tres 'X' consecutivas en forma vertical (misma columna) y no hay tres 'O' consecutivas en forma
    vertical(misma columna)}
    asegura: {res = 0 <==> no hay tres 'O' ni hay tres 'X' consecutivas en forma vertical}
    asegura: {res = 3 <==> hay tres 'X' y hay tres 'O' consecutivas en forma vertical (evidenciando que beto hizo trampa)}
}
"""

def quien_gano_el_tateti_facilito(tablero: list[list[str]]) -> int:
    """Gana la persona que logra poner 3 fichas suyas consecutivas en forma vertical."""
    gana_ana:bool = False
    gana_beto:bool = False
    res:int = 0
    
    for num_col in range(len(tablero[0])):
        for i in range(3, len(tablero)):
            if tablero[i-1][num_col] == tablero[i-2][num_col] == tablero[i-3][num_col]:
                if tablero[i-1][num_col] == "X":
                    gana_ana = True
                elif tablero[i-1][num_col] == "O":
                    gana_beto = True
    
    if gana_ana and gana_beto:
        return 3
    elif gana_ana:
        return 1
    else:
        return 0


tablero1 = [
        ["X", "O", "X", "O", "X"],
        ["X", "O", "X", "O", "X"],
        ["X", "O", "X", "O", "X"],
        ["X", "O", "X", "O", "X"],
        ["X", "O", "X", "O", "X"],
]

tablero2 = [
    ["X", "O", "X", "O", "X"],
    ["O", "X", "O", "X", "O"],
    ["X", "O", "X", "O", "X"],
    ["O", "X", "O", "X", "O"],
    ["X", "O", "X", "O", "X"],
]
print("[quien_gano_el_tateti_facilito]", quien_gano_el_tateti_facilito(tablero1))
print("[quien_gano_el_tateti_facilito]", quien_gano_el_tateti_facilito(tablero2))


"""
4) Cuántos palíndromos sufijos (2 puntos)
Decimos que una palabra es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda. Se nos pide
programar en python la siguiente función:

problema cuantos_sufijos_son_palindromos(in texto:String) : Z{
    requiere: {-}
    asegura: {res es igual a la cantidad de palíndromos que hay en el conjunto de sufijos de texto}
"""

def sin_espacios(palabra:str) -> str:
    sin_espacios:str = ""
    for letra in palabra:
        if letra == " ":
            continue
        sin_espacios += letra
    return sin_espacios

def invertida(palabra:str) -> str:
    invertida:str = ""
    for i in range(len(palabra)-1, -1, -1):
        invertida += palabra[i]
    return invertida

def sufijo(palabra:str) -> str:
    sufijo:str = ""
    for i in range(1, len(palabra)):
        sufijo += palabra[i]
    return sufijo


def cuantos_sufijos_son_palindromos(texto:str) -> int:
    texto_limpio:str = sin_espacios(texto)
    cant_palindromos:int = 0
    for _ in range(len(texto_limpio)):
        
        print(texto_limpio)
        
        if texto_limpio == invertida(texto_limpio):
            cant_palindromos += 1
        
        texto_limpio = sufijo(texto_limpio)

    return cant_palindromos


print(cuantos_sufijos_son_palindromos("Diego"))







# ------------------------------------------------------------------------------------------------------------------------------------













"""
1) Índice de la n-ésima aparición [2 puntos]
Guido y Marcela son dos estudiantes de IP, nervioses con el parcial de Python. 
Con el objetivo de tener un rato antes del parcial para preguntarse algunas dudas 
deciden encontrarse en el colectivo y viajar juntes. 
Para poder coordinar de forma exacta en qué colectivo se tienen que subir, 
Marcela usa sus habilidades de programación aprendidas en IP para acceder de forma 
poco legítima a la base de datos de colectivos de todas las empresas. 
Con esto, arma una lista de todos los colectivos que van a pasar por la parada de
Guido alrededor del horario acordado y le indica a Guido que se tiene que subir en 
el 3er colectivo de la línea 34. Por desgracia, Guido se olvida sus lentes antes 
de salir y no es capaz de distinguir a qué línea pertenece cada colectivo que 
llega a la parada. Por lo que solo puede contar cantidad total de colectivos que 
pasan.
Implementar la función ind_nesima_aparicion que dada una secuencia de enteros s, 
y dos enteros n y elem devuelve la posición en la cual elem aparece por n-ésima vez 
en s. En caso de que elem aparezca menos de n veces en s, devolver -1.

problema ind_nesima_aparicion (in s: seq⟨Z⟩, in n: Z, in elem: Z) : Z {
  requiere: {n>0}
  asegura: {Si el elemento aparece menos de n veces en la secuencia, res= -1 }
  asegura: {Si el elemento aparece al menos n veces en la secuencia, s[res] = elem }
  asegura: {Si el elemento aparece al menos n veces en la secuencia, elem aparece n-1 
  veces en s entre las posiciones 0 y res-1 }

Por ejemplo, dadas
s = [-1, 1, 1, 5, -7, 1, 3]
n = 2
elem = 1
se debería devolver res = 2
"""


def ind_nesima_aparicion(s:list[int], n:int, elem:int) -> int:
    contador_apariciones:int = 0
    
    for i in range(len(s)):
        if s[i] == elem:
            contador_apariciones += 1
        if contador_apariciones >= n:
            return i
    return -1

s = [-1, 1, 1, 5, -7, 1, 3]
n = 2
elem = 1
print(ind_nesima_aparicion(s, n, elem))




"""
2) Mezclar [2 puntos]
A la hora de jugar juegos de cartas, como el truco, el tute, o el chinchón, 
es importante que la distribución de las mismas en el mano sea aleatoria. 
Para esto, al comienzo de cada mano, antes de repartir las mismas se realizan 
mezclan sucesivas. Una técnica de mezclado es la denominada "mezcla americana" 
que consiste en separar el mazo en (aproximadamente) dos mitades e intercalar 
las cartas de ambas mitades. Implementar la función mezclar que dadas dos listas 
s1 y s2 con igual cantidad de elementos devuelva una lista con los elementos 
intercalados. Esto es, las posiciones pares de res tendrán los elementos de s1 
y las posiciones impares los elementos de s2, respetando el orden original.

problema mezclar (in s1: seq⟨Z⟩, in s2: seq⟨Z⟩) : seq⟨Z⟩ {
  requiere: {|s1| = |s2| }
  asegura: {|res| = 2 * |s1|}
  asegura: {res[2*i] = s1[i] y res[2*i+1] = s2[i], para i entre 0 y |s1|-1}
}
TIP: realizar la iteración mediante índices y no mediante elementos

Por ejemplo, dadas
s1 = [1, 3, 0, 1]
s2 = [4, 0, 2, 3]
se debería devolver res = [1, 4, 3, 0, 0, 2, 1, 3]
"""

def mezclar(s1:list[int], s2:list[int]) -> list[int]:
    res:list[int] = []
    for i in range(len(s1)):
        res.append(s1[i])
        res.append(s2[i])

    return res

s1 = [1, 3, 0, 1]
s2 = [4, 0, 2, 3]
print(mezclar(s1, s2))



"""
3) A los pingos: resultado carreras [3 puntos]
Además de recitales de artistas de renombre internacional (ej: Bizarrap), 
en el hipódromo de Palermo se realizan cotidianamente carreras de caballos. 
Por ejemplo, durante el mes de Octubre se corrieron 10 carreras. En cada una de
ellas participaron alrededor de 10 caballos.
Implementar la función frecuencia_posiciones_por_caballo que dada la lista de 
caballos que corrieron las carreras, y el diccionario que tiene los resultados del 
hipódromo en el formato carreras:posiciones_caballos, donde carreras es un String 
y posiciones_caballos es una lista de strings con los nombres de los caballos, 
genere un diccionario de caballos:#posiciones, que para cada caballo devuelva la 
lista de cuántas veces salió en esa posición.

Tip: para crear una lista con tantos ceros como caballos se puede utilizar la siguiente 
sintaxis lista_ceros = [0]*len(caballos)

problema frecuencia_posiciones_por_caballo(in caballos: seq⟨String⟩, in carreras: 
dict⟨String,seq⟨String⟩⟩: dict⟨String,seq⟨Z⟩⟩ {
    requiere: {caballos no tiene repetidos}
    requiere: {Los valores del diccionario carreras son permutaciones de la lista 
    caballos (es decir, tienen exactamente los mismos elementos que caballos, en 
    cualquier orden posible)}
    asegura: {res tiene como claves los elementos de caballos}
    asegura: {El valor en res de un caballo es una lista que indica en la posición i 
    cuántas veces salió ese caballo en la i-ésima posición.}
}
Por ejemplo, dados
caballos= ["linda", "petisa", "mister", "luck" ]
carreras= {"carrera1":["linda", "petisa", "mister", "luck"],
            "carrera2":["petisa", "mister", "linda", "luck"]}
se debería devolver res = {"petisa": [1,1,0,0],
                            "mister": [0,1,1,0],
                            "linda": [1,0,1,0],
                            "luck": [0,0,0,2]}
"""

def frecuencia_posiciones_por_caballo(caballos:list[str], carreras:dict[str,list[str]]) -> dict[str,list[int]]:
    """
    Implementar la función frecuencia_posiciones_por_caballo que dada la lista de caballos que corrieron las carreras, y el diccionario que tiene los resultados del hipódromo en el formato carreras:posiciones_caballos, donde carreras es un String y posiciones_caballos es una lista de strings con los nombres de los caballos, genere un diccionario de caballos:#posiciones, que para cada caballo devuelva la lista de cuántas veces salió en esa posición.
    """
    
    

    return



"""
4) Matriz capicúa [3 puntos]
Implementar la función matriz_capicua que dada una matriz devuelve True si 
cada una de sus filas es capicúa. Es decir, si cada fila es igual leída de 
izquierda a derecha o de derecha a izquierda. Definimos a una secuencia de
secuencias como matriz si todos los elemento de la primera secuencia tienen 
la misma longitud.

problema matriz_capicua(in m:seq⟨seq⟨Z⟩⟩ ) : Bool {
  requiere: {todos los elementos de m tienen igual longitud (los elementos de m son secuencias)}
  asegura: {(res = true) <=> todos los elementos de m son capicúa}
}

Por ejemplo, dada la matriz
m = [[1,2,2,1],[-5,6,6,-5],[0,1,1,0]]
se debería devolver res = true
"""