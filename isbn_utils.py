import re
import string
from typing import Optional


def isbn10_valid(isbn: str) -> bool:
    if len(isbn) != 10:
        return False
    sum = 0
    for i, digit in enumerate(isbn):
        if digit in ("x", "X"):
            if i != 9:
                return False
            digit = 10
        if isbn[i] not in string.digits + "xX":
            return False
        sum += int(digit) * (10 - i)
        if i == 9:
            break
    return sum % 11 == 0


def isbn13_valid(isbn: str) -> bool:
    if len(isbn) != 13:
        return False
    for digit in isbn:
        if digit not in string.digits:
            return False
    check = (10 - (sum(int(digit) * (3 if idx % 2 else 1) for idx, digit in enumerate(isbn[:12])) % 10)) % 10
    return check == int(isbn[-1])


def clean_isbn(isbn: str) -> str:
    return isbn.lower().replace("-", "").replace("urn:isbn:", "").upper()


def isbn_valid(isbn: Optional[str]) -> bool:
    if isbn is None:
        return False
    isbn = clean_isbn(isbn)
    if len(isbn) == 10:
        return isbn10_valid(isbn)
    elif len(isbn) == 13:
        return isbn13_valid(isbn)
    else:
        return False


isbn_re = re.compile("([-0-9xX]+)")


def find_isbn_in_text(text: str) -> Optional[str]:
    for match in isbn_re.finditer(text):
        if isbn_valid(match.group(1)):
            return clean_isbn(match.group(1))
