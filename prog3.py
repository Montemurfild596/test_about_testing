import unittest
from tkinter import *
from tkinter import ttk

# Ваше приложение
def create_app():
    root = Tk()
    root.title("TEST_UI")
    root.geometry("200x200") 

    entry = ttk.Entry(root)
    entry.pack(anchor=NW, padx=6, pady=6)

    label = ttk.Label(root)
    label.pack(anchor=NW, padx=6, pady=6)

    def show_message():
        text = entry.get()  # получаем введенный текст
        if any(c.isdigit() for c in text):
            label["text"] = "Успешно"
        elif any(c.isalpha() for c in text):
            label["text"] = "Ошибка"

    btn = ttk.Button(root, text="Click", command=show_message)
    btn.pack(anchor=NW, padx=6, pady=6)

    return root, entry, label

class TestApp(unittest.TestCase):
    def setUp(self):
        self.root, self.entry, self.label = create_app()

    def tearDown(self):
        self.root.destroy()

    def test_input_with_letter(self):
        self.entry.insert(0, 'A')
        self.root.update()  # Обновляем интерфейс
        self.root.children['!button'].invoke()  # Вызываем нажатие кнопки
        self.root.update()  # Обновляем интерфейс после вызова кнопки
        self.assertEqual(self.label["text"], "Ошибка")

    def test_input_with_digit(self):
        self.entry.insert(0, '1')
        self.root.update()  # Обновляем интерфейс
        self.root.children['!button'].invoke()  # Вызываем нажатие кнопки
        self.root.update()  # Обновляем интерфейс после вызова кнопки
        self.assertEqual(self.label["text"], "Успешно")

if __name__ == '__main__':
    unittest.main()
    #create_app()
