BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"
        :param id_: Идентификатор (порядковый номер) книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        self.id_ = id_
        self.name = name
        self.pages = pages

class Library:
    def __init__(self, books=None):
        """
        Создание и подготовка к работе объекта "Библиотека"
        :param books: Список книг
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id (self, id_) -> int:
        """"
        Метод возвращает идентификатор новой книги для добавления в библиотеку, если в библиотеке есть книги.
        Метод возвращает 1, если в библиотеке нет книг.
        """
        if len(self.books) == 0:
            return 1
        else:
            return self.books[-1].id_+1

    def get_index_by_book_id (self, id_) -> int:
        """
        Метод возвращает индекс книги по идентификатору, если книга с данным id существует.
        Метод возвращает строку "Книги с запрашиваемым id не существует", если такой книги нет.
        """
        for index, book in enumerate(self.books):
            if book.id_ == id_:
                return index
        print("Книги c запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  #инициализируем пустую библиотеку
    print(empty_library.get_next_book_id(1))  #проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  #инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id(1))  #проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  #проверяем индекс книги с id = 1
