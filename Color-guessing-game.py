# Diego Pérez Hidalgo
# A01704746
import random


def pasoA():
    instrucciones = """\n1. El juego genera un código aleatorio de 4 colores y se asignan a cada una de las posiciones secretas del tablero.
2. Se le presentan al jugador 10 intentos (uno a la vez) para adivinar qué colores se encuentran en cada una de las 4 posiciones secretas.
3. En cada intento, después de que el jugador selecciona los colores para cada posición secreta, el programa proporcionará información sobre si los colores son los correctos y si están o no en la posición correcta.
4. El jugador ganará solamente si adivina los 4 colores en sus lugares correctos antes de que se terminen las 10 oportunidades disponibles. En caso contrario, el jugador habrá perdido.

"""
    correr_instrucciones = input('\nDesea ver las instrucciones? (Do you want to see the instructions-- si or no): ')
    correr_instrucciones = correr_instrucciones.lower()
    while correr_instrucciones != 'si' and correr_instrucciones != 'no':
        correr_instrucciones = input('Favor escribir si o no (write si or no): ')
        correr_instrucciones = correr_instrucciones.lower()
    if correr_instrucciones == 'si':
        print(instrucciones)
        
    modelo_de_juego = input("Con cuántos colores desea jugar? (with how many colors do you want to play)(6,7 u 8): ")
    while modelo_de_juego != '7' and modelo_de_juego != '6' and modelo_de_juego != '8':
        modelo_de_juego = input("Por favor ingrese 6,7 u 8: ")
    modelo_de_juego = int(modelo_de_juego)
    colores_elegidos = []
    opciones_colores = ['v','a','n','r','g','b','m','i']
    contador = 1
    print("Los colores disponibles son (the available colors are): \n(V)erde \n(A)zul \n(N)aranja \n(R)ojo \n(G)ris \n(B)lanco \n(M)orado \n(I)ndigo")
    while modelo_de_juego != 0:
        que_color = input(f'\nElija el color {contador}: las opciones restantes son (the remaining options are) {opciones_colores}: ')
        que_color = que_color.lower()
        while que_color not in opciones_colores:
            que_color = input(f'Por favor seleccione una de las opciones disponibles (select an available option){opciones_colores}: ')
            que_color = que_color.lower()
        colores_elegidos.append(que_color)
        opciones_colores.remove(que_color)
        modelo_de_juego -= 1
        contador += 1
    return colores_elegidos


def pasoB():
    print('\nSeleccionar la dificultad del juego (choose diffiuclty):')
    print("Fácil - Los colores no se repiten. (seleccione 'F') \nIntermedio - Los colores pueden repetirse. (seleccione 'I') \nAvanzado - Los colores pueden repetirse y existe la posibilidad de que una de las casillas esté vacía. (seleccione 'A') ")
    dificultad_select = input('\nDifficultad: ')
    dificultad_select = dificultad_select.lower()
    while dificultad_select != 'f' and dificultad_select != 'i' and  dificultad_select != 'a':
        dificultad_select = input('Seleccionar uno de los valores acceptables (input a correct letter)(F, I o A): ')
        dificultad_select = dificultad_select.lower()
    if dificultad_select == 'f':
        dificultad = 1
    elif dificultad_select == 'i':
        dificultad = 2
    elif dificultad_select == 'a':
        dificultad = 3
    return dificultad
        

def pasoC():
    print('\nSeleccionar modo de juego (select game mode) ((D)eveloper, y modo (N)ormal): ')
    modo_juego = input('Modo: ')
    modo_juego = modo_juego.lower()
    while modo_juego != 'd' and modo_juego != 'n':
        modo_juego = input('Seleccionar uno de los valores acceptables(input a correct letter) (D o N): ')
        modo_juego = modo_juego.lower()
    if modo_juego == 'd':
        modo = 1
    elif modo_juego == 'n':
        modo = 2
    print()
    return modo
    

