import math

# Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo")

def imprimir_un_verso():
    print("Este es un verso\nEste es otro")

def raizDe2()->float:
    return round(2**(1/2), 4)

def factorial_de_dos()->int:
    return 2

def perimetro()->float:
    return 2*(math.pi)


# Ejercicio 2
def imprimir_saludo(nombre:int):
    print(f"Hola {nombre}")

def raiz_cuadrada_de(numero:float)->float:
    return numero**(1/2)

def fahrenheit_a_celsius(temperatura:float)->float:
    return (temperatura-32)*(5/9)

def imprimir_dos_veces(estribillo:str):
    print(estribillo + "\n" + estribillo)

def es_multiplo_de(n:int, m:int)->bool:
    return (n % m) == 0

def es_par(numero:int)->bool:
    return es_multiplo_de(numero, 2)

def cantidad_de_pizzas(comensales:int, min_cant_de_porciones:int)->int:
    porciones_totales:int = comensales * min_cant_de_porciones
    return math.ceil(porciones_totales/8)


# Ejercicio 3
def alguno_es_0(numero1:float, numero2:float)->bool:
    return (numero1 == 0) or (numero2 == 0)

def ambos_son_0(numero1:float, numero2:float)->bool:
    return (numero1 == 0) and (numero2 == 0)

def es_nombre_largo(nombre:str)->bool:
    return 3 <= len(nombre) <= 8

def es_bisiesto(año:int)->bool:
    return es_multiplo_de(año, 400) or (es_multiplo_de(año, 4) and not es_multiplo_de(año, 100))


# Ejercicio 4
def peso_pino(altura_en_m:float)->float:
    altura_en_cm:float = altura_en_m * 100 
    peso:float
    if (altura_en_cm > 300):
        peso = 300*3 + ((altura_en_cm-300) * 2)
    else:
        peso = altura_en_cm * 3
    return peso

def es_peso_util(peso:float)->bool:
    return 400 <= peso <= 1000

def sirve_pino(altura_en_m:float)->float:
    return es_peso_util(peso_pino(altura_en_m))


# Ejercicio 5
def devolver_el_doble_si_es_par(numero:int)->int:
    if (es_par(numero)):
        return numero*2
    else:
        return numero
    
def devolver_valor_si_es_par_sino_el_que_sigue(numero:int)->int:
    if (es_par(numero)):
        return numero
    else:
        return numero+1

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero:int)->int:
    if (es_multiplo_de(numero, 9)):
        return numero*3
    elif (es_multiplo_de(numero, 3)):
        return numero*2
    else:
        return numero

def lindo_nombre(nombre:str)->str:
    if (len(nombre) >= 5):
        return "Tu nombre tiene muchas letras!"
    else:
        return "Tu nombre tiene menos de 5 caracteres"
    
def elRango(numero:float):
    if (numero < 5):
        print("Menor a 5")
    elif (10 <= numero <= 20):
        print("Entre 10 y 20")
    elif (numero > 20):
        print("Mayor a 20")
    else:
        print("Fuera de la especificación")
    # entre 5 y 10 no está especificado

def trabaja_o_estudia_en_base_al_sexo_y_la_edad(sexo:str, edad:int):
    if (edad < 18):
        print("Andá de vacaciones")
    else:
        if (sexo == "M"):
            if (edad < 65):
                print("Andá de vacaciones")
            else:
                print("Te toca trabajar") 
        elif (sexo == "F"):
            if (edad < 60):
                print("Andá de vacaciones")
            else:
                print("Te toca trabajar") 

        
# Ejercicio 6
def numeros_del_1_al_10():
    i:int = 1
    while (i <= 10):
        print(i)
        i += 1

def numeros_pares_del_10_al_40():
    i:int = 10
    while (i <= 40):
        print(i)
        i += 2

def eco_10_veces():
    i:int = 1
    while (i <= 10):
        print("eco")
        i += 1

def cuenta_regresiva(valor_inicial:int):
    while (valor_inicial > 0):
        print(valor_inicial)
        valor_inicial -= 1
    print("Despegue")

