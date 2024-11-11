import os
from datetime import datetime

now = datetime.now()


def num_words(args):  # función que da cantidad de palabras
    words = args.split()
    quantity = len(words)
    return quantity


def t_day():  # Función que da fecha actual, la convierte en string y luego la almacena en array
    today = str(now.date())
    x = today.split('-')
    return x


def validar_fecha(day, month, year):
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False


class Homework:  # Clase Padre - se usará más adelante para el gestor
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
        name_archive = ''.join(array)
        self.archive = name_archive
        return self.archive

    def set_name(self):  # Cambia nombre y valida si mantiene límite de palabras
        while True:
            name = input('Ingresa nombre de tarea : ')
            if num_words(name) < 5:
                self.name = name
                return self.name
            else:
                print('Límite es de 4 palabras!!')

    def set_description(self):  # Cambia descripción y valida si mantiene límite de palabras
        while True:
            description = input('Ingrese descripción : ')
            if num_words(description) < 15:
                self.description = description
                return self.description
            else:
                print('Límite es de 14 palabras!!')

    def set_date(self):  # Pide fecha al usuario y la compara con la fecha actual
        date = []

        while True:
            try:
                year = int(input('Ingresa el año : '))
                if year > 0:
                    date.append(year)
                    break
                else:
                    print('Ingresa año válido')
            except ValueError:
                print('No, ingresa un número')

        while True:
            try:
                month = int(input('Ingrese el mes : '))
                if 0 < month < 13:
                    date.append(month)
                    break
                else:
                    print('Ingresa un mes válido')
            except ValueError:
                print('Ingresa un valor numérico')

        while True:
            try:
                day = int(input('Ingrese el día : '))
                if validar_fecha(day, date[1], date[0]):
                    date.append(day)
                    break
                else:
                    print('Ingresa un día válido para ese mes')
            except ValueError:
                print('Ingresa un valor numérico')

        tday = t_day()  # Obteniendo la fecha actual en array de strings [year, month, day]
        today = datetime(int(tday[0]), int(tday[1]), int(tday[2]))
        last_day = datetime(date[0], date[1], date[2])
        diference = last_day - today
        remain_days = diference.days
        return remain_days


class M_Homework(Homework):  # Clase de gestión de tarea - hereda la clase Homework

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

    def save(self):  # Guardar (crear) archivo con tarea inicial
        titule = self.set_archive(input('Ingrese nombre de archivo : '))
        with open(f'file/{titule}', 'w', encoding="utf-8") as arch:
            arch.write(f'[{self.set_number()}︎ {self.set_name()} (PENDIENTE)')
            arch.write(f'\n     ({self.set_description()})')
            arch.write(f'\n     PRIORIDAD {self.priority()}\n-------------------------------------')

    def add(self):
        archive = self.get_archive()
        with open(f'file/{archive}', 'a', encoding="utf-8") as new:
            new.write(f'\n[{self.set_number()} ☺︎ {self.set_name()} (PENDIENTE)')
            new.write(f'\n     ({self.set_description()})')
            new.write(f'\n     PRIORIDAD {self.priority()}\n-------------------------------------')

    def delete(self):
        archive = self.get_archive()
        with open(f'file/{archive}', 'r', encoding="utf-8") as archivee:
            lines = archivee.readlines()
        while True:
            word = int(input('Ingresa el número de la tarea que quieras eliminar: '))
            if 1 <= word <= len(lines) // 4:
                break
            else:
                print('Ingrese un número de tarea existente')
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
        with open(f'file/{archive}', 'r', encoding="utf-8") as show_it:
            print(show_it.read())

    def process(self):  # Cambiar de (PENDIENTE) a (FINALIZADO)
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

    def organize(self):  # Ordenar por prioridad
        archive = self.get_archive()
        category = {'ALTA': [], 'MEDIA': [], 'BAJA': [], 'CADUCADO': []}
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


# Creación de una instancia y ejemplo de uso
tyler = M_Homework()
tyler.save()
tyler.add()
tyler.delete()
tyler.show()
tyler.process()
tyler.show()
