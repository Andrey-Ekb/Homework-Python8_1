from functional import *
from interface import start
import os
os.system('cls')

def clear_console():
    os.system('cls')

path = "phone_book.txt"

start()    
actions = {"1": "вывод всех", "2": "добавить", "3": "поиск", "4": "редактировать", "5": "удалять", "q": "выход"}
action = None

while action != "q":
    print( *[f"{i} - {actions[i]}" for i in actions])
    print()
    action = input("выберите, что делать? ")
    clear_console()
    if action != "q":
        if action == "1":
            print('\n'*2)
            print("               Cписок абонентов : ")
            print('            ======================')
            print_records(path)
        elif action == "2":
            input_records(path)
        elif action == "3":
            find_records(path, *find_char())
        elif action == "4":
            change_records(path)
        elif action == "5":
            delete_records(path)
        else:
            print('Данный параметр неиспользуется')
        print()
