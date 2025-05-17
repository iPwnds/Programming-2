import re

class Book:
    def __init__(self, title, isbn):
        if not title:
            raise RuntimeError("Title must not be empty")

        # Clean ISBN: remove spaces and dashes
        cleaned_isbn = re.sub(r'[\s-]', '', isbn)

        if not self.is_valid_isbn(cleaned_isbn):
            raise RuntimeError("Invalid ISBN")

        self._title = title
        self._isbn = isbn

    @property
    def title(self):
        return self._title

    @property
    def isbn(self):
        return self._isbn

    def is_valid_isbn(self, isbn):
        # ISBN must be 13 digits
        if len(isbn) != 13 or not isbn.isdigit():
            return False

        digits = list(map(int, isbn))
        total = 0
        for i, d in enumerate(digits):
            if i % 2 == 0:
                total += d
            else:
                total += 3 * d

        return total % 10 == 0