import json,os
import sys
from Database.database_template import data_template
from aiogram.types import Message,CallbackQuery,callback_query

def databaser(message: Message |CallbackQuery| str = "", id='', data="", returner: bool = False) -> object:
    '''Функция для записи данных в базу данных.'''
    with open('Database\database.json', 'r') as dates:
        user_field = json.load(dates)

        if id:
            user_field[id] = data
        if isinstance(message,CallbackQuery):
            id = str(message.from_user.id)
            if id not in user_field:
                user_field[id] = user_field.setdefault(id, data_template)
        if isinstance(message, Message):
            id = str(message.from_user.id)
            if id not in user_field:
                user_field[id] = user_field.setdefault(id, data_template)
            user_field[str(message.from_user.id)]["message"].append(message.text)
    print(id, user_field[id])
    if returner:
        return id, user_field[id]
    with open('Database\database.json', 'w') as dates:
        json.dump(user_field, dates, indent=4)


def database_fields_updater() -> None:
    '''Функция для обновления и добавления новых полей в базу данных'''
    with open('Database\database.json', 'r') as rf:
        user_field = json.load(rf)
        for i in user_field:
            if 'administration' not in user_field[i]:
                user_field[i]['administration'] = False
            if 'change_number' not in user_field[i]['games']:
                user_field[i]['games']['change_number'] = {'tries': 7, 'all games': 0,
                                                           "in_game": False, "wins": 0, "loses": 0}

            if 'rock' not in user_field[i]['games']:
                user_field[i]['games']['rock'] = {'tries': 7, 'all games': 0, "in_game": False}

            if 'user_dict_template' not in user_field[i]:
                user_field[i]['user_dict_template'] = {'page': 1, 'bookmarks': {}}
    with open('Database\database.json', 'w') as dates:
        json.dump(user_field, dates, indent=4)


