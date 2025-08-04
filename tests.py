import pytest


class TestBooksCollector:

    # Проверяем добавление новой книги
    def test_add_new_book_successfully_adds_book(self, collector):
        collector.add_new_book("Война миров")
        assert collector.get_books_genre() == {"Война миров": ""}

    # Проверяем, что дубликаты не добавляются
    def test_add_new_book_rejects_duplicate_books(self, collector):
        collector.add_new_book("Война миров")
        collector.add_new_book("Война миров")
        assert len(collector.get_books_genre()) == 1

    # Проверяем, что нельзя добавить книгу с названием > 40 символов
    def test_add_new_book_rejects_book_with_long_title(self, collector):
        long_title = "А" * 41
        collector.add_new_book(long_title)
        assert long_title not in collector.get_books_genre()

    # Проверяем установку жанра
    def test_set_book_genre_sets_valid_genre(self, collector):
        collector.books_genre = {"Война миров": ""}
        collector.set_book_genre("Война миров", "Фантастика")
        assert collector.books_genre["Война миров"] == "Фантастика"

    # Проверяем, что метод возвращает жанр по названию книги
    # Замечания по ревью Тест проверяет только get_book_genre, данные создаются на прямую в тесте
    # Другие методы не используются.
    def test_get_book_genre_returns_correct_genre(self, collector):
        collector.books_genre = {"Незнайка на луне": "Мультфильмы"}
        assert collector.get_book_genre("Незнайка на луне") == "Мультфильмы"

    # Проверяем, что возвращается полный словарь книг и жанров
    # Тест проверяет только get_books_genre
    # Словарь создан на прямую для сравнения
    def test_get_books_genre_returns_correct_dict(self, collector):
        expected = {"Шерлок Холмс": "Детективы"}
        collector.books_genre = expected
        assert collector.get_books_genre() == expected

    # Проверка: метод возвращает только книги заданного жанра
    def test_get_books_with_specific_genre_returns_only_that_genre(self, collector):
        collector.books_genre = {
            "Война миров": "Фантастика",
            "Шерлок Холмс": "Детективы",
            "Звёздные войны": "Фантастика"
        }
        result = collector.get_books_with_specific_genre("Фантастика")
        assert set(result) == {"Война миров", "Звёздные войны"}

    # Проверка: метод возвращает только детские жанры
    def test_get_books_for_children_returns_only_allowed_genres(self, collector):
        collector.books_genre = {
            "Война миров": "Фантастика",
            "Колыбельная": "Ужасы",
            "Незнайка": "Мультфильмы",
            "Загадка Эндхауза": "Детективы"
        }
        result = collector.get_books_for_children()
        assert set(result) == {"Война миров", "Незнайка"}

    # Параметризованный тест: список книг для детей
    @pytest.mark.parametrize(
        "books_genre, expected_result",
        [
            (
                {
                    "Война миров": "Фантастика",
                    "Колыбельная": "Ужасы",
                    "Загадка Эндхауза": "Детективы",
                    "Незнайка на луне": "Мультфильмы",
                    "Короли и капуста": "Комедии"
                },
                {"Война миров", "Незнайка на луне", "Короли и капуста"}
            )
        ]
    )
    def test_get_books_for_children_parametrized(self, collector, books_genre, expected_result):
        collector.books_genre = books_genre
        result = set(collector.get_books_for_children())
        assert result == expected_result

    # Проверка: книга успешно добавляется в избранное
    def test_add_book_in_favorites_adds_book(self, collector):
        collector.books_genre = {"Война миров": "Фантастика"}
        collector.add_book_in_favorites("Война миров")
        assert collector.get_list_of_favorites_books() == ["Война миров"]

    # Проверка: нельзя дважды добавить книгу в избранное
    def test_add_book_in_favorites_does_not_duplicate(self, collector):
        collector.books_genre = {"Война миров": "Фантастика"}
        collector.add_book_in_favorites("Война миров")
        collector.add_book_in_favorites("Война миров")
        assert collector.get_list_of_favorites_books() == ["Война миров"]

    # Проверка: нельзя добавить книгу, которой нет в общем списке
    def test_add_book_in_favorites_ignores_unknown_books(self, collector):
        collector.add_book_in_favorites("Неизвестная книга")
        assert collector.get_list_of_favorites_books() == []

    # Проверка: книга удаляется из избранного
    def test_delete_book_from_favorites_removes_book(self, collector):
        collector.books_genre = {"Война миров": "Фантастика"}
        collector.add_book_in_favorites("Война миров")
        collector.delete_book_from_favorites("Война миров")
        assert collector.get_list_of_favorites_books() == []

    # Проверка: метод возвращает текущий список избранного
    # Тест проверяет только get_list_of_favorites_books,
    # Данные создаются вручную без вызова других методов
    def test_get_list_of_favorites_books_returns_expected_list(self, collector):
        collector.favorites = ["Война миров", "Незнайка"]
        assert collector.get_list_of_favorites_books() == ["Война миров", "Незнайка"]

