from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON
from services.file_handling import book


def create_bookmarks_keyboard(**kwargs: int) -> InlineKeyboardMarkup:
    """
    :type kwargs: object
    """
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    for button in sorted(kwargs.values()):
        kb_builder.row(InlineKeyboardButton(
            text=f'{button} - {book[button][:100]}',
            callback_data=str(button)
        ))
    # Добавляем в клавиатуру в конце две кнопки "Редактировать" и "Отменить"
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON['edit_bookmarks_button'],
            callback_data='edit_bookmarks'),
        InlineKeyboardButton(
            text=LEXICON['cancel'],
            callback_data='cancel'),
        width=2)
    return kb_builder.as_markup()


def create_edit_keyboard(**kwargs: int) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    deleter=LEXICON["del"]
    for button in sorted(kwargs.values()):
        kb_builder.row(InlineKeyboardButton(
            text=f'{deleter} {button} - {book[button][:100]}', callback_data=('del '+str(button))))
    kb_builder.row(InlineKeyboardButton(text=LEXICON['cancel'], callback_data='cancel'))
    return kb_builder.as_markup()
