# Importación de módulos
import random

# Valores de piedra, papel o tijera
r = 'piedra'
p = 'papel'
s = 'tijera'

# Diccionario de piedra papel o tijera
rps = {
    '1' : r,
    '2' : p,
    '3': s
}

#Marcador del juego
mi_score = 0
npc_score = 0

while True:
    # Presentación del juego
    print('--------------- Piedra, Papel o Tijera ---------------')

    #Publicación del score
    print('Score:')
    print('Tú: ' + str(mi_score))
    print('NPC ' + str(npc_score))
    print('------------------------------------------------------')

    #print('Elige una opción')
    print('1: Piedra')
    print('2: Papel')
    print('3: Tijera')

    # Decisión del jugador de piedra, papel o tijera
    # Hace falta la correción para valores incorrectos
    eleccion_jugador = input('Elige un número del 1 al 3: ')
    print('------------------------------------------------------')

    #Creación del filtro
    if eleccion_jugador not in rps:
        print('Opción no valida. Elige un número válido')
        continue    
    
    #Decisión NPC
    eleccion_npc = str(random.randint(1,3))
    #eleccion_npc = '3'
    # Declaración de tu opción y la del NPC
    print('¡Elegiste ' + rps[eleccion_jugador] + '!')
    print('¡NPC eligió ' + rps[eleccion_npc] + '!')

    # Condiciones de ganar, perder, empate (Orden: Jugador vs NPC)

    # Empate
    if eleccion_jugador == eleccion_npc:
        print('¡Empate!')

    # Gana jugador
        # Piedra vs Tijera
        # Tijera vs Papel
        # Papel vs Piedra
    elif (eleccion_jugador == '1' and eleccion_npc == '3') or \
        (eleccion_jugador == '3' and eleccion_npc == '2') or \
        (eleccion_jugador == '2' and eleccion_npc == '1'):
        print('¡Ganaste')
        # Suma un punto al jugador
        mi_score += 1

    # Gana NPC (pierde jugador)
        # Tijera vs Piedra
        # Piedra vs Papel
        # Papel vs Tijera
    else:
        print('Perdiste...')
        # Suma un punto al NPC
        npc_score += 1

    # Pregunta de continuar juego 
    print('------------------------------------------------------')
    print('¿Otra vez?')
    print('1: Sí')
    print('Otro: No')
    continuar_juego = input('Elige un número: ')
    if continuar_juego != '1':
        print('------------------------------------------------------') 
        print('Final Score:')
        print('Tú: ' + str(mi_score))
        print('NPC ' + str(npc_score))
        print('------------------------------------------------------')
        break


