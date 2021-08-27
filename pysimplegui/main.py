import PySimpleGUI as sg
import pyperclip
import moduls

from win32gui import ShowWindow
from win32console import GetConsoleWindow
from win32con import SW_HIDE


sg.ChangeLookAndFeel("Gray Gray Gray")


layout = [
	  [sg.Checkbox("Символы a-z", text_color="#000000", background_color="#C2C2C2", default=True), sg.Checkbox("Символы A-Z", text_color="#000000", background_color="#C2C2C2"), sg.Checkbox("Специальные символы", text_color="#000000", background_color="#C2C2C2"), sg.Checkbox("Цифры 0-9", text_color="#000000", background_color="#C2C2C2")],
	  [sg.Text("Введи длину пароля:" , text_color="#000000", background_color="#C2C2C2"), sg.InputText("8", size=(4, 1), justification="center")],
	  [sg.Text("Результат генерации:", text_color="#000000", background_color="#C2C2C2"), sg.Combo(["pass", "pass", "pass"], background_color="", tooltip="Сгенерированный пароль", size=(20, 22), key="password")],
      [sg.Text("", size=(52, 1), text_color="#000000", background_color="#C2C2C2", key="error")],
      [sg.Button("Generate", button_color=("white", "#454545"), pad=((0, 0), (51, 0))), sg.Button("Copy", button_color=("white", "#454545"), size=(7, 1), pad=((160, 0), (51, 0))), sg.Button("Exit", button_color=("white", "#454545"), size=(7, 1), pad=((155, 0), (51, 0)))]
]

window = sg.Window("Password Gen", layout, background_color="#C2C2C2", icon="pass_icon.ico")
val_pass = ["pass", "pass", "pass"]

def hide():
	if "__main__" == __name__:
		ShowWindow(GetConsoleWindow(), SW_HIDE)
hide()

while True:
	event, values = window.read()
	window.Element("error").Update("")

	# Размер окна
	# print(window.size)

	# print(values)

	if event == "Exit" or event == sg.WIN_CLOSED:
		break

	elif event == "Generate":
		try:
			len_pass = int(values[4])
			gen_pass = moduls.check_checkbox(len_pass, values)

			if gen_pass == 1:
				window.Element("error").Update("Вы не выбрали чекбокс для генерации пароля")

			else:
				window.Element("error").Update("")
				if val_pass[0] == "pass":
					# print(gen_pass)
					val_pass[0] = gen_pass
					window.Element("password").Update(gen_pass, values=val_pass)
					
				elif val_pass[0] != "pass":
					# print(gen_pass)
					val_pass.pop(2)
					val_pass.insert(0, gen_pass)

					window.Element("password").Update(gen_pass, values=val_pass)
		
		except ValueError:
			window.Element("error").Update("Вы не правильно указали длину пароля. Длина должна быть числом.")

		except NameError:
			pass

	elif event == "Copy":
		pyperclip.copy(values["password"])
		window.Element("error").Update("Пароль скопирован")