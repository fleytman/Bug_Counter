import os

from UiMainWindow import Ui_MainWindow
import pyperclip
import ast


class MainWindowSlots(Ui_MainWindow):
    def start_program(self):

        # Load Data
        if not os.path.isfile('data.txt'):
            data_file = open('data.txt', 'w', encoding="utf-8")
            data_file.close()
            users = {}
            # data_file.write("")
        else:
            data_file = open('data.txt', 'r', encoding="utf-8")

            try:
                users = ast.literal_eval(data_file.read())
                print(users)
            except:
                users = {}

            data_file.close()

        # Load Users
        if not os.path.isfile('Тестировщики.txt'):
            # Окно в котором говорится об отсуствие Тестировщики.txt
            pass
        else:
            f = open('Тестировщики.txt', 'r', encoding="utf-8")

        for line in f:
            if line[:-1] not in users:
                users.update({line[:-1]: [0, 0, 0, 0, 0, 0, 0]})
            self.comboBox.addItem(line[:-1])
        f.close()

        data_file = open('data.txt', 'w', encoding="utf-8")
        data_file.write(str(users))

    def generate(self):
        if self.comboBox.currentText() != "":
            """Скрипт, генерирующий отчёт по багам
            by fleytman"""

            summ = int(self.lineEdit_0.text()) + int(self.lineEdit_1.text()) + \
                   int(self.lineEdit_2.text()) + int(self.lineEdit_3.text()) + \
                   int(self.lineEdit_4.text()) + int(self.lineEdit_5.text()) + \
                   int(self.lineEdit_6.text())

            self.summEdit.setText(str(summ))
            self.summEdit.setEnabled(True)

            path = "Отчёт по багам " + self.comboBox.currentText() + ".txt"
            f = open(path, "w+")

            L = int(38 / 2 - len(self.comboBox.currentText()) / 2)
            print(L)
            f.write(" " * L + self.comboBox.currentText() + "\n")
            f.write("---------------------------------------\n")
            f.write("         Категория               Баги \n")
            f.write("-----------------------------||-------- \n")
            f.write("Критичный первой категории   || " + self.lineEdit_0.text() + "\n")
            f.write("Критичный первой категории   || " + self.lineEdit_1.text() + "\n")
            f.write("Некритичный первой категории || " + self.lineEdit_2.text() + "\n")
            f.write("Некритичный первой категории || " + self.lineEdit_3.text() + "\n")
            f.write("Простейший                   || " + self.lineEdit_4.text() + "\n")
            f.write("Не баг/дубль                 || " + self.lineEdit_5.text() + "\n")
            f.write("Некорректный                 || " + self.lineEdit_6.text() + "\n")
            f.write("---------------------------------------\n")
            f.write("ИТОГО                        || " + str(summ) + "\n")
            f.close()

            self.statusBar.showMessage("Файл \"" + path + "\" сгенирирован")

            os.startfile(path)

            mystring = self.lineEdit_0.text() + "\n" + self.lineEdit_1.text() + "\n" + \
                       self.lineEdit_2.text() + "\n" + self.lineEdit_3.text() + "\n" + \
                       self.lineEdit_4.text() + "\n" + self.lineEdit_5.text() + "\n" + \
                       self.lineEdit_6.text()

            pyperclip.copy(str(mystring))

        else:
            self.statusBar.showMessage("Поле фамилия не заполнено")

        return None

    # кнопки плюс
    def plus_button_0(self):
        if (int(self.lineEdit_0.text())) < 999:
            self.lineEdit_0.setText(str(int(self.lineEdit_0.text()) + 1))

    def plus_button_1(self):
        if (int(self.lineEdit_1.text())) < 999:
            self.lineEdit_1.setText(str(int(self.lineEdit_1.text()) + 1))

    def plus_button_2(self):
        if (int(self.lineEdit_2.text())) < 999:
            self.lineEdit_2.setText(str(int(self.lineEdit_2.text()) + 1))

    def plus_button_3(self):
        if (int(self.lineEdit_3.text())) < 999:
            self.lineEdit_3.setText(str(int(self.lineEdit_3.text()) + 1))

    def plus_button_4(self):
        if (int(self.lineEdit_4.text())) < 999:
            self.lineEdit_4.setText(str(int(self.lineEdit_4.text()) + 1))

    def plus_button_5(self):
        if (int(self.lineEdit_5.text())) < 999:
            self.lineEdit_5.setText(str(int(self.lineEdit_5.text()) + 1))

    def plus_button_6(self):
        if (int(self.lineEdit_6.text())) < 999:
            self.lineEdit_6.setText(str(int(self.lineEdit_6.text()) + 1))

    # Кнопка минус
    def minus_button_0(self):
        if (int(self.lineEdit_0.text())) > 0:
            self.lineEdit_0.setText(str(int(self.lineEdit_0.text()) - 1))

    def minus_button_1(self):
        if (int(self.lineEdit_1.text())) > 0:
            self.lineEdit_1.setText(str(int(self.lineEdit_1.text()) - 1))

    def minus_button_2(self):
        if (int(self.lineEdit_2.text())) > 0:
            self.lineEdit_2.setText(str(int(self.lineEdit_2.text()) - 1))

    def minus_button_3(self):
        if (int(self.lineEdit_3.text())) > 0:
            self.lineEdit_3.setText(str(int(self.lineEdit_3.text()) - 1))

    def minus_button_4(self):
        if (int(self.lineEdit_4.text())) > 0:
            self.lineEdit_4.setText(str(int(self.lineEdit_4.text()) - 1))

    def minus_button_5(self):
        if (int(self.lineEdit_5.text())) > 0:
            self.lineEdit_5.setText(str(int(self.lineEdit_5.text()) - 1))

    def minus_button_6(self):
        if (int(self.lineEdit_6.text())) > 0:
            self.lineEdit_6.setText(str(int(self.lineEdit_6.text()) - 1))

    def change_text(self):
        self.lineEdit_0.text()

    def update_data(self):
        if self.comboBox.currentText() != "":
            data_file = open('data.txt', 'r', encoding="utf-8")

            users = ast.literal_eval(data_file.read())
            users.update({self.comboBox.currentText(): [int(self.lineEdit_0.text()), int(self.lineEdit_1.text()),
                                                        int(self.lineEdit_2.text()), int(self.lineEdit_3.text()),
                                                        int(self.lineEdit_4.text()), int(self.lineEdit_5.text()),
                                                        int(self.lineEdit_6.text())]})

            data_file.close()
            data_file = open('data.txt', 'w', encoding="utf-8")
            data_file.write(str(users))

        self.statusBar.clearMessage()

        self.summEdit.setText("")
        self.summEdit.setEnabled(False)

    def load_user(self):
        if self.comboBox.currentText() != "":
            data_file = open('data.txt', 'r', encoding="utf-8")

            users = ast.literal_eval(data_file.read())
            i_values = users.get(self.comboBox.currentText())
            values = []
            for value in i_values:
                values.append(str(value))
            print(values)
            data_file.close()

            self.lineEdit_0.setText(values[0])
            self.lineEdit_1.setText(values[1])
            self.lineEdit_2.setText(values[2])
            self.lineEdit_3.setText(values[3])
            self.lineEdit_4.setText(values[4])
            self.lineEdit_5.setText(values[5])
            self.lineEdit_6.setText(values[6])
        else:
            self.lineEdit_0.setText("0")
            self.lineEdit_1.setText("0")
            self.lineEdit_2.setText("0")
            self.lineEdit_3.setText("0")
            self.lineEdit_4.setText("0")
            self.lineEdit_5.setText("0")
            self.lineEdit_6.setText("0")

    def clear_user_data(self):
        self.lineEdit_0.setText("0")
        self.lineEdit_1.setText("0")
        self.lineEdit_2.setText("0")
        self.lineEdit_3.setText("0")
        self.lineEdit_4.setText("0")
        self.lineEdit_5.setText("0")
        self.lineEdit_6.setText("0")

        self.statusBar.clearMessage()

        self.summEdit.setText("")
        self.summEdit.setEnabled(False)