def monitoreo_de_viaje_en_el_tiempo(año_de_partida:int, año_de_llegada:int):
    while (año_de_partida > año_de_llegada):
        año_de_partida -= 1
        print(f"Viajó un año al pasado, estamos en el año: {año_de_partida}")

def nuevo_monitoreo_de_viaje_en_el_tiempo(año_de_partida:int):
    while (año_de_partida > -384):
        año_de_partida -= 20
        if ((año_de_partida < -384) and abs(año_de_partida+384) > abs(año_de_partida+404)): break
        print(f"Viajó un año al pasado, estamos en el año: {año_de_partida}")


# Ejercicio 7
def for_numeros_del_1_al_10():
    i:int 
    for i in range(1,11):
        print(i)

def for_numeros_pares_del_10_al_40():
    for i in range(10, 41, 2):
        print(i)

def for_eco_10_veces():
    for i in range(10):
        print("eco")

def for_cuenta_regresiva(valor_inicial:int):
    for i in range(valor_inicial, 0, -1):
        print(i)
    print("Despegue")

def for_monitoreo_de_viaje_en_el_tiempo(año_de_partida:int, año_de_llegada:int):
    for i in range(año_de_partida, año_de_llegada, -1):
        print(f"Viajó un año al pasado, estamos en el año: {i-1}")

def for_nuevo_monitoreo_de_viaje_en_el_tiempo(año_de_partida:int):
    for i in range(año_de_partida, -385, -20):
        if ((i < -384) and abs(i+384) > abs(i+404)): break
        print(f"Viajó un año al pasado, estamos en el año: {i}")






# Ejecucion de prueba

imprimir_hola_mundo()
imprimir_un_verso()
print(raizDe2())
print(factorial_de_dos())
print(perimetro())

imprimir_saludo("Facundo")
print(raiz_cuadrada_de(5))
print(fahrenheit_a_celsius(100))
imprimir_dos_veces("Te para tres")
print(es_multiplo_de(4,2))
print(es_par(6))
print(cantidad_de_pizzas(5, 3))

print(alguno_es_0(5,0))
print(ambos_son_0(5,0))
print(es_nombre_largo("Facundo"))
print(es_bisiesto(1900))

print(peso_pino(2))
print(peso_pino(5))
print(es_peso_util(600))
print(sirve_pino(5))

print(devolver_el_doble_si_es_par(8))
print(devolver_el_doble_si_es_par(7))
print(devolver_valor_si_es_par_sino_el_que_sigue(8))
print(devolver_valor_si_es_par_sino_el_que_sigue(7))
print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(27))
print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(6))
print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(11))
print(lindo_nombre("sdsdgfhgfhj"))
print(lindo_nombre("abc"))
elRango(5)
elRango(7)
elRango(12)
elRango(25)
trabaja_o_estudia_en_base_al_sexo_y_la_edad("M", 16)
trabaja_o_estudia_en_base_al_sexo_y_la_edad("M", 35)
trabaja_o_estudia_en_base_al_sexo_y_la_edad("M", 62)
trabaja_o_estudia_en_base_al_sexo_y_la_edad("M", 70)
trabaja_o_estudia_en_base_al_sexo_y_la_edad("F", 16)
trabaja_o_estudia_en_base_al_sexo_y_la_edad("F", 35)
trabaja_o_estudia_en_base_al_sexo_y_la_edad("F", 62)
trabaja_o_estudia_en_base_al_sexo_y_la_edad("F", 70)

numeros_del_1_al_10()
numeros_pares_del_10_al_40()
eco_10_veces()
cuenta_regresiva(10)
monitoreo_de_viaje_en_el_tiempo(2100, 2095)
nuevo_monitoreo_de_viaje_en_el_tiempo(100)

for_numeros_del_1_al_10()
for_numeros_pares_del_10_al_40()
for_eco_10_veces()
for_cuenta_regresiva(10)
for_monitoreo_de_viaje_en_el_tiempo(2100, 2095)
for_nuevo_monitoreo_de_viaje_en_el_tiempo(100)
