import pickle
import json

class Book:
    """Модель книги"""
    list_read_books = []

    def __init__(self, author, genre, name_book, pages, read_pages):
        self.author = author
        self.genre = genre
        self.name_book = name_book
        self.pages = pages
        self.book_read = False
        self.read_pages = read_pages

    def get_author(self, age):
        """Информация об авторе книги"""
        return (f"Имя автора: {self.author}\n"
                f"Возраст автора: {age}")

    def get_genre(self):
        """Информация о жанре книги"""
        return self.genre

    def get_pages(self):
        """Информация о количестве страниц в книге"""
        return self.pages

    def get_read_book(self):
        """Информация о прочтении книги"""
        percent_read_book = (self.read_pages / self.pages) * 100

        if 0 <= percent_read_book < 100:
            print("Книга не прочитана!")
            self.book_read = False
        elif percent_read_book == 100:
            if self.name_book not in Book.list_read_books:
                print("Книга прочитана!")
                Book.list_read_books.append(self.name_book)
                print(f"Список прочитанных книг: {Book.list_read_books}")
            else:
                print(f"Книга '{self.name_book}' уже в списке прочитанных.")
            self.book_read = True
        else:
            print("Неверный ввод данных!")
        return self.book_read


class Pickler:

    def __init__(self, protocol: int = pickle.DEFAULT_PROTOCOL):
        self.protocol = protocol

    def save_data(self, data, filename):
        '''Сохранение данных при помощи pickle'''
        with open(filename, 'wb') as fp:
            pickle.dump(data, fp)

    def load_data(self, filename):
        '''Загрузка объекта из pickle-файла'''
        try:
            with open(filename, 'rb') as fp:
                data = pickle.load(fp)
                print(f"Данные успешно загружены из файла {filename}")
                return data
        except FileNotFoundError:
            print(f"Файл {filename} не найден!")
            return None

class BookEncoder(json.JSONEncoder):

    def default(self, o):
        return {
            "Автор": o.author,
            "Жанр": o.genre,
            "Наименование": o.name_book,
            "Кол-во страниц": o.pages,
            "Прочитано страниц:": o.read_pages,
            "Прочтение книги:": o.book_read,
            "Список прочитанных книг:": o.list_read_books
        }

    def save_json(self, object, filename):
        """Преобразование объекта в json файл"""

        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(object, fp, cls=BookEncoder, ensure_ascii=False, indent=2)

    def load_json(self, filename):
        """Распаковка json файла"""
        try:
            with open(filename, 'r', encoding='utf-8') as fp:
                data = json.load(fp)
                print(f"Данные успешно выгружены из файла {filename}")
                return data
        except FileNotFoundError:
            print(f"Файл {filename} не найден!")
            return None

if __name__ == "__main__":
    book = Book('Прилепин', 'Роман', 'Обитель', 752, 752)
    print(book.get_read_book())

    my_pickle = Pickler()
    my_pickle.save_data(book, r'files/book_name.pkl')
    print()

    json_file = BookEncoder()
    json_file.save_json(book, r'files/book.json')
    print()

    book_1 = Book('Булгаков', 'Роман', 'Белая гвардия', 992, 300)
    book_1.get_read_book()
    json_file.save_json(book_1, r'files/book.json')
    print(json_file.load_json(r'files/book.json'))
    print()

    book_2 = Book('Лермонтов', 'Баллада', 'Бородино', 64, 64)
    book_2.get_read_book()
    json_file.save_json(book_2, r'files/book.json')
    print()

    book_3 = Book('Пушкин', 'Сказка', 'О царе Салтане', 62, 62)
    book_3.get_read_book()
    json_file.save_json(book_3, r'files/book.json')
    print()
