
import random
import string
import csv

csv_paises = './Recursos/paises.csv'
csv_nombres_hombre = './Recursos/nombres-hombre.csv'
csv_nombres_mujer = './Recursos/nombres-mujer.csv'




char = random.choice(string.ascii_uppercase)


def username():
    '''pregunta y establece nombre al usuario'''
    name = input('Por favor, escribe tu nombre: ')

    print(f'{name}, bienvenid@ al juego STOP.\n--------------------------------------------\nEl objetivo del  juego es escribir \nuna palabra que comience por la letra [{char}] \nen las categorias que se te indicarán \na continuación, en el menor tiempo posible.\n--------------------------------------------')

    input('Presiona ENTER para comenzar el juego!!!\n\n')


def revision(x, csv_file):
    with open(csv_file, 'r', encoding='utf8') as f:
        reader = csv.reader(f, delimiter=',')
        rev_list = []
        for row in reader:
            for field in row:
                rev_list.append(field)
        if x in rev_list:
            if x.startswith(char):
                print(f'¡¡¡CORRECTO!!!', x, 'está en la lista y empieza por', char)
            else:
                print(f'Lo siento', x, 'no empieza por', char)
        elif x is not rev_list:
            print(f'Lo siento', x, 'empieza por', char, 'pero no está en la lista :(')



username()
pais = input(f'Escribe el nombre de un país que comience por la letra {char}: ')
revision(pais, csv_paises)
nombre_hombre = input(f'Escribe un nombre masculino que comience por la letra {char}: ')
revision(nombre_hombre, csv_nombres_hombre)
nombre_mujer = input(f'Escribe un nombre femenino que comience por la letra {char}: ')
revision(nombre_mujer, csv_nombres_mujer)



