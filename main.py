"""
Основной скрипт программы.
Запускает конфигуратор окна, подключает слоты и отображает окно.
"""
# Импортируем системый модуль для корректного закрытия программы
import sys
# Импортируем минимальный набор виджетов
#from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
# Импортируем созданный нами класс со слотами
from slots import MainWindowSlots
from PyQt5.QtGui import QIntValidator

# Создаём ещё один класс, наследуясь от класса со слотами
class MainWindow(MainWindowSlots):

    # При инициализации класса нам необходимо выпонить некоторые операции
    def __init__(self, dialog):
        # Сконфигурировать интерфейс методом из базового класса Ui_Form
        self.setupUi(dialog)
        # Подключить созданные нами слоты к виджетам
        self.connect_slots()

        self.lineEdit_0.setValidator(QIntValidator(0, 999))
        self.lineEdit_1.setValidator(QIntValidator(0, 999))
        self.lineEdit_2.setValidator(QIntValidator(0, 999))
        self.lineEdit_3.setValidator(QIntValidator(0, 999))
        self.lineEdit_4.setValidator(QIntValidator(0, 999))
        self.lineEdit_5.setValidator(QIntValidator(0, 999))
        self.lineEdit_6.setValidator(QIntValidator(0, 999))


    # Подключаем слоты к виджетам
    def connect_slots(self):
        self.start_program()

        self.pushButton.clicked.connect(self.generate)
        self.pushButton_2.clicked.connect(self.clear_user_data)


        self.plusButton_0.clicked.connect(self.plus_button_0)
        self.plusButton_1.clicked.connect(self.plus_button_1)
        self.plusButton_2.clicked.connect(self.plus_button_2)
        self.plusButton_3.clicked.connect(self.plus_button_3)
        self.plusButton_4.clicked.connect(self.plus_button_4)
        self.plusButton_5.clicked.connect(self.plus_button_5)
        self.plusButton_6.clicked.connect(self.plus_button_6)

        self.minusButton_0.clicked.connect(self.minus_button_0)
        self.minusButton_1.clicked.connect(self.minus_button_1)
        self.minusButton_2.clicked.connect(self.minus_button_2)
        self.minusButton_3.clicked.connect(self.minus_button_3)
        self.minusButton_4.clicked.connect(self.minus_button_4)
        self.minusButton_5.clicked.connect(self.minus_button_5)
        self.minusButton_6.clicked.connect(self.minus_button_6)

        self.lineEdit_0.textChanged.connect(self.update_data)
        self.lineEdit_1.textChanged.connect(self.update_data)
        self.lineEdit_2.textChanged.connect(self.update_data)
        self.lineEdit_3.textChanged.connect(self.update_data)
        self.lineEdit_4.textChanged.connect(self.update_data)
        self.lineEdit_5.textChanged.connect(self.update_data)
        self.lineEdit_6.textChanged.connect(self.update_data)

        self.comboBox.currentIndexChanged.connect(self.load_user)

        return None

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = MainWindow(Window)
    Window.show()
    sys.exit(app.exec_())
