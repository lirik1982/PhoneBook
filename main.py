from view import add_to_contact, seach_by_number, create_contact
from view import seach_by_name, del_by_name, del_phone, show_all
from view import seed_base
from db import Base, engine


def main():
    Base.metadata.create_all(engine)

    while True:
        print('''
--------------------------
Книга контактов
Выберите команду
--------------------------
1-Создать контакт
2-Добавить телефон к контакту
3-Поиск контакта по номеру
4-Поиск контакта по имени
5-Удаление контакта по имени
6-Удаление номера
7-Вывести все контакты с номерами
8-Заполнение базы случайными данными
0-Выход''')

        ch = input()
        match ch:
            case '0': break
            case '1': create_contact()
            case '2': add_to_contact(input('Укажите имя: '))
            case '3': seach_by_number(input('Введите номер: '))
            case '4': seach_by_name(input('Введите имя: '))
            case '5': del_by_name(input('Введите имя для удаления: '))
            case '6': del_phone(input('Введите номер для удаления: '))
            case '7': show_all()
            case '8': seed_base(int(input('Укажите количество контактов: ')))


if __name__ == "__main__":
    main()
