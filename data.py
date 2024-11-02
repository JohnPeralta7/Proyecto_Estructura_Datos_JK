import os
from datetime import datetime
now = datetime.now()
def num_words(args): #funcion que da cantidad de palabras
    words = args.split()
    quantity = len(words)
    return quantity

def t_day(): #Funcion que da fecha actual, la convierte en string y luego la almacena en array
    today = str(now.date())
    x = today.split('-')
    return x

#(2024-10-26) == '2024-10-26'


class Homework: #Clase Padre - se usará más adelante para el gestor
    def __init__(self):
        self.archive = ''
        self.name = ''
        self.description = ''
        self.date = ''
        self.number = 0

    def get_archive(self):
        return self.archive

    def get_number(self):
        return self.number

    def set_number(self):
        self.number += 1
        return self.number

    def set_archive(self, name):
        array = name.split(' ')
        array.append('.txt')
        name_archive = ''
        for i in range(len(array)):
            name_archive += array[i]
        self.archive = name_archive
        return self.archive



    def set_name(self):#Cambia nombre y valida si mantiene limite de palabras
        while True:
            name = input('Ingresa nombre de tarea : ')
            if num_words(name) < 5:
                self.name = name
                return self.name
            else:
                print('Límite es de 4 palabras!!')


    def set_description(self):#Cambia descripcion y valida si mantiene limite de palabras
        while True:
            description = input('Ingrese descripcion : ')
            if num_words(description) < 15:
                self.description = description
                return self.description
            else:
                print('Límite es de 14 palabras!!')

    def set_date(self):#Pide fecha al usuario y la compara con la fecha actual
        date = []
        while True:
            try:
                year = int(input('Ingresa el año : '))
                if year > 0:
                    date.append(year)
                    break
                else:
                    print('Ingresa año valido')
            except ValueError:
                print('no xupapi te estas pasando')

        while True:
            try:
                month = int(input('Ingrese el mes : '))
                if 0 < month < 13:
                    date.append(month)
                    break
                else:
                    print('Ingresa un mes valido')
            except ValueError:
                print('Nuh uh, ingresa valor numerico')

        while True:
            try:
                day = int(input('Ingrese el dia : '))
                if 0 < day < 32:
                    date.append(day)
                    break
                else:
                    print('Ingresa un dia valido')
            except ValueError:
                print('Nuh uh, ingresa valor valido')

        tday = t_day() #una funcion que me retorna un array con valores string de la fecha actual
        today = datetime(int(tday[0]), int(tday[1]), int(tday[2]))
        last_day = datetime(date[0], date[1], date[2])
        diference = last_day - today
        remain_days = diference.days #el .days me ayuda a mostrar los dias restante del resto de arriba
        return remain_days


class M_Homework(Homework):#Clase de gestion de tarea - hereda la clase homework

    def priority(self):
        re_days = self.set_date()
        if 0 <= re_days < 5:
            return 'ALTA'
        elif 5 <= re_days < 9:
            return 'MEDIA'
        elif re_days >= 9:
            return 'BAJA'
        else:
            print('Loco esa vaina no existe')
            return 'CADUCADO'



    def save(self): # guardar(crear) archivo con tarea inicial
        titule = self.set_archive(input('Ingrese nombre de archivo : '))
        arch = open(f'file/{titule}', 'w', encoding="utf-8")
        arch.write(f'[{self.set_number()}︎ {self.set_name()} (PENDIENTE)')
        arch.close()
        arch = open(f'file/{titule}', 'a')
        arch.write(f'\n     ({self.set_description()})')
        arch.close()
        arch = open(f'file/{titule}', 'a')
        arch.write(f'\n     PRIORIDAD {self.priority()}\n-------------------------------------')
        arch.close()

    def add(self):
        archive = self.get_archive()
        new = open(f'file/{archive}', 'a', encoding="utf-8")
        new.write(f'\n[{self.set_number()} ☺︎ {self.set_name()} (PENDIENTE)')
        new.close()
        new = open(f'file/{archive}', 'a', encoding="utf-8")
        new.write(f'\n     ({self.set_description()})')
        new.close()
        new = open(f'file/{archive}', 'a', encoding="utf-8")
        new.write(f'\n     PRIORIDAD {self.priority()}\n-------------------------------------')
        new.close()

    def delete(self):
        archive = self.get_archive()
        with open(f'file/{archive}', 'r', encoding="utf-8") as archivee:
            lines = archivee.readlines()
        while True:
            word = int(input('Ingresa el numero de la tarea que quieras eliminar: '))
            if 1 <= word <= len(lines) // 4:
                break
            else:
                print('Ingrese un numero de tarea existente')
        with open(f'file/{archive}', 'w', encoding="utf-8") as archivee:
            i = 0
            while i < len(lines):
                if (i // 4) + 1 == word:
                    i += 4
                else:
                    archivee.write(lines[i])
                    i += 1

    def show(self):
        archive = self.get_archive()
        show_it = open(f'file/{archive}', 'r', encoding="utf-8")
        print(show_it.read())
        show_it.close()

    def process(self): #cada que el user presiona procesar(interfaz), la tarea cambiara de pend a finalizado
        archive = self.get_archive()
        with open(f'file/{archive}', 'r', encoding="utf-8") as archivee:
            lines = archivee.readlines()
        find = False
        with open(f'file/{archive}', 'w', encoding="utf-8") as archivee:
            for line in lines:
                if '(PENDIENTE)' in line and not find:
                    line = line.replace('(PENDIENTE)', '(FINALIZADO)')
                    find = True
                archivee.write(line)

    def organize(self): #ordenara dependiendo de la fecha de entrega, su prioridad
        archive = self.get_archive()
        category = {'ALTA': [], 'MEDIA' : [], 'BAJA' : [], 'CADUCADO' : []} #se creo un diccionario para ahi almacenar las listas
        with open(f'file/{archive}', 'r', encoding="utf-8") as archivee:
            lines = archivee.readlines()
            for i in range(0, len(lines), 4):
                t = lines[i:i + 4]
                if 'ALTA' in t[2]:
                    category['ALTA'].append(t)
                elif 'MEDIA' in t[2]:
                    category['MEDIA'].append(t)
                elif 'BAJA' in t[2]:
                    category['BAJA'].append(t)
                else:
                    category['CADUCADO'].append(t)
        with open(f'file/{archive}', 'w', encoding="utf-8") as archivee:
            for prio in ['ALTA', 'MEDIA', 'BAJA', 'CADUCADO']:
                for t in category[prio]:
                    archivee.writelines(t)



tyler = M_Homework()
tyler.save()
tyler.add()
tyler.delete()
tyler.show()
tyler.process()
tyler.show()