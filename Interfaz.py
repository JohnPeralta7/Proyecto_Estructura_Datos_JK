import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
    QLabel, QMessageBox, QLineEdit, QSpinBox, QDialog, QListWidget, QListWidgetItem
)
from PyQt5.QtCore import Qt
from datetime import datetime, timedelta

# Funciones auxiliares
now = datetime.now()

def num_words(args):
    words = args.split()
    return len(words)

def t_day():
    today = str(now.date())
    x = today.split('-')
    return x

# Clases principales
class Homework:
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
        self.archive = ''.join(array)
        return self.archive

    def set_name(self, name):
        if num_words(name) < 5:
            self.name = name
            return self.name
        else:
            raise ValueError('El límite es de 4 palabras para el nombre de la tarea.')

    def set_description(self, description):
        if num_words(description) < 15:
            self.description = description
            return self.description
        else:
            raise ValueError('El límite es de 14 palabras para la descripción de la tarea.')

    def set_date(self, year, month, day):
        tday = t_day()
        today = datetime(int(tday[0]), int(tday[1]), int(tday[2]))
        last_day = datetime(year, month, day)
        if last_day >= today:
            return (last_day - today).days
        else:
            raise ValueError("La fecha debe ser igual o posterior a la fecha actual.")

class M_Homework(Homework):
    def priority(self, re_days):
        if 0 <= re_days < 5:
            return 'ALTA'
        elif 5 <= re_days < 9:
            return 'MEDIA'
        elif re_days >= 9:
            return 'BAJA'
        else:
            return 'CADUCADO'

    def save(self):
        return f"Tarea '{self.name}' guardada con éxito con prioridad {self.priority(self.date)}."

# Ventana principal para el manejo de tareas
class TaskManagerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tyler = M_Homework()
        self.tasks = []  # Lista para almacenar múltiples tareas
        self.setWindowTitle("Gestor de Tareas")
        self.setGeometry(600, 800, 800, 600)

        # Layout principal
        main_layout = QVBoxLayout()

        # Campos de entrada
        self.archive_input = QLineEdit(self)
        self.archive_input.setPlaceholderText("Nombre del archivo")
        main_layout.addWidget(self.archive_input)

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Nombre de la tarea (máx 4 palabras)")
        main_layout.addWidget(self.name_input)

        self.description_input = QLineEdit(self)
        self.description_input.setPlaceholderText("Descripción de la tarea (máx 14 palabras)")
        main_layout.addWidget(self.description_input)

        # Campos para la fecha
        self.day_input = QSpinBox(self)
        self.day_input.setRange(1, 31)
        self.day_input.setPrefix("Día: ")
        main_layout.addWidget(self.day_input)

        self.month_input = QSpinBox(self)
        self.month_input.setRange(1, 12)
        self.month_input.setPrefix("Mes: ")
        main_layout.addWidget(self.month_input)

        self.year_input = QSpinBox(self)
        self.year_input.setRange(now.year, now.year + 10)
        self.year_input.setPrefix("Año: ")
        main_layout.addWidget(self.year_input)

        # Botón para agregar tarea
        self.add_task_btn = QPushButton("Agregar Tarea")
        self.add_task_btn.clicked.connect(self.add_task)
        main_layout.addWidget(self.add_task_btn)

        # Botón para mostrar todas las tareas
        self.show_task_btn = QPushButton("Mostrar Tareas")
        self.show_task_btn.clicked.connect(self.show_tasks)
        main_layout.addWidget(self.show_task_btn)

        # Configuración del layout en el widget central
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def add_task(self):
        try:
            # Crear una nueva instancia de M_Homework para cada tarea
            tyler = M_Homework()

            # Configurar el archivo
            archive_name = self.archive_input.text()
            if not archive_name:
                raise ValueError("El nombre del archivo no puede estar vacío.")
            tyler.set_archive(archive_name)

            # Configurar nombre de la tarea
            task_name = self.name_input.text()
            if not task_name:
                raise ValueError("El nombre de la tarea no puede estar vacío.")
            tyler.set_name(task_name)

            # Configurar descripción de la tarea
            task_description = self.description_input.text()
            if not task_description:
                raise ValueError("La descripción de la tarea no puede estar vacía.")
            tyler.set_description(task_description)

            # Configurar fecha de la tarea
            day = self.day_input.value()
            month = self.month_input.value()
            year = self.year_input.value()
            days_remaining = tyler.set_date(year, month, day)
            tyler.date = days_remaining  # Guardar el número de días restantes

            # Guardar tarea en la lista de tareas
            self.tasks.append(tyler)  # Agregar tarea a la lista
            result = tyler.save()
            QMessageBox.information(self, "Agregar Tarea", result)

        except ValueError as e:
            QMessageBox.warning(self, "Error en los datos",str(e))

    def show_tasks(self):
        # Crear una ventana de diálogo para mostrar todas las tareas
        self.task_list_dialog = QDialog(self)
        self.task_list_dialog.setWindowTitle("Lista de Tareas")
        layout = QVBoxLayout(self.task_list_dialog)

        # Lista para mostrar tareas
        self.task_list_widget = QListWidget(self.task_list_dialog)
        for task in self.tasks:
            # Calcular la prioridad y la fecha límite
            prioridad = task.priority(task.date)
            fecha_entrega = (now + timedelta(days=task.date)).strftime("%Y-%m-%d") if isinstance(task.date, int) else "Fecha no válida"

            # Crear un item con nombre, descripción, prioridad y fecha
            item_text = f"{task.name} - {task.description} - Fecha: {fecha_entrega} - Prioridad: {prioridad}"
            item = QListWidgetItem(item_text)
            self.task_list_widget.addItem(item)

        layout.addWidget(self.task_list_widget)

        # Botón para eliminar la tarea seleccionada
        delete_btn = QPushButton("Eliminar Tarea Seleccionada", self.task_list_dialog)
        delete_btn.clicked.connect(self.delete_task)
        layout.addWidget(delete_btn)

        # Botón para procesar la tarea seleccionada
        process_btn = QPushButton("Procesar Tarea Seleccionada", self.task_list_dialog)
        process_btn.clicked.connect(self.process_task)
        layout.addWidget(process_btn)

        self.task_list_dialog.setLayout(layout)
        self.task_list_dialog.exec_()

    def delete_task(self):
        selected_item = self.task_list_widget.currentRow()
        if selected_item >= 0:
            del self.tasks[selected_item]
            self.task_list_widget.takeItem(selected_item)
            QMessageBox.information(self, "Eliminar Tarea", "La tarea ha sido eliminada correctamente")
        else:
            QMessageBox.warning(self, "Error", "Seleccione una tarea para eliminar")

    def process_task(self):
        selected_item = self.task_list_widget.currentRow()
        if selected_item >= 0:
            task = self.tasks[selected_item]
            task.date = "Finalizado"  # Marcar la tarea como finalizada
            self.task_list_widget.item(selected_item).setText(f"{task.name} - {task.description} - Finalizado")
            QMessageBox.information(self, "Procesar Tarea", "La tarea ha sido marcada como finalizada")
        else:
            QMessageBox.warning(self, "Error", "Seleccione una tarea para procesar")

# Ejecutar la aplicación
app = QApplication(sys.argv)
window = TaskManagerWindow()
window.show()
sys.exit(app.exec_())


