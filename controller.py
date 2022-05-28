import action
import view
from innit import *

def start():
    while True:
        view.menu()
        if view.answer == 1:
            action.show(input('Введите фамилию: '))
        elif view.answer == 2:
            action.add(name,team,post,salary,phone)
        elif view.answer == 3:
            action.dell(input('Введите фамилию: '))
        elif view.answer == 4:
            print("Программа завершена")
            break
        else:
            print('Некорректный ввод')


