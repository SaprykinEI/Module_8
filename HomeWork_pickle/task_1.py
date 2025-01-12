import pickle

class Pickler:

    def __init__(self, protocol:int = pickle.DEFAULT_PROTOCOL):
        self.protocol = protocol

    def pickle_file(self, data, filename):
        '''Сохранение данных при помощи pickle'''
        with open(filename, "wb")as file:
            pickle.dump(data, file)

    def load_pickle_file(self, filename):
        '''Загрузка объекта из pickle-файла'''
        try:
            with open(filename, 'rb') as file:
                data = pickle.load(file)
                print(f"Данные успешно загружены из файла {filename}.")
                return data
        except FileNotFoundError:
            print(f"Файл {filename} не найден!")
            return None


class Country:

    def __init__(self):
        self.country_dict = {}

    def add_data(self, country, capital):
        '''Добавление данных'''
        self.country_dict[country] = capital

    def delete_data(self, country):
        '''Удаление данных'''
        for key, value in self.country_dict.items():
            if key == country:
                delete_country = self.country_dict.pop(key)
                return delete_country
        return "Такая страна не найдена!"

    def search_data(self, country):
        '''Поиск данных'''
        if country in self.country_dict:
            return f"Страна {country} найдена, её столица {self.country_dict[country]}"
        else:
            return f"Данная страна не найдена!"

    def editing_data(self, country, new_capital):
        '''Редактирование данных'''
        if country in self.country_dict:
            self.country_dict[country] = new_capital
            return f"Столица страны {country} успешно изменена на {new_capital}"
        else:
            return "Страна не найдена"






if __name__ == "__main__":
    my_dict = Country()
    my_dict.add_data("Россия", "Москва")
    my_dict.add_data("Беларусь", "Минск")
    my_dict.add_data("Китай", "Пекин")
    print(my_dict.search_data("Китай"))
    print(my_dict.delete_data("Беларусь"))
    print(my_dict.delete_data("США"))
    print(my_dict.editing_data("Россия", "Санкт-Петербург"))
    my_pickler = Pickler()
    my_pickler.pickle_file(my_dict, 'my_pickle.pkl')
    my_pickler.load_pickle_file('my_pickle.pkl')

