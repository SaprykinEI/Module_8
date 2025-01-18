import pickle
import json


class Car:
    '''Модель автомобиля'''
    def __init__(self, brand, model, color, year, car_is_coming=True):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.car_is_coming = car_is_coming

    def get_brand(self):
        '''Информация о брэнде'''
        return self.brand

    def get_model(self):
        '''Информация о модели'''
        return self.model

    def get_color(self):
        '''Цвет авто'''
        return self.color

    def get_year(self):
        '''Год выпуска авто'''
        return self.year

    def get_car_is_coming(self):
        """Машина на ходу"""
        return self.car_is_coming

    def __str__(self):
        '''Полная информация о самолете'''
        return (f"Бренд: {self.get_brand()}\n"
                f"Модель: {self.get_model()}\n"
                f"Цвет: {self.get_color()}\n"
                f"Год выпуска: {self.get_year()}\n"
                f"Машина на ходу: {self.car_is_coming}")


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

class CarEncoder(json.JSONEncoder):

    def default(self, o):
        return {
            "Бренд": o.brand,
            "Модель авто": o.model,
            "Цвет": o.color,
            "Год выпуска": o.year,
            "Машина едет:": o.car_is_coming
        }

    def save_json(self, object, filename):
        """Преобразование объекта в json файл"""

        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(object, fp, cls=CarEncoder, ensure_ascii=False, indent=2)

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
    car = Car('BMW', 'M5', 'Black', 2024, False)
    print(car)
    print()
    my_pickle = Pickler()
    my_pickle.save_data(car, r'files/car.pkl')
    my_pickle.load_data(r'files/car.pkl')
    my_pickle.load_data('filename.pkl')
    print()
    json_file = CarEncoder()
    json_file.save_json(car, r'files/my_car.json')
    print(json_file.load_json(r'files/my_car.json'))
    json_file.load_json('my_car.json')
