import sys
import pyperclip
import moduls

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("gen_pass.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

val_pass = ["pass", "pass", "pass"]

def append_val_pass(val_pass):
	index = 0
	for box_text in val_pass:
		form.comboBox.setItemText(index, box_text)
		index += 1

def generate():

	try:
		values = []
		len_pass = int(form.lineEdit.text())

		# Проверка чекбоксов
		az_check = form.checkBox.isChecked()
		AZ_check = form.checkBox_2.isChecked()
		spec_sumbol_check = form.checkBox_3.isChecked()
		digits_check = form.checkBox_4.isChecked()

		# Создание списка для передачи в функцию из другого модуля
		values = [az_check, AZ_check, spec_sumbol_check, digits_check]

		password_string = moduls.generate_pass(len_pass, moduls.check_checkbox(len_pass, values))

		if val_pass[0] == "pass":
			val_pass[0] = password_string
			append_val_pass(val_pass)

		elif val_pass[0] != "pass":
			val_pass.pop(2)
			val_pass.insert(0, password_string)
			append_val_pass(val_pass)

	except ValueError:
		print("Вы не ввели длину пароля")
	except TypeError:
		print("Вы не выбрали чекбокс для генерации")
		
	# print(password_string)

	# form.comboBox.setItemText(2, "хихих") # Устанавливает текст по индексу
	# print(form.comboBox.itemText(2)) # Считывает элемент по индексу
	# print(form.comboBox.count()) # Считывает все индексы
	# form.comboBox.removeItem(2) # Удаляет элемент по индексу


def copy():
	pyperclip.copy(form.comboBox.currentText()) # Считывает значение из comboBox
	print("Копирование")

def exit_prog():
	exit()

# Проверка кнопок
form.pushButton.clicked.connect(generate)
form.pushButton_3.clicked.connect(copy)
form.pushButton_2.clicked.connect(exit_prog)

# print(form.comboBox.activated[str].connect(combo_box))

app.exec()