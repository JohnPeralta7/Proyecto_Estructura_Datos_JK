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
        self.name = ''
        self.description = ''
        self.date = ''

    def get_all(self): #Me muestra toda la info de la tarea y valida si hay algo que mostrar o no
        if self.name != '' and self.description != '' and self.priority != '':
            return f'''
                ☃︎{self.name}
                    ({self.description})
                PRIORIDAD {self.priority.upper()}
            '''
        else:
            print('No hay nada que mostrar!')

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



    def save(self, titule): # guardar(crear) archivo con tarea inicial
        titule += '.txt'
        arch = open(f'file/{titule}', 'w')
        arch.write(f'[☺︎ {self.set_name()} (PENDIENTE)')
        arch.close()
        arch = open(f'file/{titule}', 'a')
        arch.write(f'\n     ({self.set_description()})')
        arch.close()
        arch = open(f'file/{titule}', 'a')
        arch.write(f'\n     PRIORIDAD {self.priority()}\n-------------------------------------')
        arch.close()


teamo = M_Homework()
teamo.save('teamo_Karencita')
