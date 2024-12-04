**Описание приложения**

Это консольное приложение позволяет пользователю управлять библиотекой книг. Пользователь может добавлять, удалять, искать и отображать книги, а также изменять статус книги. Данные о книгах хранятся в формате JSON в файле db.json.
____
**Импортируемые модули**
```
import json
import os
```
**json**: Модуль для работы с JSON-форматом, используемый для сериализации и десериализации данных.
**os**: Модуль для взаимодействия с операционной системой, используется для проверки существования файла.
____
**Глобальные переменные**
```
data = "db.json"
```

**data**: Строка, содержащая имя файла, в котором хранятся данные о книгах.
____
**Функции**

`read_db() -> list`

Читает данные из файла db.json. Если файл существует, загружает и возвращает список книг. Если файл отсутствует, возвращает пустой список.


`write_db(books_list: list) -> None`

Записывает переданный список книг в файл db.json в формате JSON.

`create_book(title: str, author: str, year: str) -> None`

Создает новую книгу с заданными параметрами:

**title**: Название книги.

**author**: Автор книги.

**year**: Год издания книги.

Функция генерирует уникальный идентификатор для новой книги и добавляет ее в список книг. Если год не является числом, запрашивает его повторно у пользователя.

`delete_book(book_id: str) -> None`

Удаляет книгу из библиотеки по указанному идентификатору:

**book_id**: Идентификатор книги для удаления.

Если книга с указанным идентификатором найдена, она удаляется из списка и файл обновляется. Если книга не найдена, выводится сообщение об этом.

`hide_book(argument: str) -> None`

Ищет книги по указанному аргументу (названию, автору или году издания):

**argument**: Строка для поиска.

Выводит список найденных книг или сообщение о том, что книги не найдены.

`books_list() -> None`

Отображает все книги в библиотеке. Если библиотека пуста, выводит соответствующее сообщение.

`change_status(book_id: str, status: str) -> None`

Изменяет статус книги по указанному идентификатору:

**book_id**: Идентификатор книги.

**status**: Новый статус книги (может быть "в наличии" или "выдана").

Если книга с указанным идентификатором найдена, статус изменяется и файл обновляется. Если книга не найдена или статус уже установлен, выводится соответствующее сообщение.

`main_func() -> None`

Основная функция приложения, которая предоставляет пользователю меню для взаимодействия с библиотекой. Пользователь может выбрать действие (добавление, удаление, поиск книг и т.д.) через командный ввод. Программа продолжает работать до тех пор, пока пользователь не введет команду "Exit".
____
**Запуск приложения**

Приложение запускается при выполнении скрипта. При запуске отображается приветственное сообщение и вызывается основная функция.
____
**Заключение**

Данное приложение предоставляет простой интерфейс для управления библиотекой книг с возможностью добавления, удаления и поиска книг. Использование JSON позволяет легко сохранять и загружать данные о книгах.