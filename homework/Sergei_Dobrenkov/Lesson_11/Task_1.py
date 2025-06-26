class Book:
    # Общие атрибуты для всех книг
    material = "бумага"
    has_text = True

    def __init__(self, title, author, pages, isbn, reserved=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved

    def get_info(self):
        if self.reserved:
            return (f'Название: {self.title}, Автор: {self.author}, '
                    f'страниц: {self.pages}, материал: {self.material}, '
                    f'зарезервирована')
        else:
            return (f'Название: {self.title}, Автор: {self.author}, '
                    f'страниц: {self.pages}, материал: {self.material}')


class Textbook(Book):
    def __init__(self, title, author, pages, isbn, subject, school_class,
                 has_exercises, reserved=False):
        super().__init__(title, author, pages, isbn, reserved)
        self.subject = subject
        self.school_class = school_class
        self.has_exercises = has_exercises

    def get_info(self):
        if self.reserved:
            return (f'Название: {self.title}, Автор: {self.author}, '
                    f'страниц: {self.pages}, предмет: {self.subject}, '
                    f'класс: {self.school_class}, зарезервирована')
        else:
            return (f'Название: {self.title}, Автор: {self.author}, '
                    f'страниц: {self.pages}, предмет: {self.subject}, '
                    f'класс: {self.school_class}')


# Создание 5 экземпляров книг
book1 = Book("Идиот", "Достоевский", 500, "1")
book2 = Book("Война и мир", "Толстой", 1225, "2")
book3 = Book("Преступление и наказание",
             "Достоевский", 600, "3")
book4 = Book("Мастер и Маргарита", "Булгаков", 470, "4")
book5 = Book("Анна Каренина", "Толстой", 800, "5")

# Отметим одну книгу как зарезервированную
book1.reserved = True

# Учебники
textbook1 = Textbook("Алгебра", "Иванов", 200, "6", "Математика", 9, True)
textbook2 = Textbook("История", "Петров", 180, "7", "История", 8, True)
textbook3 = Textbook("География", "Сидоров", 150, "8", "География", 7, False)

# Помечаем один как зарезервированный
textbook2.reserved = True

# Выводим информацию о книгах
print(book1.get_info())
print(book2.get_info())
print(book3.get_info())
print(book4.get_info())
print(book5.get_info())

print()
# Выводим информацию о учебниках
print(textbook1.get_info())
print(textbook2.get_info())
print(textbook3.get_info())
