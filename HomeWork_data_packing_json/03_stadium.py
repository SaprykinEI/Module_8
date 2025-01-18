import pickle
import json

class Stadium:
    '''Модель стадиона'''

    def __init__(self, name, capacity, destiny, working=True):
        self.name = name
        self.capacity = capacity
        self.destiny = destiny
        self.working = working

    def get_name_stadium(self):
        """Название стадиона"""
        return self.name

    def get_capacity(self):
        """Вместимость стадиона"""
        return self.capacity

    def get_destiny(self):
        """Предназначение стадиона"""
        return self.destiny

    def get_working_stadium(self):
        """Работает сейчас стадион"""
        return self.working

    def __str__(self):
        return f"Стадион: {self.name}, {self.capacity}, {self.destiny}, {self.working}"


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

class JSONDataAdapter:
    @staticmethod
    def save_to_json(obj, filename):
        if isinstance(obj, Stadium):
            json_string = json.dumps({
                'Name_Stadion': obj.name,
                'Capacity': obj.capacity,
                'Destiny': obj.destiny,
                'Working_stadion': obj.working
            })
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_string)
        return json_string

    @staticmethod
    def load_from_json(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            obj = json.load(file)
            try:
                return Stadium(obj["Name_Stadion"],
                               obj['Capacity'],
                               obj['Destiny'],
                               obj['Working_stadion'])

            except AttributeError:
                print("Неверная структура")






if __name__ == "__main__":
    stadium_1 = Stadium('Camp-Nou', 93444, 'Football', False)
    print(stadium_1.get_name_stadium())
    print(stadium_1.get_capacity())
    print(stadium_1.get_destiny())
    print(stadium_1.get_working_stadium())
    print()

    my_pickle = Pickler()
    my_pickle.save_data(stadium_1, r'files/stadium.club')
    my_pickle.load_data(r'files/stadium.club')
    my_pickle.load_data(r'files/stadium.pkl')
    print()

    my_json = JSONDataAdapter.save_to_json(stadium_1, r'files/stadium.json')
    print(my_json)
    stadium_obj = JSONDataAdapter.load_from_json(r'files/stadium.json')
    print(stadium_obj)



