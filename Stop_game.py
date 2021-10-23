import random
import string
import csv


class StopGame:

        def __init__(self):
            self.char = random.choice(string.ascii_uppercase)
            self.csv_paises = './Recursos/paises.csv'
            self.csv_nombres_hombre = './Recursos/nombres-hombre.csv'
            self.csv_nombres_mujer = './Recursos/nombres-mujer.csv'
            pass



        def char(self):
            self.char = random.choice(string.ascii_uppercase)


        def username(self):
            '''pregunta y establece nombre al usuario'''

            name = input('Por favor, escribe tu nombre: ')

            print(f'''{name}, bienvenid@ al juego STOP.
            --------------------------------------------
            El objetivo del  juego es escribir 
            una palabra que comience por la letra [{self.char}] 
            en las categorias que se te indicarán 
            a continuación, en el menor tiempo posible.
            --------------------------------------------''')

            input('Presiona ENTER para comenzar el juego!!!\n\n')


        def revision(self, x, csv_file):
            with open(csv_file, 'r', encoding='utf8') as f:
                reader = csv.reader(f, delimiter=',')
                rev_list = []
                for row in reader:
                    for field in row:
                        rev_list.append(field)
                if x in rev_list:
                    if x.startswith(self.char):
                        print(f'¡¡¡CORRECTO!!!', x, 'está en la lista y empieza por', self.char)
                    else:
                        print(f'Lo siento', x, 'no empieza por', self.char)
                elif x is not rev_list:
                    print(f'Lo siento {x}  empieza por {self.char}, pero no está en la lista :(')


        def juego(self):

            self.username()
            self.pais = input(f'Escribe el nombre de un país que comience por la letra {self.char}: ')
            self.revision(self.pais, self.csv_paises)
            self.nombre_hombre = input(f'Escribe un nombre masculino que comience por la letra {self.char}: ')
            self.revision(self.nombre_hombre, self.csv_nombres_hombre)
            self.nombre_mujer = input(f'Escribe un nombre femenino que comience por la letra {self.char}: ')
            self.revision(self.nombre_mujer, self.csv_nombres_mujer)


def main():
    while True:
        partida = StopGame()
        partida.juego()

        seguir = input('Si desea otra partida escriba STOP y pulse Enter :')
        if seguir != 'STOP':
            break



if __name__ == '__main__':
    main()

