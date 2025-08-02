import pytest

from main import BooksCollector

from conftest import fantasy_book, detective_book, child_book, comedy_book, horror_book


class TestBooksCollector:

    # Добавляем книгу в список
    def test_add_new_book_add_one_book_successfully(self, book_titles):
        book_titles.add_new_book(fantasy_book)

        assert len(book_titles.get_books_genre()) == 1

    # Добавляем две одинаковые книги, проверка дублирования
    def test_add_new_book_add_similar_books(self, book_titles):
        book_titles.add_new_book(fantasy_book)

        book_titles.add_new_book(fantasy_book)

        assert len(book_titles.get_books_genre()) == 1

    # Добавляем книгу с недопустимым количеством символов (41)
    def test_add_new_book_add_books_more_than_40_symbols(self, book_titles):
        name_book = 'Янки из Коннектикута при дворе короля Артура'

        book_titles.add_new_book(name_book)

        assert len(book_titles.get_books_genre()) == 0

    # Делаем проверку, что у добавленных книг отсутствует жанр
    def test_add_new_book_add_book_without_genre(self, book_titles):
        book_titles.add_new_book(fantasy_book)

        assert book_titles.get_books_genre().get(fantasy_book) == ''

    # Делаем проверку установки жанра книги
    def test_set_book_genre_get_genre_successfully(self, book_titles, prepare_books):
        assert book_titles.get_book_genre(fantasy_book) == 'Фантастика'

    # Проверяем, что название жанра возвращает нужную книгу
    def test_get_books_with_specific_genre_one_book_get_list_genre(self, book_titles, prepare_books):
        genre = 'Детективы'

        assert book_titles.get_books_with_specific_genre(genre) == [detective_book]

    # Проверяем возрастной рейтинг книг для детей
    def test_get_books_for_children_three_books_get_list_book(self, book_titles, prepare_books):
        assert book_titles.get_books_for_children() == [fantasy_book, child_book, comedy_book]

    # Тесты параметризацией с ожидаемым результатом как вы просили
    @pytest.mark.parametrize(
        'book, expected_result',
        [
            (fantasy_book, True),
            (horror_book, False),
            (detective_book, False),
            (child_book, True),
            (comedy_book, True),
        ]
    )
    # Делаем проверку, что в списке книг для детей нет книг для взрослых
    def test_get_books_for_children_adult_books_not_included_the_list(self, book_titles, prepare_books, book, expected_result):
        children_books = book_titles.get_books_for_children()

        assert book in children_books == expected_result

    # Проверяем, что возможно добавить книгу в избранное
    def test_add_book_in_favorites_add_one_books_successfully(self, book_titles, prepare_books):
        book_titles.add_book_in_favorites(fantasy_book)

        assert book_titles.get_list_of_favorites_books() == [fantasy_book]

    # Проверяем, что нельзя дважды добавить книгу в избранное
    def test_add_book_in_favorites_same_books(self, book_titles, prepare_books):
        book_titles.add_book_in_favorites(fantasy_book)
        book_titles.add_book_in_favorites(fantasy_book)

        assert len(book_titles.get_list_of_favorites_books()) == 1

    # Проверяем, что нельзя добавить книгу не из списка
    def test_add_to_favorites_unlisted_books(self, book_titles, prepare_books):
        book_titles.add_book_in_favorites('Время не ждет')

        assert len(book_titles.get_list_of_favorites_books()) == 0

    # Проверяем, что книгу можно удалить из избранного
    def test_delete_book_from_favorites_removes_book_successfully(self, book_titles, prepare_books):
        book_titles.add_book_in_favorites(fantasy_book)

        book_titles.delete_book_from_favorites(fantasy_book)

        assert book_titles.get_list_of_favorites_books() == []

    # Как я понял все задания проще выполнить используя фикстуры, тесты с параметризацией можно не использовать