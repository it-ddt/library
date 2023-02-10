"""
    TODO: 
        создать меню с выбором действий
        при поиске по ключу вывести сообщение, если книга не нашлась
"""

library = [
    {
        "название": "Введение в Python. Том 1",
        "автор": "Марк Лутц",
        "год": 2022
    },
    {
        "название": "Введение в Python. Том 2",
        "автор": "Марк Лутц",
        "год": 2022
    },
    {
        "название": "Искусство программирования",
        "автор": "Дональд Кнут",
        "год": 2019
    },
    {
        "название": "Грокаем алгоритмы",
        "автор": "Бхаргава Адитья",
        "год": 2020    
    }
]


def show_books() -> None:
    """ выводит на экран все книги библиотеки, пронумеровав их с 1 """
    
    if not library:
        print("Библиотека пуста")
        return
    for num, book in enumerate(library, 1):
        print(f"номер на полке: {num}")
        print(f"название: {book['название']}")
        print(f"автор: {book['автор']}")
        print(f"год: {book['год']}")
        print("")


def add_book() -> None:
    """ добавляет книгу в библиотеку, в книге обязательно заполненыф 3 поля """
    
    title = input("Введите название книги: ")
    if not title:
        print("Ошибка! Нет названия.")
        return

    author = input("Введите имя автора книги: ")
    if not author:
        print("Ошибка! Нет автора.")
        return

    year = input("Введите год издания книги: ")
    if year.isdigit():
        year = int(year)
    else:
        print("Ошибка! Год должен быть целым числом.")
        return

    book = {
        "название": title,
        "автор": author,
        "год": year
    }

    if book in library:
        print("Ошибка! Такая книга уже есть.")
        return

    library.append(book)
    print("Книга успешно добавлена в библиотеку!")


def remove_book() -> None:
    """ удаляет книгу из библиотеки по порядковму номеру ( >0 ) """
    
    num = input("Введите номер книги для удаления: ")
    
    if not num.isdigit():
        print("Номер должен быть целым числом")
        return
    else:
       num = int(num)

    idx = num - 1 

    if idx < 0:
        print("Номер должен быть целым положительным числом")
        return

    if idx > len(library) - 1:
        print("Нет такой книги")
        return

    print(f"Книга {library[idx]} удалена")
    library.pop(idx)

    
def find_book_by_number() -> None:
    """ Ищет книгу по порядковому номеру и показывает ее """
    
    num = input("Введите порядковый номер книги: ")

    if not num.isdigit():
        print("Номер должен быть целым положительным числом")
        return

    num = int(num) 
    idx = num - 1

    if idx < 0:
        print("Номер должен быть целым положительным числом")
        return

    if idx > len(library) - 1:
        print("В библиотеке нет такой книги")
        return

    book = library[idx]

    print("Книга найдена!")
    print(f"номер на полке: {idx + 1}")
    print(f"название: {book['название']}")
    print(f"автор: {book['автор']}")
    print(f"год: {book['год']}")
    print("")


def search_book_by_key(user_key: str) -> None:
    """ Показывает на экране книгу, если находит её по порыядковому номеру """
    
    if not library:
        print("Библиотека пуста!")
        return

    user_value = input(f"Введите {user_key}: ")

    if not user_value:
        print("Нет данных для поиска!")
        return

    if user_key == "год" :
        if user_value.isdigit():
            user_value = int(user_value)
        else:
            print("год должен быть числом")
            return
    
    for book in library:
        if book[user_key] == user_value:
            print(f"номер на полке: {library.index(book) + 1}")
            print(f"название: {book['название']}")
            print(f"автор: {book['автор']}")
            print(f"год: {book['год']}")
            print("")

def menu():
    while True:
        print("1. Показать все")

        user_choice = input()

        if user_choice == "1":
            show_books()
        elif user_choice == "0":
            return

# тестирование
menu()