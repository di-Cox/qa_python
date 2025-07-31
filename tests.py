from main import BooksCollector
import pytest # type: ignore
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Добавление разных книг с корректными названиями, параметризованный тест
    @pytest.mark.parametrize("book_name", [
        "По ком звонит колокол",
        "Джон Ячменное Зерно",
        "Янки при дворе короля Артура"
    ])
    def test_add_new_book_adds_books(self, book_name):
        collector = BooksCollector()

        collector.add_new_book(book_name)

        assert book_name in collector.get_books_genre()

    # Добавляем книгу с недопустимым количеством символов (41)
    @pytest.mark.parametrize("invalid_number", [
        "",
        "A" * 41,
        "Янки из Коннектикута при дворе короля Артура"
    ])
    def test_add_new_book_invalid_number(self, invalid_number):
        collector = BooksCollector()

        collector.add_new_book(invalid_number)

        assert invalid_number not in collector.get_books_genre()

    # Добавляем две одинаковые книги, проверка дублирования
    def test_add_new_book_does_not_add_duplicate_books(self):
        collector = BooksCollector()

        collector.add_new_book("Джерри-островитянин")
        collector.add_new_book("Джерри-островитянин")

        assert list(collector.get_books_genre().keys()).count("Джерри-островитянин") == 1

    # Делаем проверку, что у добавленных книг отсутствует жанр
    def test_added_new_book_has_empty_genre(self):
        collector = BooksCollector()

        collector.add_new_book("Джон Ячменное Зерно")

        assert collector.get_book_genre("Джон Ячменное Зерно") == ""

    # Добавляем книге жанр и проверяем его
    @pytest.mark.parametrize("genre", ["Комедия", "Приключения"])
    def test_set_book_genre_valid_genre(self, genre):
        collector = BooksCollector()

        collector.add_new_book("Приключения Тома Сойера")
        collector.set_book_genre("Приключения Тома Сойера", genre)

        assert collector.get_book_genre("Приключения Тома Сойера") == genre

    # Проверяем, что название жанра возвращает нужную книгу
    def test_get_books_with_specific_genre_return_correct_books(self):
        collector = BooksCollector()

        collector.add_new_book("Война миров")
        collector.set_book_genre("Война миров", "Фантастика")

        assert collector.get_books_with_specific_genre("Фантастика") == ["Война миров"]

    # Проверяем возрастной рейтинг книг для детей
    @pytest.mark.parametrize("book_name, genre", [
        ("Колыбельная", "Ужасы"),
        ("Загадка Эндхауза", "Детективы")
    ])
    def test_get_books_for_children_age_restrictions_books(self, book_name, genre):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        assert book_name not in collector.get_books_for_children()

    # Проверяем что возможно добавить книгу в избранное
    def test_add_book_in_favorites_check_book_has_been_added(self):
        collector = BooksCollector()

        collector.add_new_book("Мартин Иден")
        collector.add_book_in_favorites("Мартин Иден")
        assert "Мартин Иден" in collector.get_list_of_favorites_books()

    # Добавляем несуществующую книгу в избранное
    def test_add_book_in_favorites_dont_not_add_unknown_book(self):
        collector = BooksCollector()
        collector.add_book_in_favorites("Время не ждет")

        assert collector.get_list_of_favorites_books() == []

    # Проверяем что книгу можно удалить из избранного.
    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()

        collector.add_new_book("Старик и море")
        collector.add_book_in_favorites("Старик и море")
        collector.delete_book_from_favorites("Старик и море")

        assert "Старик и море" not in collector.get_list_of_favorites_books()

        pass


        

