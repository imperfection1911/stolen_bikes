from app.search import Search
from config import Configuration
from telebot import types


class BotHandler:

    def __init__(self):
        self.config = Configuration()
        self.token = self.config.token
        self.search = Search()

    def start_menu(self):
        start_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        button1 = types.KeyboardButton('Поиск по госномеру')
        button2 = types.KeyboardButton('Поиск по производителю')
        button3 = types.KeyboardButton('Поиск по модели')
        start_markup.add(button1, button2, button3)
        return start_markup

    def state_number_search(self, state_number):
        return self.search.search_by_state_number(state_number)

