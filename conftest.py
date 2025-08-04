import pytest

from main import BooksCollector

# Создание экземпляра, эта фикстура используется во всех тестах, инициализируя экземпляр класса.
@pytest.fixture
def collector():
    return BooksCollector()
