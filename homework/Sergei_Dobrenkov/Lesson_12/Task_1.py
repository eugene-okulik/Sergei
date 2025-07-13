# Создать классы цветов: общий класс для всех цветов и классы для нескольких
# видов.
# Создать экземпляры (объекты) цветов разных видов.
# Собрать букет (букет - еще один класс) с определением его стоимости.
# В букете цветы пусть хранятся в списке. Это будет список объектов.
#
# Для букета создать метод, который определяет время его увядания по среднему
# времени жизни всех цветов в букете.
#
# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
#
# Реализовать поиск цветов в букете по каким-нибудь параметрам
# (например, по среднему времени жизни) (и это тоже метод).

class Flower:
    def __init__(self, name, color, stem_length, price, life_days):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.life_days = life_days  # Время жизни (в днях)

    def __repr__(self):
        return (f"{self.name}({self.color}, {self.stem_length}см, "
                f"{self.price}р, {self.life_days}д)")


# Подклассы цветов
class Rose(Flower):
    def __init__(self, color, stem_length, price):
        super().__init__("Rose", color, stem_length, price, life_days=7)


class Aster(Flower):
    def __init__(self, color, stem_length, price):
        super().__init__("Aster", color, stem_length, price, life_days=10)


class Peonies(Flower):
    def __init__(self, color, stem_length, price):
        super().__init__("Peonies", color, stem_length, price, life_days=4)


# Класс букета
class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def total_price(self):
        return sum(flower.price for flower in self.flowers)

    def average_life(self):
        return sum(f.life_days for f in self.flowers) / len(self.flowers)

    def sort_by(self, attr):
        self.flowers.sort(key=lambda flower: getattr(flower, attr))

    def find_by_life_more_than(self, days):
        return [f for f in self.flowers if f.life_days > days]

    def __repr__(self):
        return f"Bouquet({self.flowers})"


# Создаем цветы
f1 = Rose("red", 40, 150)
f2 = Aster("yellow", 30, 80)
f3 = Peonies("white", 25, 50)
f4 = Rose("white", 50, 180)

# Собираем букет
bouquet = Bouquet([f1, f2, f3, f4])

# Общая стоимость
print("Стоимость:", bouquet.total_price())

# Средняя продолжительность жизни
print("Среднее время увядания:", bouquet.average_life())

# Сортировка по длине стебля
bouquet.sort_by("stem_length")
print("Сортировка по длине:", bouquet)

# Поиск цветов, живущих более 5 дней
long_living = bouquet.find_by_life_more_than(5)
print("Цветы с жизнью > 5 дней:", long_living)
