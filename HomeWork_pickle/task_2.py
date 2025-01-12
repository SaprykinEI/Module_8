import pickle

class Pickler:

    def __init__(self, protocol: int = pickle.DEFAULT_PROTOCOL):
        self.protocol = protocol

    def save_data(self, data, filename):
        '''Сохранение данных при помощи pickle'''
        with open(filename, 'wb') as file:
            pickle.dump(data, file)

    def load_data(self, filename):
        '''Загрузка данных из pickle файла'''
        try:
            with open(filename, 'rb') as file:
                data = pickle.load(file)
                print(f"Данные из файла {filename}, успешно загружены")
                return data
        except FileNotFoundError:
            print(f"Файл {filename} не найден!")
            return None
        except pickle.UnpicklingError:
            print(f"Ошибка распаковки данных из файла {filename}. Возможно, файл повреждён или не является корректным")

class Artist:

    def __init__(self):
        self.artist_dict = {}

    def add_data(self, artist, album):
        '''Добавление данных в словарь'''
        if artist not in self.artist_dict:
            self.artist_dict[artist] = album
        else:
            print(f"Для {artist}, альбом уже существует")

    def delete_data(self, artist):
        '''Удаление данных'''
        if artist in self.artist_dict:
            delete_artist = self.artist_dict.pop(artist)
            return f"Альбом {delete_artist} артиста {artist} был удален"
        else:
            return f"Артист {artist} не найден"

    def search_data(self, artist):
        '''Поиск данных'''
        if artist in self.artist_dict:
            return f"Артист {artist} найден, у него есть альбом {self.artist_dict[artist]}"
        else:
            return f"{artist}, не найден в нашей базе данных"

    def editing_data(self, artist, new_album):
        if artist in self.artist_dict:
            # self.artist_dict[artist] = new_album
            self.artist_dict.get(artist, new_album)
            return f"У артиста {artist}, изменился альбом на {new_album}"
        else:
            return f"Артист не найден"


if __name__ == "__main__":
    my_artist = Artist()
    my_artist.add_data("Александр Розенбаум", "Берега чистого братства")
    my_artist.add_data("Михаил Шуфутинский", "3-е сентября")
    my_artist.add_data("Григорий Лепс", "Натали")
    print(my_artist.search_data("Григорий Лепс"))
    print(my_artist.search_data("Queen"))
    print()
    print(my_artist.editing_data("Александр Розенбаум", "Гоп-Стоп"))
    print(my_artist.delete_data("Михаил Шуфутинский"))
    print()
    my_pickle = Pickler()
    my_pickle.save_data(my_artist, 'artist.album')
    my_pickle.load_data('artist.album')
    my_pickle.load_data('artist.pkl')