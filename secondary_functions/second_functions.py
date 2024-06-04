from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def univ_btnr(*args: list, width: int = 1, mod: str = 'inline', under_butn: str = None, **kwargs: dict[str, None]) \
        -> (InlineKeyboardBuilder | ReplyKeyboardBuilder):
    """ Угиверсальная функуия для преобразования списка в кнопки для клавиатуры
    :param under_butn: last button
    :param width: selection of parameters for keyboard lines
    :param mod: selection of parameters for keyboard
    """
    if mod == 'inline':

        keyboard_builder = InlineKeyboardBuilder()
        btn_list: list[InlineKeyboardButton] = []
        if args:
            btn_list.extend([InlineKeyboardButton(text=f'{i}', callback_data=i) for i in args])
        if kwargs:
            btn_list.extend([InlineKeyboardButton(text=f'{i}', callback_data=kwargs[i]) for i in kwargs])
        keyboard_builder.row(*btn_list, width=width)
        if under_butn:
            keyboard_builder.row(InlineKeyboardButton(text=under_butn, callback_data=under_butn))
        return keyboard_builder

    if mod == 'reply':
        keyboard_builder = ReplyKeyboardBuilder()
        btn_list: list[KeyboardButton] = []
        if args:
            btn_list.extend([KeyboardButton(text=f'{args[i]}') for i in range(len(args))])
        if kwargs:
            btn_list.extend([KeyboardButton(text=f'{kwargs[i]}') for i in kwargs])

        keyboard_builder.row(*btn_list, width=width)

        if under_butn:
            keyboard_builder.row(KeyboardButton(text=under_butn))
        return keyboard_builder
