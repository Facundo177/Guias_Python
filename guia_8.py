from queue import LifoQueue as Pila
from queue import Queue as Cola
import random

# 1. PILAS

# Ejercicio 1
def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila[int]:
    """
    Implementar una funcion generar nros al azar(in cantidad:int, in desde:int, in hasta:int) -> Pila[int] que genere una pila de cantidad de numeros enteros al azar en el rango [desde, hasta].
    """
    res:Pila[int] = Pila()
    for _ in range(cantidad):
        n:int = random.randint(desde, hasta)
        res.put(n)
    
    return res

def mostrar_pila(pila:Pila[int]):
    """
    Muestra por pantalla cada elemento de la pila sin modificar su contenido.
    """
    pilaAuxiliar:Pila[int] = Pila()

    # Mostramos los elementos sacandolos de la pila original para mostrarlos y se guardan en orden inverso en la pila auxiliar
    while not pila.empty():
        elem:int = pila.get()
        print(elem)
        pilaAuxiliar.put(elem)

    # Devolvemos los elementos a la pila original en el orden correcto
    while not pilaAuxiliar.empty():
        elem:int = pilaAuxiliar.get()
        pila.put(elem)



# Ejercicio 2 
def cantidad_elementos(p:Pila) -> int:
    """
    Implementar una funcion cantidad elementos(in p : Pila) → int que, dada una pila, cuente y devuelva la cantidad de elementos que contiene. No se puede utilizar la funcion LifoQueue.qsize(). Si se usa get() para recorrer la pila, esto modifica el parametro de entrada. Y como la especificacion dice que es de tipo in hay que restaurarla.
    """
    pilaAuxiliar:Pila[int] = Pila()
    res:int = 0

    # Contador sobre los elementos de la pila original, sacandolos, y guardándolos en orden inverso en la pila auxiliar
    while not p.empty():
        elem:any = p.get()
        res += 1
        pilaAuxiliar.put(elem)

    # Devolvemos los elementos a la pila original en el orden correcto
    while not pilaAuxiliar.empty():
        elem:any = pilaAuxiliar.get()
        p.put(elem)

    return res



# Ejercicio 3 
def buscar_el_maximo(p:Pila[int]) -> int:
    """
    Dada una pila de enteros, implementar una funcion buscar el maximo(in p : Pila[int]) → int que devuelva el maximo elemento.
    """

    if p.empty():
        return

    # Agarro el primer valor
    maximo:int = p.get()
    p.put(maximo)

    pilaAuxiliar:Pila[int] = Pila()

    # Comparo cada elemento de la pila original, sacandolos, y guardándolos en orden inverso en la pila auxiliar
    while not p.empty():
        elem:any = p.get()
        if elem > maximo:
            maximo = elem
        pilaAuxiliar.put(elem)

    # Devolvemos los elementos a la pila original en el orden correcto
    while not pilaAuxiliar.empty():
        elem:any = pilaAuxiliar.get()
        p.put(elem)

    return maximo



# Ejercicio 4 
def buscar_nota_maxima(p:Pila[tuple[str, int]]) -> tuple[str, int]:    
    """
    Dada una pila de tuplas de string x enteros, implementar una funcion buscar nota maxima(in p : Pila[tuple[str, int]]) → tuple[str, int]
    que devuelva la tupla donde aparece la maxima nota (segunda componente de la tupla). La pila no esta vacia, no hay valores en las segundas posiciones repetidas en la pila.
    """

    # Agarro el primer valor
    nota_max:tuple[str, int] = p.get()
    pilaAuxiliar:Pila[tuple[str, int]] = Pila()
    pilaAuxiliar.put(nota_max)

    # Comparo cada elemento de la pila original, sacandolos, y guardándolos en orden inverso en la pila auxiliar
    while not p.empty():
        elem:tuple[str, int] = p.get()
        if elem[1] > nota_max[1]:
            nota_max = elem
        pilaAuxiliar.put(elem)

    # Devolvemos los elementos a la pila original en el orden correcto
    while not pilaAuxiliar.empty():
        elem:tuple[str, int] = pilaAuxiliar.get()
        p.put(elem)

    return nota_max



