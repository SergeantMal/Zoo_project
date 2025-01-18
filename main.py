# Программа, реализующая зоопарк. В зоопарке работают сотрудники, которые ухаживают за животными.
# Реализовано с использованием классов, полиморфизма и композиции.


# Класс Животные

class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def eat(self):  # Метод еды
        print(f"{self.name} ест")

    def sleep(self):  # Метод сна
        print(f"{self.name} спит")

    def make_noise(self):  # Метод шума
        print(f"{self.name} издает шум")


# Дочерний класс Млекопитающие

class Mammal(Animal):
    def __init__(self, name: str, age: int, fur_color: str):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_noise(self):  # Метод шума
        print(f"{self.name} урчит")


# Дочерний класс Птицы

class Bird(Animal):
    def __init__(self, name: str, age: int, feather_color: str):
        super().__init__(name, age)
        self.feather_color = feather_color

    def make_noise(self):  # Метод шума
        print(f"{self.name} чирикает")


# Дочерний класс Рептилии

class Reptile(Animal):
    def __init__(self, name: str, age: int, scales_color: str):
        super().__init__(name, age)
        self.scales_color = scales_color

    def make_noise(self):  # Метод шума
        print(f"{self.name} шипит")


# Класс Сотрудники

class Personal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


# Дочерний класс Смотритель

class ZooKeeper(Personal):
    def feed_animal(self, animal: Animal):  # Метод кормления
        print(f"{self.name} кормит {animal.name}")
        animal.eat()


# Дочерний класс Ветеринар

class Veterinarian(Personal):
    def heal_animal(self, animal: Animal):  # Метод лечения
        print(f"{self.name} лечит {animal.name}")
        animal.sleep()


# Дочерний класс Уборщик

class CleaningWorker(Personal):
    def clean_cage(self, animal: Animal):  # Метод уборки
        print(f"{self.name} чистит клетку {animal.name}")


# Класс Зоопарк

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal: Animal):  # Метод добавления животного
        self.animals.append(animal)

    def add_staff(self, staff_member: Personal):  # Метод добавления сотрудника
        self.staff.append(staff_member)

    def list_animals(self):  # Метод вывода списка животных
        for animal in self.animals:
            if isinstance(animal, Mammal):
                print(f"{animal.name}, {animal.age} лет, цвет шерсти: {animal.fur_color}")
            elif isinstance(animal, Bird):
                print(f"{animal.name}, {animal.age} лет, цвет перьев: {animal.feather_color}")
            elif isinstance(animal, Reptile):
                print(f"{animal.name}, {animal.age} лет, цвет чешуи: {animal.scales_color}")

    def list_staff(self):  # Метод вывода списка сотрудников
        for staff_member in self.staff:
            print(f"{staff_member.name}, {staff_member.age} лет, {staff_member.__class__.__name__}")

    def save_zoo(self):  # Метод сохранения состояния зоопарка
        with open("zoo_state.txt", "w", encoding="utf-8") as file:
            for animal in self.animals:
                if isinstance(animal, Mammal):
                    file.write(f"Mammal,{animal.name},{animal.age},{animal.fur_color}\n")
                elif isinstance(animal, Bird):
                    file.write(f"Bird,{animal.name},{animal.age},{animal.feather_color}\n")
                elif isinstance(animal, Reptile):
                    file.write(f"Reptile,{animal.name},{animal.age},{animal.scales_color}\n")
            for staff_member in self.staff:
                file.write(f"{staff_member.__class__.__name__},{staff_member.name},{staff_member.age}\n")

    def load_zoo(self):  # Метод загрузки состояния зоопарка
        try:
            with open("zoo_state.txt", "r", encoding="utf-8") as file:
                for line in file:
                    data = line.strip().split(",")
                    if data[0] == "Mammal":
                        self.add_animal(Mammal(data[1], int(data[2]), data[3]))
                    elif data[0] == "Bird":
                        self.add_animal(Bird(data[1], int(data[2]), data[3]))
                    elif data[0] == "Reptile":
                        self.add_animal(Reptile(data[1], int(data[2]), data[3]))
                    elif data[0] in {"ZooKeeper", "Veterinarian", "CleaningWorker"}:
                        staff_class = globals()[data[0]]
                        self.add_staff(staff_class(data[1], int(data[2])))

            print("Состояние зоопарка успешно загружено!")
        except FileNotFoundError:
            print("Файл с состоянием зоопарка не найден!")



# Функция основного меню
def main():
    zoo = Zoo()

    while True:
        print("\n--- Меню ---")
        print("1. Загрузить зоопарк")
        print("2. Сохранить зоопарк")
        print("3. Создать новый зоопарк")
        print("4. Добавить животное")
        print("5. Добавить сотрудника")
        print("6. Управление зоопарком")
        print("7. Прослушать звуки животных")
        print("8. Вывести список животных")
        print("9. Вывести список сотрудников")
        print("10. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            zoo.load_zoo()
        elif choice == "2":
            zoo.save_zoo()
        elif choice == "3":
            zoo = Zoo()
            print("Создан новый зоопарк!")
        elif choice == "4":
            animal_type = input("Введите тип животного (Mammal, Bird, Reptile): ")
            name = input("Имя: ")
            age = int(input("Возраст: "))
            if animal_type == "Mammal":
                fur_color = input("Цвет шерсти: ")
                zoo.add_animal(Mammal(name, age, fur_color))
            elif animal_type == "Bird":
                feather_color = input("Цвет перьев: ")
                zoo.add_animal(Bird(name, age, feather_color))
            elif animal_type == "Reptile":
                scales_color = input("Цвет чешуи: ")
                zoo.add_animal(Reptile(name, age, scales_color))
        elif choice == "5":
            role = input("Введите профессию (ZooKeeper, Veterinarian, CleaningWorker): ")
            name = input("Имя: ")
            age = int(input("Возраст: "))
            staff_class = globals().get(role)
            if staff_class:
                zoo.add_staff(staff_class(name, age))
        elif choice == "6":
            zoo.list_staff()
            staff_name = input("Выберите сотрудника: ")
            staff_member = next((s for s in zoo.staff if s.name == staff_name), None)
            if isinstance(staff_member, ZooKeeper):
                zoo.list_animals()
                animal_name = input("Выберите животное: ")
                animal = next((a for a in zoo.animals if a.name == animal_name), None)
                if animal:
                    staff_member.feed_animal(animal)
            elif isinstance(staff_member, Veterinarian):
                zoo.list_animals()
                animal_name = input("Выберите животное: ")
                animal = next((a for a in zoo.animals if a.name == animal_name), None)
                if animal:
                    staff_member.heal_animal(animal)
            elif isinstance(staff_member, CleaningWorker):
                zoo.list_animals()
                animal_name = input("Выберите животное: ")
                animal = next((a for a in zoo.animals if a.name == animal_name), None)
                if animal:
                    staff_member.clean_cage(animal)
        elif choice == "7":
            for animal in zoo.animals:
                animal.make_noise()
        elif choice == "8":
            zoo.list_animals()
        elif choice == "9":
            zoo.list_staff()
        elif choice == "10":
            break
        else:
            print("Неверный выбор, попробуйте снова.")

# Запуск основного меню

if __name__ == "__main__":
    main()
