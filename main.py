import json
import os

data = "db.json"


def read_db() -> list:
    if os.path.exists(data):
        with open(data, 'r') as db:
            return json.load(db)
    return []


def write_db(books_list: list) -> None:
    with open(data, 'w') as db:
        json.dump(books_list, db)


def create_book(title: str, author: str, year: str) -> None:
    while not year.isdigit():
        year = input('Введите год издания книги: ')
    new_id = len(books) + 1
    new_book = {
        'id': new_id,
        'title': title,
        'author': author,
        'year': year,
        'status': 'в наличии'
    }
    books.append(new_book)
    write_db(books)
    print('Книга успешно добавлена!')


def delete_book(book_id: str) -> None:
    while not book_id.isdigit():
        book_id = input('Введите id книги для удаления: ')
    flag = False
    for book in books:
        if book['id'] == int(book_id):
            flag = True
            books.remove(book)
    if flag:
        for book in books:
            if book['id'] > int(book_id):
                book['id'] -= 1
        write_db(books)
        print('Книга успешно удалена!')
        return
    print('Книга с таким id не найдена!')


def hide_book(argument: str) -> None:
    found_books = [book for book in books if
                   (argument in book['title'] or argument in book['author'] or argument in book['year'])]
    if found_books:
        for book in found_books:
            print(f'{book["id"]}: {book["title"]} - {book["author"]} ({book["year"]}) - {book["status"]}')
    else:
        print('Книга не найдена!')


def books_list() -> None:
    if not books:
        print('Библиотека пуста!')
        return

    for book in books:
        print(f'{book["id"]}: {book["title"]} - {book["author"]} ({book["year"]}) - {book["status"]}')


def change_status(book_id: str, status: str) -> None:
    while not book_id.isdigit():
        book_id = input('Введите id книги для изменения статуса: ')
    while status not in ('в наличии', 'выдана'):
        status = input('Введите статус книги (в наличии/выдана): ').lower()
    for book in books:
        if book['id'] == int(book_id):
            if book['status'] == status:
                print('Данный статус книги уже задан!')
            else:
                book['status'] = status
                write_db(books)
                print('Статус книги успешно изменен!')
        return
    print('Книга с таким id не найдена!')


def main_func() -> None:
    while True:
        print('\nДля добавления книги введите "Добавить"\n'
              'Для удаления книги введите "Удалить"\n'
              'Для нахождения книги введите "Найти"\n'
              'Для отображения всех книг введите "Список"\n'
              'Для изменения статуса книги введите "Статус"\n'
              'Для выхода из программы введите "Exit"\n')
        command = input('Поле для ввода: ').lower()

        if command == 'добавить':
            title = input('Введите название книги: ')
            author = input('Введите автора книги: ')
            year = input('Введите год издания книги: ')
            create_book(title, author, year)

        elif command == 'удалить':
            book_id = input('Введите id книги для удаления: ')
            delete_book(book_id)

        elif command == 'найти':
            answer = input('Введите название, автора или год издания книги: ')
            hide_book(answer)

        elif command == 'список':
            books_list()

        elif command == 'статус':
            book_id = input('Введите id книги для изменения статуса: ')
            status = input('Введите статус книги (в наличии/выдана): ').lower()
            change_status(book_id, status)

        elif command == 'exit':
            break


books = read_db()

if __name__ == '__main__':
    print('Приветствуем вас в интерактивной библиотеке!')
    main_func()
