from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import  CallbackContext

def main_keyboard():
    keyboard = ReplyKeyboardMarkup([
        ['Показать гитары', 'Начать поиск']
    ], resize_keyboard=True)
    return keyboard

def get_main_keyboard(update: Update, context: CallbackContext):
    update.message.reply_text('Основное меню', reply_markup=main_keyboard())