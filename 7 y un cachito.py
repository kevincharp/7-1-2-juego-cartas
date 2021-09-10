# Bibliotecas
import random
from random import choice

# Variables
limitejugador = 7.5
limitebanca = 7
puntajejugador = 0
puntajebanca = 0
poso = 100
partidajugada = 10
gana = 20
puntaje = 0
win = 'GANASTE 20 estrellas de cobre'
lose = 'PERDISTE CAMPEON intenta de nuevo'


print('---------------BIENVENIDO A 7 y UN CACHITO--------------- \n\n\n')

print('--->  Usted tiene', poso,'estrellas de cobre \n\nPara entrar al juego debe gastar 10 monedas de cobre\n')

print('----¿Quiere jugar?----')
print('1.Si  2.No')
play = int(input())
if play > 2:
    print('')
    print('Opcion incorrecta\n')
    print('----¿Quiere jugar?----')
    print('1.Si  2.No')
    play = int(input())
    print('')
    
elif play == 1:
    print('La banca reparte \n')
    carta  = (choice([i for i in range(1, 12) if i not in [8, 9]]))
    # CARTAS DEL JUGADOR // Se entra en el while y el usuario decide si pedir carta o plantarse
    while puntajejugador <= limitejugador or respuesta == 2:
        print('')
        print('1.Pedir carta   ')
        print('2.Plantarse     ')
        respuesta = int(input())
        while respuesta > 2:
            print('')
            print('Opcion incorrecta\n')
            print('1.Pedir carta   ')
            print('2.Plantarse     ')
            respuesta = int(input())
        if respuesta == 1:
            carta  = (choice([i for i in range(1, 12) if i not in [8, 9]]))
            if carta  == 1:
                print('Tu carta es ', carta )
                puntaje = 1
                puntajejugador = puntajejugador + puntaje
                print('Puntaje:', puntajejugador)
            if carta  == 2:
                print('Tu carta es ', carta )
                puntaje = 2
                puntajejugador = puntajejugador + puntaje
                print('Puntaje:', puntajejugador)
            if carta  == 3:
                print('Tu carta es ', carta )
                puntaje = 3
                puntajejugador = puntajejugador + puntaje
                print('Puntaje:', puntajejugador)
            if carta  == 4:
                print('Tu carta es ', carta )
                puntaje = 4
                puntajejugador = puntajejugador + puntaje
                print('Puntaje:', puntajejugador)
            if carta  == 5:
                print('Tu carta es ', carta )
                puntaje = 5
                puntajejugador = puntajejugador + puntaje
                print('Puntaje:', puntajejugador)
            if carta  == 6:
                print('Tu carta es ', carta )
                puntaje = 6
                puntajejugador = puntajejugador + puntaje
                print('Puntaje:', puntajejugador)
            if carta  == 7:
                print('Tu carta es ', carta )
                puntaje = 7
                puntajejugador = puntajejugador + puntaje
                print('Puntaje:', puntajejugador)
            if carta  == 10 or carta  == 11 or carta  == 12:
                print('Tu carta es ', carta )
                puntaje = 0.5
                puntajejugador = puntajejugador + puntaje
                print('Puntaje:', puntajejugador)
            if puntajejugador > limitejugador:
                print('Te pasaste de 7.5\n', )
                break
        elif respuesta == 2:
            print('Puntaje:', puntajejugador, '\n')
            print('')
            break
    print('--------------------------------Ahora le toca a la BANCA--------------------------------')
    input('Enter para continuar...')
    print('Las cartas de la banca son: \n')
    # CARTAS DE LA BANCA // Banca pide cartas si llega a 7 se planta
    while puntajebanca < limitebanca:
        carta  = (choice([i for i in range(1, 12) if i not in [8, 9]]))
        if carta  == 1:
            print('Carta: ', carta , '\n')
            puntaje = 1
            puntajebanca = puntajebanca + puntaje
            print('Puntaje:', puntajebanca, '\n')
        elif carta  == 2:
            print('Carta: ', carta , '\n')
            puntaje = 2
            puntajebanca = puntajebanca + puntaje
            print('Puntaje:', puntajebanca, '\n')
        elif carta  == 3:
            print('Carta: ', carta , '\n')
            puntaje = 3
            puntajebanca = puntajebanca + puntaje
            print('Puntaje:', puntajebanca, '\n')
        elif carta  == 4:
            print('Carta: ', carta , '\n')
            puntaje = 4
            puntajebanca = puntajebanca + puntaje
            print('Puntaje:', puntajebanca, '\n')
        elif carta  == 5:
            print('Carta: ', carta , '\n')
            puntaje = 5
            puntajebanca = puntajebanca + puntaje
            print('Puntaje:', puntajebanca, '\n')
        elif carta  == 6:
            print('Carta: ', carta , '\n')
            puntaje = 6
            puntajebanca = puntajebanca + puntaje
            print('Puntaje:', puntajebanca, '\n')
        elif carta  == 7:
            print('Carta: ', carta , '\n')
            puntaje = 7
            puntajebanca = puntajebanca + puntaje
            print('Puntaje:', puntajebanca, '\n')
        elif carta  == 10 or carta  == 11 or carta  == 12:
            print('Carta: ', carta , '\n')
            puntaje = 0.5
            puntajebanca = puntajebanca + puntaje
            print('Puntaje:', puntajebanca, '\n')
        elif puntajebanca == 7:
            break
    poso = 100 - partidajugada
    if puntajebanca == limitebanca and puntajebanca == puntajejugador:
        print('La banca se planta su puntaje es: ', puntajebanca)
        print('')
        posoacum = poso - partidajugada
        print(lose)
        print('')
    elif puntajebanca <= limitejugador and puntajebanca >= puntajejugador:
        print(lose)
        posoacum = poso - partidajugada
        print('')
    elif puntajejugador > limitejugador and puntajebanca > limitejugador:
        posoacum = poso - partidajugada
        print('Te pasaste de 7.5 pero la banca tambien')
        print('No ganaste nada pero tampoco te devolvemos tu dinero\n')
    elif puntajebanca < puntajejugador and puntajejugador <= limitejugador:
        print(win)
        posoacum = poso + gana
        print('Riqueza ', posoacum)
        print('')
    elif puntajebanca > limitebanca:
        print('La banca se paso de 7.5 ', win)
        posoacum = poso + gana
        print('Riqueza ', posoacum)
        print('')
        print('')
        
print('¿Queres revancha?')
respuesta = revancha (int(input('1.Si 2.No\n')))
            