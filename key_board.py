from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import CallbackContext

def main_keyboard():
    keyboard = ReplyKeyboardMarkup([
        ['Показать гитары', 'Начать поиск']
    ], resize_keyboard=True)
    return keyboard