import os
def votoRepublicano():
    print('Voto partido republicano')
    input('Presione "ENTER" para continuar')
    os.system('cls')

def votoDemocrata():
    print('Voto partido democrata')
    input('Presione "ENTER" para continuar')
    os.system('cls')

def contarVotos(cont_republicano,cont_democrata):
    print('Totalización de los votos')
    print(f'Total de votos Republicanos: {cont_republicano}')
    print(f'Total de votos Demócratas: {cont_democrata}')
    print(f'Cantidad total de votos: {cont_republicano+cont_democrata}')
    input('Presione "ENTER" para continuar')
    os.system('cls')

opcion =0
cont_republicano = 0
cont_democrata = 0

while opcion !=4:
    print('\t*** MENU ***')
    print('=====================')
    print('[1] -> Partido Republicano')
    print('[2] -> Partido Demócrata')
    print('[3] -> Totalización de Votos')
    print('[4] -> Salir del Sistema')
    print('=====================')
    opcion=int(input('Ingrese opción: '))

    if opcion==1:
        cont_republicano+=1
        votoRepublicano()
    if opcion==2:
        cont_democrata+=1
        votoDemocrata()
    if opcion==3:
        contarVotos(cont_republicano,cont_democrata)
    if opcion==4:
        print('Saliendo de sistema de votación...')
    

