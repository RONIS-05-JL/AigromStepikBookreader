import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    """ Получение текста
    :param text: текст
    :param start: начало части
    :param size: размер части
    :return: часть текста"""
    end = start + size
    text_part = text[start:start + size]
    if text[end - 1:end] in "?,.!:;" and text[end:end + 1] not in "?,.!:;":
        return text_part, len(text_part)
    else:
        for i in range(2, size):
            if text_part[size - i - 1:size - i] in "?,.!:;":
                text_part = text_part[:size - i]
                return text_part, len(text_part)


def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as book_text:
        text = book_text.read().lstrip()
        start = 0
        for i in range(1, len(text) // 2):
            page, page_len = _get_part_text(text, start, PAGE_SIZE)
            if page_len == 0:
                break
            book[i] = page.lstrip()
            start += page_len


prepare_book(os.path.join(sys.path[1], os.path.normpath(BOOK_PATH)))

