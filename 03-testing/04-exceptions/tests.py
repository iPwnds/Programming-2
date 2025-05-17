import pytest
from book import Book

# Valid ISBN examples
valid_books = [
    ("Watchmen", "978-1779501127"),
    ("Python 101", "978 0134685991"),
    ("Clean Code", "9780132350884"),
]

# Invalid titles (empty strings)
invalid_titles = [
    ("", "978-1779501127"),
    ("", "9780132350884"),
]

# Invalid ISBNs (wrong checksum, wrong length, non-digit chars)
invalid_isbns = [
    ("Watchmen", "978-1779501128"),  # invalid checksum
    ("Python 101", "978-177950112"),  # too short
    ("Clean Code", "97801323508845"),  # too long
    ("Some Book", "9780A2350884"),     # contains letter
]

@pytest.mark.parametrize("title, isbn", valid_books)
def test_valid_creation(title, isbn):
    book = Book(title, isbn)
    assert book.title == title
    assert book.isbn == isbn

@pytest.mark.parametrize("title, isbn", invalid_titles)
def test_creation_with_invalid_title(title, isbn):
    with pytest.raises(RuntimeError):
        Book(title, isbn)

@pytest.mark.parametrize("title, isbn", invalid_isbns)
def test_creation_with_invalid_isbn(title, isbn):
    with pytest.raises(RuntimeError):
        Book(title, isbn)