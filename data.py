def num_words(args): #funcion que da cantidad de palabras
    words = args.split()
    quantity = len(words)
    return quantity


class Homework: #Clase Padre - se usará más adelante para el gestor
    def __init__(self):
        self.name = ''
        self.description = ''
        self.priority = ''

    def get_all(self): #Me muestra toda la info de la tarea y valida si hay algo que mostrar o no
        if self.name != '' and self.description != '' and self.priority != '':
            return f'''
                ☃︎{self.name}
                    ({self.description})
                PRIORIDAD {self.priority.upper()}
            '''
        else:
            print('No hay nada que mostrar!')

    def set_name(self, name):#Cambia nombre y valida si mantiene limite de palabras
        if num_words(name) < 5:
            self.name = name
            return self.name
        else:
            print('Límite es de 4 palabras!!')

    def set_description(self, description):#Cambia descripcion y valida si mantiene limite de palabras
        if num_words(description) < 15:
            self.description = description
            return self.description
        else:
            print('Límite es de 14 palabras!!')

    def set_priority(self, priority):#Valida la prioridad
        if priority.lower() == 'alta':
            self.priority = priority.upper()
            return self.priority
        elif priority.lower() == 'media':
            self.priority = priority.upper()
            return self.priority
        elif priority.lower() == 'baja':
            self.priority = priority.upper()
            return self.priority
        else:
            print('Valor no Válido')

class M_Homework(Homework):#Clase de gestion de tarea - hereda la clase homework
    def save(self, priority, titule = input('Nombre de archivo : ')): # guardar(crear) archivo con tarea inicial
        titule += '.txt'
        arch = open(f'file/{titule}', 'w')
        arch.write(f'[☺︎ {self.set_name(name = input('Ingresa nombre de tarea : '))} (PENDIENTE)')
        arch.close()
        arch = open(f'file/{titule}', 'a')
        arch.write(f'\n     ({self.set_description(description = input('Ingrese descripcion'))})')
        arch.close()
        arch = open(f'file/{titule}', 'a')
        arch.write(f'\n      PRIORIDAD {self.set_priority(priority)}]\n----------------------------------------')
        arch.close()


#nota mental - la validacion de prioridad habria que hacerlo con fecha, comparar fecha de tarea por hacer con la fecha actual
#y segun los dias que falten por hacerla poner su prioridad, tipo si es en 3 dias que hay que terminar la tarea que sea ALTA
#entonces dependiendo eso, reestructurar save en la parte prioridad
#modificar set priority en la clase padre, para que pida fecha y compare con la actual para luego tomarlo con validar prioridad y usarlo en save, pilas!!
x = M_Homework()








