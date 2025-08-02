import pytest

from main import BooksCollector


@pytest.fixture(scope="function")
def book_titles():
    collector = BooksCollector()
    return collector

fantasy_book = 'Война миров'
horror_book = 'Колыбельная'
detective_book = 'Загадка Эндхауза'
child_book = 'Незнайка на луне'
comedy_book = 'Короли и капуста'

@pytest.fixture(scope="function")
def prepare_books(book_titles):
    books_genre = [
        (fantasy_book, "Фантастика"),
        (horror_book, "Ужасы"),
        (detective_book, "Детективы"),
        (child_book, "Мультфильмы"),
        (comedy_book, "Комедии"),
    ]

    for book, genre in books_genre:
        book_titles.add_new_book(book)
        book_titles.set_book_genre(book, genre)