# Ejercicio 5
def esta_bien_balanceada(s:str) -> bool:        
    """
    Implementar una funcion esta bien balanceada(in s : str) → bool que dado un string con una formula aritmetica sobre los enteros, diga si los parentesis estan bien balanceados. 
    Las formulas pueden formarse con: los numeros enteros, las operaciones basicas +, -, * y /, parentesis, espacios.
    Entonces las siguientes son formulas aritmeticas con sus parentesis bien balanceados:
    . 1 + ( 2 x 3 - ( 20 / 5 ) )     
    . 10 * ( 1 + ( 2 * ( -1)))
    Y la siguiente es una formula que no tiene los parentesis bien balanceados:  1 + ) 2 x 3 ( ()
    """
    
    listaParentesis:list[str] = []
    
    for caracter in s:
        if pertenece(caracter, ["(", ")"]):
            listaParentesis.append(caracter)
    
    lenP:int = len(listaParentesis)
    
    if lenP % 2 != 0:
        return False
    
    for i in range(lenP//2):
        if listaParentesis[i] != "(" or listaParentesis[lenP - 1 - i] != ")":
            return False
    
    return True



# Ejercicio 6. 
def evaluar_expresion(s:str) -> float:
    """
    La notacion polaca inversa, tambien conocida como notacion postfix, es una forma de escribir expresiones matematicas en la que los operadores siguen a sus operandos. Por ejemplo, la expresion “3 + 4” se escribe como “3 4 +” en notacion postfix. 
    Escribe una funcion evaluar expresion(in s : str) → float en Python que tome una expresion en notacion postfix y la evalue. La expresion estara representada como una cadena de caracteres, donde los operandos y operadores estaran separados por espacios. Para simplificar el problema, solo vamos a considerar los operandos +, -, * y / (suma, resta, multiplicacion y division), los operadores son numeros.
    Para resolver este problema, se recomienda seguir el siguiente algoritmo:\n
    1. Dividir la expresion en tokens (operandos y operadores) utilizando espacios como delimitadores.\n
    2. Recorre los tokens uno por uno.\n
        a) Si es un operando, agregalo a una pila. \n
        b) Si es un operador, saca los dos operandos superiores de la pila, aplicale el operador y luego coloca el resultado en la pila.\n
    3. Al final de la evaluacion, la pila contendra el resultado de la expresion.
    """

    pila_operandos:Pila[str] = Pila()

    def separar_en_tokens(s:str) -> list[str]:
        tokens:list[str] = s.split(" ")
        return tokens
    
    def aplicar_operacion(operador:str, valor1:str, valor2:str):
        if operador == "+":
            return int(valor2) + int(valor1)
        elif operador == "-":
            return int(valor2) - int(valor1)
        elif operador == "*":
            return int(valor2) * int(valor1)
        elif operador == "/":
            return int(valor2) / int(valor1)
    
    for token in separar_en_tokens(s):
        if token in ["+","-","*","/"]:
            pila_operandos.put(aplicar_operacion(token, pila_operandos.get(), pila_operandos.get()))
        else:
            pila_operandos.put(token)

    return pila_operandos.get()



# Ejercicio 7
def intercalar(p1:Pila, p2:Pila) -> Pila:
    """
    \nImplementar una funcion que dadas dos pilas de igual longitud devuelve una nueva pila con los elementos intercalados. 
    \nintercalar(p1:Pila, p2:Pila)->Pila. 
    \nEl tope de la pila resultado sera el tope de la p2. 
    \nNota: Ojo que hay que recorrer dos veces para que queden en el orden apropiado al final.
    """
    res:Pila = Pila()
    pilaAuxiliar:Pila = Pila()
    
    # Junto ambas pilas, de forma intercalada, en una pila auxiliar
    while not p2.empty():
        pilaAuxiliar.put(p2.get())
        pilaAuxiliar.put(p1.get())

    # Los paso a res en el orden correcto
    while not pilaAuxiliar.empty():
        res.put(pilaAuxiliar.get())

    return res




# 2. COLAS

# Ejercicio 8
def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Cola[int]:
    """ 
    Implementar una funcion generar nros al azar(in cantidad:int, in desde:int, in hasta:int) → Cola[int] que genere una cola de cantidad de numeros enteros al azar en el rango [desde, hasta]. Pueden usar la funcion random.randint(< desde >, < hasta >) y la clase Queue() que es un ejemplo de una implementacion basica de una Cola.
    """
    cola:Cola[int] = Cola()
    
    for _ in range(cantidad):
        numero:int = random.randint(desde, hasta)
        cola.put(numero)
    
    return cola



# Ejercicio 9
def cantidad_elementos_cola(c:Cola):
    """ 
    Implementar una funcion cantidad elementos(in c : Cola) → int que, dada una cola, cuente y devuelva la cantidad de elementos que contiene. Comparar con la version usando pila. No se puede utilizar la funcion Queue.qsize().
    """
    contador_elems:int = 0
    cola_auxiliar:Cola = Cola()
    
    while not c.empty():
        elem:any = c.get()
        contador_elems += 1
        cola_auxiliar.put(elem)

    while not cola_auxiliar.empty():
        c.put(cola_auxiliar.get())

    return contador_elems



# Ejercicio 10
def buscar_el_maximo_cola(c:Cola[int]) -> int:
    """ 
    Dada una cola de enteros, implementar una funcion buscar el maximo(in c : Cola[int]) → int que devuelva el maximo elemento. Comparar con la version usando pila.
    """
    if c.empty():
        return
    
    cola_auxiliar:Cola[int] = Cola()
    maximo:int = c.get()
    cola_auxiliar.put(maximo)
    
    while not c.empty():
        elem:int = c.get()
        
        if elem > maximo:
            maximo = elem
        
        cola_auxiliar.put(elem)

    while not cola_auxiliar.empty():
        c.put(cola_auxiliar.get())

    return maximo



# Ejercicio 11
def buscar_nota_minima(c:Cola[tuple[str, int]]) -> tuple[str, int]:
    """ 
    Dada una cola de tuplas de string x enteros, implementar una funcion buscar nota minima(in c : Cola[str, int]) → int que devuelva la tupla donde aparece la minima nota (segunda componente de la tupla). La cola no esta vacia, no hay valores en las segundas posiciones repetidas en la cola.
    """
    if c.empty():
        return
    
    cola_auxiliar:Cola[tuple[str, int]] = Cola()
    primer_tupla:tuple[str, int] = c.get()
    minima_nota:int = primer_tupla[1]
    cola_auxiliar.put(primer_tupla)
    
    while not c.empty():
        tupla:tuple[str, int] = c.get()
        
        if minima_nota > tupla[1]:
            minima_nota = tupla[1]
        
        cola_auxiliar.put(tupla)
    
    while not cola_auxiliar.empty():
        c.put(cola_auxiliar.get())

    return minima_nota



# Ejercicio 12
def intercalar(c1:Cola, c2:Cola) -> Cola:
    """ 
    Implementar una funcion que dadas dos colas de igual longitud devuelve una nueva cola con los elementos intercalados. El primer elemento de la cola resultado sera el primer elemento de la c1.
    """
    
    res:Cola = Cola()
    cola_auxiliar:Cola = Cola()
    
    while not c1.empty():
        elem1 = c1.get()
        elem2 = c2.get()
        res.put(elem1)
        res.put(elem2)
        cola_auxiliar.put(elem1)
        cola_auxiliar.put(elem2)
    
    # Devuelvo los elementos a su cola original, para no modificar los parámetros de entrada
    while not cola_auxiliar.empty():
        elem1 = cola_auxiliar.get()
        elem2 = cola_auxiliar.get()
        c1.put(elem1)
        c2.put(elem2)
    
    return res



# Ejercicio 13
def armar_secuencia_de_bingo() -> Cola[int]:
    """ 
    Implementar una funcion armar secuencia de bingo() → Cola[int] que genere una cola con los numeros del 0 al 99
    ordenados al azar.
    """
    res:Cola[int] = Cola()
    
    numeros:list[int] = list(range(100))
    random.shuffle(numeros)
    
    for num in numeros:
        res.put(num)
    
    return res

def jugar_carton_de_bingo(carton:list[int], bolillero:Cola[int]) -> int:
    """ 
    Bingo: un carton de bingo contiene 12 numeros al azar en el rango [0, 99].
    - Implementar una funcion jugar carton de bingo(in carton : list[int], in bolillero:Cola[int]) → int que toma un     carton de Bingo y una cola de enteros (que corresponden a las bolillas numeradas) y determina cual es la cantidad de jugadas de ese bolillero que se necesitan para ganar.
    """
    bolillas_en_carton:int = 0
    jugadas:int = 0
    
    while bolillas_en_carton < 12:
        bolilla:int = bolillero.get()
        if pertenece(bolilla, carton):
            bolillas_en_carton += 1
        jugadas += 1
    
    return jugadas



# Ejercicio 14
def n_pacientes_urgentes(c:Cola[tuple[int, str, str]]) -> int:
    """ 
    Vamos a modelar una guardia de un hospital usando una cola donde se van almacenando los pedidos de atencion para los pacientes que van llegando.\n 
    A cada paciente se le asigna una prioridad del 1 al 10 (donde la prioridad 1 es la mas urgente y requiere atencion inmediata) junto con su nombre y la especialidad medica que le corresponde.\n
    Implementar la funcion n pacientes urgentes(in c:Cola[tuple[int, str, str]]) → int que devuelve la cantidad de pacientes de la cola que tienen prioridad en el rango [1, 3].
    """
    cola_auxiliar:Cola[tuple[int, str, str]] = Cola()
    cant_urgentes:int = 0
    
    while not c.empty():
        paciente:tuple[int, str, str] = c.get()
        cola_auxiliar.put(paciente)
        if paciente[0] < 4:
            cant_urgentes += 1
    
    while not cola_auxiliar.empty():
        c.put(cola_auxiliar.get())
    
    return cant_urgentes



# Ejercicio 15
def atencion_a_clientes(c:Cola[tuple[str, int, bool, bool]]) -> Cola[tuple[str, int, bool, bool]]:
    """ 
    La gerencia de un banco nos pide modelar la atencion de los clientes usando una cola donde se van registrando los pedidos de atencion. Cada vez que ingresa una persona a la entidad, debe completar sus datos en una pantalla que esta a la entrada: Nombre y Apellido, DNI, tipo de cuenta (si es preferencial o no) y si tiene prioridad por ser adulto +65, embarazada o con movilidad reducida (prioridad si o no).
    La atencion a los clientes se da por el siguiente orden: primero las personas que tienen prioridad, luego las que tienen cuenta bancaria preferencial y por ultimo el resto. Dentro de cada subgrupo de clientes, se respeta el orden de llegada.
    - Implementar atencion a clientes(in c:Cola[tuple[str, int, bool, bool]]) → Cola[tuple[str, int, bool, bool]] que dada la cola de ingreso de clientes al banco devuelve la cola en la que van a ser atendidos.
    """
    res:Cola[tuple[str, int, bool, bool]] = Cola()
    cola_auxiliar:Cola[tuple[str, int, bool, bool]] = Cola()
    
    con_prioridad:Cola[tuple[str, int, bool, bool]] = Cola()
    con_cuenta_pref:Cola[tuple[str, int, bool, bool]] = Cola()
    con_poca_prioridad:Cola[tuple[str, int, bool, bool]] = Cola()
    
    # Clasificar
    while not c.empty():
        cliente:tuple[str, int, bool, bool] = c.get()
        cola_auxiliar.put(cliente)
        
        if cliente[3]:
            con_prioridad.put(cliente)
        elif cliente[2]:
            con_cuenta_pref.put(cliente)
        else:
            con_poca_prioridad.put(cliente)
    
    # Devolver todo a la cola original
    while not cola_auxiliar.empty():
        c.put(cola_auxiliar.get())
    
    # Respuesta ordenada
    while not con_prioridad.empty():
        res.put(con_prioridad.get())
    while not con_cuenta_pref.empty():
        res.put(con_cuenta_pref.get())
    while not con_poca_prioridad.empty():
        res.put(con_poca_prioridad.get())
    
    return res




# 3. DICCIONARIOS

# Ejercicio 16
def agrupar_por_longitud(nombre_archivo:str) -> dict[int, int]:
    """ 
    Leer un archivo de texto y agrupar la cantidad de palabras de acuerdo a su longitud. Implementar la funcion agrupar por longitud(in nombre archivo:str) → dict que devuelve un diccionario {longitud en letras : cantidad de palabras}.
    \n
    Ej el diccionario
    \n\{
        1: 2,
        2: 10,
        5: 4
    }
    indica que se encontraron 2 palabras de longitud 1, 10 palabras de longitud 2 y 4 palabras de longitud 5. Para este ejercicio vamos a considerar palabras a todas aquellas secuencias de caracteres que no tengan espacios en blanco.
    """
    archivo = open(nombre_archivo, "r")
    contenido:list[str] = archivo.readlines()
    archivo.close()
    
    largo_palabra:int = 0
    res:dict[int, int] = {}
    
    for linea in contenido:
        for letra in linea:
            if letra == " " or letra == "\n":
                if not pertenece(largo_palabra, list(res.keys())):
                    res[largo_palabra] = 1
                else:
                    res[largo_palabra] += 1
                largo_palabra = 0
            else:
                largo_palabra += 1
    
    return res



# Ejercicio 17
def calcular_promedio_por_estudiante(notas:list[tuple[str, float]]) -> dict[str, float]:
    """ 
    Dada una secuencia de tuplas, donde cada tupla tiene en la primera componente el nombre de un estudiante, y en la esgunda componenete la nota que saco en un examen; se pide devolver un diccionario con los promedios de todos los estudiantes. La clave del diccionario debe ser el nombre del estudiante, y el valor el promedio de todos sus examenes.
    """
    def promedio(list_notas:list[float]) -> float:
        total:float = 0
        for nota in list_notas:
            total += nota
        return (total / len(list_notas))
    
    res:dict[str, float] = dict()
    dict_auxiliar:dict[str, list[float]] = dict()

    for examen in notas:
        estudiante:str = examen[0]
        nota:float = examen[1]
        if not dict_auxiliar[estudiante]:
            dict_auxiliar[estudiante] =  []
        dict_auxiliar[estudiante].append(nota)
    
    for estudiante, examenes in dict_auxiliar.items():
        res[estudiante] = promedio(examenes)

    return res



# Ejercicio 18
def la_palabra_mas_frecuente(nombre_archivo:str) -> str:
    """ 
    Implementar la funcion la palabra mas frecuente(in nombre archivo:str) → str que devuelve la palabra que mas veces aparece en un archivo de texto. Se aconseja utilizar un diccionario de palabras para resolver el problema.
    """
    archivo = open(nombre_archivo, "r")
    contenido:list[str] = archivo.readlines()
    archivo.close()
    
    palabra:str = ""
    apariciones:dict[str, int] = {}
    
    for linea in contenido:
        for letra in linea:
            if letra == " " or letra == "\n":
                if not pertenece(palabra, list(apariciones.keys())):
                    apariciones[palabra] = 1
                else:
                    apariciones[palabra] += 1
                palabra = ""
            else:
                palabra += letra
    
    if palabra != "":
        if not pertenece(palabra, list(apariciones.keys())):
            apariciones[palabra] = 1
        else:
            apariciones[palabra] += 1
        palabra = ""
    
    palabra_mas_frecuente:tuple[str, int] = tuple()
    for pal, cant in apariciones.items():
        if palabra_mas_frecuente == tuple():
            palabra_mas_frecuente = (pal, cant)
        elif palabra_mas_frecuente[1] < cant:
            palabra_mas_frecuente = (pal, cant)
    
    return palabra_mas_frecuente[0]



# Ejercicio 19
""" 
Nos piden desarrollar un navegador web muy simple que debe llevar un registro de los sitios web visitados por los usuarios del sistema. El navegador debe permitir al usuario navegar hacia atras y hacia adelante en la historia de navegacion.
"""

def visitar_sitio(historiales:dict[str, Pila[str]], usuario:str, sitio:str):
    """ 
    Implementar visitar sitio(inout:historiales:dict[str, Pila[str]], in:usuario:str, in:sitio:str) que reciba el diccionario de historiales, el nombre de usuario y el sitio web visitado. La funcion debe agregar el sitio web al historial del usuario correspondiente.
    """
    if not pertenece(usuario, list(historiales.keys())):
        historiales[usuario] = Pila()
        historiales[usuario].put(sitio)
    else:
        historiales[usuario].put(sitio)


def navegar_atras(historiales:dict[str, Pila[str]], usuario:str):
    """ 
    Implementar navegar atras(inout:historiales: dict[str, Pila[str]], in:usuario:str) que permita al usuario navegar hacia atras en la historia de navegacion. Primero debemos obtener el sitio anterior al actual, y luego poner este como ultimo en la pila.
    """
    sitio_actual:str = historiales[usuario].get()
    sitio_anterior:str = historiales[usuario].get()
    
    historiales[usuario].put(sitio_actual)
    historiales[usuario].put(sitio_anterior)



# Ejercicio 20 
""" 
Nos piden desarrollar un sistema de gestion de inventario para una tienda de ropa. Este sistema permite llevar un registro de los productos en el inventario y realizar operaciones como agregar nuevos productos, actualizar las existencias y calcular el valor total del inventario.
Para resolver este problema vamos a utilizar un diccionario llamado inventario que almacene informacion sobre los productos. Cada elemento del diccionario debe tener el nombre del producto como clave y otro diccionario cuya clave sea un string que
indique un atributo del producto ("precio","cantidad") y su valor sea un Float o un Int, dependiendo del atributo clave.
"""

def agregar_producto(inventario:dict[str, dict[str, float | int]], nombre:str, precio:float, cantidad:int):
    """ 
    Implementa una funcion llamada agregar producto(inout inventario:dict[str, dict[str, float | int]], in nombre:str, in precio:float, in cantidad:int) que permita agregar un nuevo producto al inventario. El nombre del producto debe ser la clave del diccionario, y el valor debe ser otro diccionario con las claves “precio” y “cantidad”. Como requisito de esta funcion el producto a agregar no esta en el inventario.
    """
    inventario[nombre] = {"precio": precio , "cantidad": cantidad}

def actualizar_stock(inventario:dict[str, dict[str, float | int]], nombre:str, cantidad:int):
    """ 
    Implementa una funcion llamada actualizar stock(inout inventario:dict[str, dict[str, float | int]], in nombre:str, in cantidad:int) que permita actualizar la cantidad de un producto existente en el inventario.
    """
    inventario[nombre]["cantidad"] = cantidad

def actualizar_precios(inventario:dict[str, dict[str, float | int]], nombre:str, precio:float):
    """ 
    Implementa una funcion llamada actualizar precios(inout inventario:dict[str, dict[str, float | int]], in nombre:str, in precio:float) que permita actualizar el precio de un producto existente en el inventario.
    """
    inventario[nombre]["precio"] = precio

def calcular_valor_inventario(inventario:dict[str, dict[str, float | int]]) -> float:
    """ 
    Implementa una funcion llamada calcular valor inventario(in inventario:dict[str, dict[str, float | int]]) → float que calcule el valor total del inventario multiplicando el precio por la cantidad de cada producto y sumando los valores de todos los productos.
    """
    total:float = 0
    
    for _, diccionario in inventario.items():
        total += diccionario["cantidad"] * diccionario["precio"]
    
    return total




# 4. ARCHIVOS

def pertenece(elem, lista:list) -> bool:
    for elemento in lista:
        if elem == elemento:
            return True
        
    return False


def separar_palabras(texto:str) -> list[str]:
    caracteres_especiales:list[str] = [" ",".",",",";",":","\n"]
    res:list[str] = []
    palabra:str = ""
    
    for letra in texto:
        if pertenece(letra, caracteres_especiales):
            if palabra != "":          
                res.append(palabra)
            palabra = ""
        else:
            palabra += letra
    if palabra != "":          
                res.append(palabra)

    return res


def sacar_espacios_iniciales(texto:str) -> str:
    res:str = ""
    inicio_texto:int = 0

    for i in range(len(texto)):
        if texto[i] == " ":
            continue
        else:
            inicio_texto = i
            break
    
    for i in range(inicio_texto, len(texto)):
        res += texto[i]

    return res



# Ejercicio 21 
def contar_lineas(nombre_archivo:str) -> int:
    """ 
    Una funcion contar lineas(in nombre archivo : str) → int que cuenta y devuelva la cantidad de lineas de texto del archivo dado.
    """
    res:int = 0
    archivo = open(nombre_archivo, "r")
    contenido:list[str] = archivo.readlines()
    archivo.close()

    res = len(contenido)
    return res


def existe_palabra(palabra:str, nombre_archivo:str) -> bool:
    """ 
    Una funcion existe palabra(in palabra : str, in nombre archivo:str) → bool que dice si una palabra existe en un archivo de texto o no
    """
    archivo = open(nombre_archivo, "r")
    contenido:list[str] = archivo.readlines()
    archivo.close()

    palabras_del_texto:list[str] = []
    
    for linea in contenido:
        palabras_del_texto += separar_palabras(linea)

    for p in palabras_del_texto:
        if palabra == p:
            return True
    
    return False


def cantidad_apariciones(nombre_archivo:str, palabra:str) -> int:
    """ 
    Una funcion cantidad apariciones(in nombre archivo:str, in palabra:str) → int que devuelve la cantidad de apariciones de una palabra en un archivo de texto
    """
    contador_de_palabra:int = 0
    archivo = open(nombre_archivo, "r")
    contenido:list[str] = archivo.readlines()
    archivo.close()

    palabras_del_texto:list[str] = []
    
    for linea in contenido:
        palabras_del_texto += separar_palabras(linea)

    for p in palabras_del_texto:
        if palabra == p:
            contador_de_palabra += 1
    
    return contador_de_palabra



# Ejercicio 22
def clonar_sin_comentarios(nombre_archivo_entrada:str, nombre_archivo_salida:str):
    """ 
    Dado un archivo de texto con comentarios, implementar una funcion clonar sin comentarios(in nombre_archivo_entrada:str, in nombre_archivo_salida:str) que toma un archivo de entrada y genera un nuevo archivo que tiene el contenido original sin las lineas comentadas. Para este ejercicio vamos a considerar comentarios como aquellas lineas que tienen un caracter # como primer caracter de la linea, o si no es el primer caracter, se cumple que todos los anteriores son espacios. 
    \n
    Ejemplo: \n
    \# esto es un comentario \n
        \# esto tambien \n
    esto no es un comentario \# esto tampoco
    """
    archivo_entrada = open(nombre_archivo_entrada, "r")
    contenido:list[str] = archivo_entrada.readlines()
    archivo_entrada.close()

    contenido_clonado:list[str] = []

    for linea in contenido:
        if sacar_espacios_iniciales(linea)[0] == "#":
            continue
        else:
            contenido_clonado.append(linea)

    archivo_salida = open(nombre_archivo_salida, "w")
    archivo_salida.writelines(contenido_clonado)
    archivo_salida.close()



# Ejercicio 23 
def invertir_lineas(nombre_archivo:str):
    """ 
    Dado un archivo de texto, implementar una funcion invertir lineas(in nombre archivo : str), que escribe un archivo nuevo llamado reverso.txt que tiene las mismas lineas que el original, pero en el orden inverso.
    \n
    Ejemplo: si el archivo original es: \n
        Esta es la primera linea.
        Y esta es la segunda.
    \n
    debe generar: \n
        Y esta es la segunda.
        Esta es la primera linea.
    """
    archivo_entrada = open(nombre_archivo, "r")
    contenido:list[str] = archivo_entrada.readlines()
    archivo_entrada.close()

    pila_de_lineas:Pila[str] = Pila()
    
    for linea in contenido:
        pila_de_lineas.put(linea)

    contenido_clonado:list[str] = []

    while not pila_de_lineas.empty():
        linea:str = pila_de_lineas.get()
        if linea[len(linea)-1] != "\n":
            linea += "\n"
        contenido_clonado.append(linea)

    archivo_salida = open("reverso.txt", "w")
    archivo_salida.writelines(contenido_clonado)
    archivo_salida.close()



# Ejercicio 24 
def agregar_frase_al_final(nombre_archivo:str, frase:str):
    """ 
    Dado un archivo de texto y una frase, implementar una funcion agregar frase al final(in nombre archivo:str, in frase:str), que la agregue al final del archivo original (sin hacer una copia).
    """
    archivo_entrada = open(nombre_archivo, "r")
    contenido:list[str] = archivo_entrada.readlines()
    archivo_entrada.close()

    ultima_linea:str = contenido[len(contenido)-1]

    if ultima_linea[len(ultima_linea)-1] != "\n":
        ultima_linea += "\n"
    
    contenido[len(contenido)-1] = ultima_linea

    contenido.append(frase)

    archivo_salida = open(nombre_archivo, "w")
    archivo_salida.writelines(contenido)
    archivo_salida.close()



# Ejercicio 25 
def agregar_frase_al_principio(nombre_archivo:str, frase:str):
    """ 
    Dado un archivo de texto y una frase, implementar una funcion agregar frase al principio(in nombre archivo:str, in frase:str), que agregue la frase al comienzo del archivo original (similar al ejercicio anterior, sin hacer una copia del archivo)
    """
    archivo_entrada = open(nombre_archivo, "r")
    contenido:list[str] = archivo_entrada.readlines()
    archivo_entrada.close()

    contenido_nuevo:list[str] = []
    contenido_nuevo.append(frase + "\n")
    for linea in contenido:
        contenido_nuevo.append(linea)

    archivo_salida = open(nombre_archivo, "w")
    archivo_salida.writelines(contenido_nuevo)
    archivo_salida.close()



# Ejercicio 26
def listar_palabras_de_archivo(nombre_archivo:str) -> list:
    """
    Implementar una funcion listar palabras de archivo(in nombre archivo:str) → list, que lea un archivo en modo binario y devuelva la lista de palabras legibles, donde vamos a definir una palabra legible como: 
    secuencias de texto formadas por numeros, letras mayusculas/minusculas y los caracteres ' '(espacio) y ' '(guion bajo) que tienen longitud >= 5
    Una vez implementada la funcion, probarla con diferentes archivos binarios (.exe, .zip, .wav, .mp3, etc).
    Referencia: https://docs.python.org/es/3/library/functions.html#open
    Para resolver este ejercicio se puede abrir un archivo en modo binario 'b'. Al hacer read() vamos a obtener una secuencia de bytes, que al hacer chr(byte) nos va a devolver un caracter correspondiente al byte leido.
    """
    archivo_entrada = open(nombre_archivo, "rb")
    secuencia_bytes = archivo_entrada.read()
    archivo_entrada.close()
    
    lista_palabras:list[str] = []
    palabra_legible:str = ""
    
    for byte in secuencia_bytes:
        caracter:str = chr(byte)
        if len(palabra_legible) >= 5 and pertenece(caracter, [" ",",",".",";","\n"]):
            lista_palabras.append(palabra_legible)
            palabra_legible = ""
        else:
            palabra_legible += caracter
            
    if palabra_legible != "":
        lista_palabras.append(palabra_legible)
    
    return lista_palabras



# Ejercicio 27
def calcular_promedio_por_estudiante(nombre_archivo_notas:str, nombre_archivo_promedios:str):
    """ 
    Implementar una funcion calcular promedio por estudiante(in nombre archivo notas:str, in nombre archivo promedios:str), que lea un archivo de texto separado por comas (comma-separated values, o .csv) que contiene las notas de toda la carrera de un grupo de estudiantes y calcule el promedio final de uno. El resultado se guardara en un archivo ”nombre archivo promedios.csv” El archivo tiene el siguiente formato:
    nro de LU (str), materia (str), fecha (str), nota (float)
    Para modularizar el codigo, implementar la funcion promedio estudiante(in nombre archivo, in lu:str) → float.
    """
    
    def promedio_estudiante(nombre_archivo:str, lu:str) -> float:
        return


























print("PILAS")

print("\nEjercicio 1:")
ejemplo_pila= generar_nros_al_azar(5, 10, 20)
mostrar_pila(ejemplo_pila)
mostrar_pila(ejemplo_pila)

print("\nEjercicio 2:")
print("Cant:")
print(cantidad_elementos(ejemplo_pila))
print("Pila no modificada")
mostrar_pila(ejemplo_pila)

print("\nEjercicio 3:")
print("Max:")
print(buscar_el_maximo(ejemplo_pila))
print("Pila no modificada")
mostrar_pila(ejemplo_pila)

print("\nEjercicio 4:")
notas:Pila[tuple[str, int]] = Pila()
notas.put(("Juan", 7))
notas.put(("Pedro", 9))
notas.put(("Jose", 8))
notas.put(("Maria", 6))
print(buscar_nota_maxima(notas))

print("\nEjercicio 5:")
print(esta_bien_balanceada("1 + ( 2 x 3 - ( 20 / 5 ) )"))
print(esta_bien_balanceada("10 * ( 1 + ( 2 * ( -1)))"))
print(esta_bien_balanceada("1 + ) 2 x 3 ( ("))

print("\nEjercicio 6")
expresion = "3 4 + 5 * 2 -"
resultado = evaluar_expresion(expresion)
print(resultado) # Deberia devolver 33




####### FALTAN MUCHOS TESTS #######


historiales = {}
visitar_sitio(historiales, "Usuario1", "google.com")
visitar_sitio(historiales, "Usuario1", "facebook.com")
navegar_atras(historiales, "Usuario1")
visitar_sitio(historiales, "Usuario2", "youtube.com")



####### FALTAN MUCHOS TESTS #######


print(separar_palabras("Hola buenos dias, todo bien"))
print(existe_palabra("Pera", "texto.txt"))

clonar_sin_comentarios("texto_entrada.txt", "texto_salida.txt")
invertir_lineas("texto.txt")

agregar_frase_al_final("agregar_final.txt", "Buenos dias")

agregar_frase_al_principio("agregar_final.txt", "Buenos dias")




print(listar_palabras_de_archivo("texto.txt"))