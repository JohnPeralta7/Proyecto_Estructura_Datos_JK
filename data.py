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
        else:
            print('Límite es de 4 palabras!!')

    def set_description(self, description):#Cambia descripcion y valida si mantiene limite de palabras
        if num_words(description) < 15:
            self.description = description
        else:
            print('Límite es de 14 palabras!!')

    def set_priority(self, priority):#Valida la prioridad
        if priority.lower() == 'alta':
            self.priority = priority.upper()
        elif priority.lower() == 'media':
            self.priority = priority.upper()
        elif priority.lower() == 'baja':
            self.priority = priority.upper()
        else:
            print('Valor no Válido')

