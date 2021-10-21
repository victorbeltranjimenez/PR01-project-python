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

        #def data(self):

            #self.csv_paises = './Recursos/paises.csv'
            #self.csv_nombres_hombre = './Recursos/nombres-hombre.csv'
            #self.csv_nombres_mujer = './Recursos/nombres-mujer.csv'
            #self.pais = input(f'Escribe el nombre de un país que comience por la letra {self.char}: ')
            #self.revision(self.pais, self.csv_paises)
            #self.nombre_hombre = input(f'Escribe un nombre masculino que comience por la letra {self.char}: ')
            #self.revision(self.nombre_hombre, self.csv_nombres_hombre)
            #self.nombre_mujer = input(f'Escribe un nombre femenino que comience por la letra {self.char}: ')
            #self.revision(self.nombre_mujer, self.csv_nombres_mujer)

        def char(self):
            self.char = random.choice(string.ascii_uppercase)


        def username(self):
            '''pregunta y establece nombre al usuario'''

            name = input('Por favor, escribe tu nombre: ')

            print(f'{name}, bienvenid@ al juego STOP.\n--------------------------------------------\nEl objetivo del  juego es escribir \nuna palabra que comience por la letra [{self.char}] \nen las categorias que se te indicarán \na continuación, en el menor tiempo posible.\n--------------------------------------------')

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
                    print(f'Lo siento', x, 'empieza por, {self.char}, pero no está en la lista :(')


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



if __name__ == '__main__':
    main()

