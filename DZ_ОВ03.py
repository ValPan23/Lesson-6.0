#  Для сохранения информации о зоопарке в файл и возможность её загрузки, использовать модуль `pickle`
import pickle  # Импорт модуля pickle


# Базовый класс для всех животных в зоопарке
class Animal:
    def __init__(self, name, age):
        self.name = name  # Имя животного
        self.age = age    # Возраст животного

    def make_sound(self):
        # Метод для издания звуков, переопределяется в подклассах
        pass

    def eat(self):
        # Вывод сообщения о том, что животное ест
        print(f"{self.name} ест")


# Класс птиц (наследуется от Animal)
class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} говорит чирик")


# Класс млекопитающих (наследуется от Animal)
class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} говорит мяу")


# Класс рептилий (наследуется от Animal)
class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} говорит шшш")


# Класс смотрителей зоопарка
class ZooKeeper:
    def __init__(self, name):
        self.name = name  # Имя смотрителя

    def feed_animal(self, animal):  # Метод для кормления животных
        print(f"{self.name} кормит {animal.name}")


# Класс ветеринаров зоопарка
class Veterinarian:
    def __init__(self, name):
        self.name = name  # Имя ветеринара

    def heal_animal(self, animal):  # Метод для лечения животных
        print(f"{self.name} лечит {animal.name}")


# Класс зоопарка
class Zoo:
    def __init__(self):
        self.animals = []  # Список животных в зоопарке
        self.staff = []    # Список сотрудников зоопарка

    def add_animal(self, animal):  # Добавление животного в зоопарк
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк.")

    def add_staff(self, employee):  # Добавление сотрудника в зоопарк
        self.staff.append(employee)
        print(f"{employee.name} добавлен в зоопарк.")

    def print_animals(self):
        # Вывод списка всех животных в зоопарке
        print("Список всех животных в зоопарке:")
        for animal in self.animals:
            print(f"{animal.name}, возраст {animal.age}")

    def print_staff(self):
        # Вывод списка всех сотрудников зоопарка
        print("Список всех сотрудников зоопарка:")
        for employee in self.staff:
            print(employee.name)

    def save_to_file(self, filename):  # Сохранение состояния зоопарка в файл
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f"Состояние зоопарка сохранено в файл {filename}.")

    @staticmethod
    def load_from_file(filename):  # Загрузка состояния зоопарка из файла
        with open(filename, 'rb') as file:
            zoo = pickle.load(file)
        return zoo


# Создания объектов для зоопарка
zoo = Zoo()
# Добавление животных
zoo.add_animal(Bird("Воробей", 3))
zoo.add_animal(Mammal("Кот", 5))
zoo.add_animal(Reptile("Змея", 4))
# Добавление персонала
zoo.add_staff(ZooKeeper("Смотритель Гоша"))
zoo.add_staff(ZooKeeper("Смотритель Семен"))
zoo.add_staff(Veterinarian("Ветеринар Маша"))
# Сохранение состояния зоопарка с применением модуля `pickle`
zoo.save_to_file('zoo_state.pkl')
# Загрузка состояния зоопарка (после перезапуска программы) с применением модуля `pickle`
zoo = Zoo.load_from_file('zoo_state.pkl')

zoo.print_animals()  # Вывод списка всех животных
zoo.print_staff()    # Вывод списка всех сотрудников

# Каждое животное издает звуки
for animal in zoo.animals:
    animal.make_sound()

zookeeper1 = zoo.staff[0]
zookeeper2 = zoo.staff[1]
vet = zoo.staff[2]

zookeeper1.feed_animal(zoo.animals[1])  # Смотритель Гоша кормит Кота
zookeeper2.feed_animal(zoo.animals[0])  # Смотритель Семен кормит Воробья
vet.heal_animal(zoo.animals[2])         # Ветеринар Маша лечит Змею
