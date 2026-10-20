import pytest

import isbn_utils


def test_isbn10_valid():
    assert isbn_utils.isbn10_valid("074348858X")
    assert not isbn_utils.isbn10_valid("0743488589")
    assert not isbn_utils.isbn10_valid("XXXXXXXXXX")
    assert not isbn_utils.isbn10_valid("test")


def test_isbn13_valid():
    assert isbn_utils.isbn13_valid("9780743488587")


@pytest.mark.parametrize("isbn", ["", "0", "000000000", "074348858X0"])
def test_isbn10_rejects_incorrect_length(isbn: str) -> None:
    assert not isbn_utils.isbn10_valid(isbn)


@pytest.mark.parametrize("isbn", ["", "0", "000000000000", "97807434885870"])
def test_isbn13_rejects_incorrect_length(isbn: str) -> None:
    assert not isbn_utils.isbn13_valid(isbn)


assert not isbn_utils.isbn13_valid("test")


def test_isbn_valid():
    assert isbn_utils.isbn_valid("074348858X")
    assert isbn_utils.isbn_valid("9780743488587")
    assert not isbn_utils.isbn_valid(None)
    assert not isbn_utils.isbn_valid("test")


def test_find_isbn_in_text():
    assert isbn_utils.find_isbn_in_text("ISBN: 074348858X") == "074348858X"
    assert isbn_utils.find_isbn_in_text("ISBN: 0743488589") is None
    assert isbn_utils.find_isbn_in_text("ISBN: 978-0743488587") == "9780743488587"