def proceso_paso_D_E_F(colores, dificultad, modo_juego):
    contador_intento = 1
    cuantos_colores = len(colores)
    random_colors = []
    if dificultad == 1:
        'Los colores no se repiten'
        colores_dificultad = colores
        for ciclo in range(4):
            color_elected = colores_dificultad[random.randint(0, len(colores) - 1)]
            while color_elected in random_colors:
                color_elected = colores[random.randint(0, len(colores) - 1)]
            random_colors += color_elected
    elif dificultad == 2:
        'Los colores pueden repetirse'
        colores_dificultad = colores*2
        for ciclo in range(4):
            color_elected = colores_dificultad[random.randint(0, len(colores_dificultad) - 1)]
            random_colors += color_elected
    elif dificultad == 3:
        'Los colores pueden repetirse y existe la posibilidad de que una de las casillas esté vacía.'
        colores_dificultad = colores*2
        colores_dificultad.append(' ')
        for ciclo in range(4):
            color_elected = colores_dificultad[random.randint(0, len(colores_dificultad) - 1)]
            random_colors += color_elected
    string_de_colores = ''
    for cuantos in range(cuantos_colores):
        string_de_colores += f'{colores[cuantos]} '
    string_de_colores = string_de_colores.upper()
    developer_mode = 'X X X X'
    if modo_juego == 1:
        developer_mode = random_colors
    matrix_resultados = []
    contador_print = 1
    para_romper = ['=', '=', '=', '=']
    resultado_final = []
    while contador_intento != 11 and resultado_final != para_romper:
        resultado = []
        lista_intento = []
        for mini_contador in range(4):
            adivina_color = input(f'¿Cuál es el color (What is the color) {mini_contador+1} - {string_de_colores}? ')
            adivina_color = adivina_color.lower()
            while adivina_color not in colores_dificultad:
                adivina_color = input(f'Por favor seleccione una de las opciones disponibles (select one of the available options) {colores}: ')
                adivina_color = adivina_color.lower()
            lista_intento += adivina_color
        for mini_contador2 in range(4):
            if lista_intento[mini_contador2] == random_colors[mini_contador2]:
                valor = '='
            elif lista_intento[mini_contador2] in random_colors:
                valor = '+'
            elif lista_intento[mini_contador2] not in random_colors:
                valor = '-'
            resultado += valor
        resultado_final = resultado
        intentos_matriz_lista = ''
        correctos_o_incorrectos = ''
        for ciclo in range(4):
            intentos_matriz_lista += f'{lista_intento[ciclo]} '
            intentos_matriz_lista = intentos_matriz_lista.upper()
            correctos_o_incorrectos += f'{resultado[ciclo]} '
            correctos_o_incorrectos = correctos_o_incorrectos.upper()
        matrix_resultados += [[intentos_matriz_lista, correctos_o_incorrectos]]
        for ciclo in range(contador_print):
            print(f'Intento (Try) {ciclo+1}: {developer_mode} - {matrix_resultados[ciclo][0]} -> {matrix_resultados[ciclo][1]}')
        contador_intento += 1
        contador_print += 1
        print()
    return contador_intento


def salida(contador):
    if contador == 11:
        print('Game Over')
    elif contador < 11:
        print('Felicidades, Ganaste! (You won)')
    volver_a_jugar = input('\nDesea volver a jugar? (Play again): ')
    volver_a_jugar = volver_a_jugar.lower()
    while volver_a_jugar != 'si' and volver_a_jugar != 'no':
        volver_a_jugar = input('Favor escribir si o no (write si or no): ')
        volver_a_jugar = volver_a_jugar.lower()
    return volver_a_jugar
    
    
def volver_a_jugar(jugar):
    if jugar == 'si':
        color = pasoA()
        dif = pasoB()
        mode = pasoC()
        cont = proceso_paso_D_E_F(color, dif, mode)
        jugar_denuevo = salida(cont)
        volver_a_jugar(jugar_denuevo)

    

color = pasoA()
dif = pasoB()
mode = pasoC()
cont = proceso_paso_D_E_F(color, dif, mode)
jugar_denuevo = salida(cont)
volver_a_jugar(jugar_denuevo)


# caso de prueba 1: Entradas: instrucciones: no,  colores: 6,  opciones: v, a, r, g, n, b,  dificultad: a,  modo: d,   color1? v, color2? a, color1? r, color1? g
#                   Salida: Intento 1: ['n', 'n', 'n', ' '] - V A R G  -> - - - -
#                   Entradas2: color1? n, color2? n, color1? n, color1?
#                   Salida: Intento 1: ['n', 'n', 'n', ' '] - V A R G  -> - - - -, Intento 2: ['n', 'n', 'n', ' '] - N N N    -> = = = =
#                   Salida: Felicidades, Ganaste!, Desea volver a jugar?
#                   Entrada3: no

# caso de prueba 2: Entradas: instrucciones: no,  colores: 7,  opciones: i, m, g, r, a, n, v  dificultad: f,  modo: n,   color1? i, color2? m, color1? g, color1? r
#                   Salida: Intento 1: X X X X - I M G R  -> - - + + 
#                   Entradas2: color1? a, color2? g, color1? r, color1? n
#                   Salida: Intento 1: ['v', 'b', 'i', 'm'] - B V A G  -> + + - - , Intento 2: X X X X - A G R N  -> + = + - 
#                   Entradas2: color1? r, color2? g, color1? a, color1? v
#                   Salida: Intento 1: ['v', 'b', 'i', 'm'] - B V A G  -> + + - - , Intento 2: X X X X - A G R N  -> + = + -, Intento 3: X X X X - R G A V  -> = = = = 
#                   Salida: Felicidades, Ganaste!, Desea volver a jugar?
#                   Entrada3: si
#                   -Programa repeat-