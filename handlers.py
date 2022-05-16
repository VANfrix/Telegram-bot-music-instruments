from telegram.ext import  CallbackContext
from telegram import ReplyKeyboardMarkup, Update
from keyboard import main_keyboard
from utils import get_guitar_message

def start(update: Update, context: CallbackContext):
    text_greeting = "Привет, я бот для поиска гитар!\nЧто я умею:\n- искать гитару по определённым характеристикам"
    update.message.reply_text(text_greeting, reply_markup=main_keyboard())

def search(update: Update, context: CallbackContext):
    pages = 0
    dict_list = get_guitar_message(pages, 'электрогитара')
    context.user_data["pages"] = pages+12
    update.message.reply_text(dict_list, reply_markup= ReplyKeyboardMarkup([['Далее', 'В основное меню']], resize_keyboard=True))

def search_next(update: Update, context: CallbackContext):
    pages = context.user_data["pages"]
    dict_list = get_guitar_message(pages, 'электрогитара')
    context.user_data["pages"] = pages+12
    update.message.reply_text(dict_list, reply_markup= ReplyKeyboardMarkup([['Далее', 'В основное меню']], resize_keyboard=True))

def search_by_model(update: Update, context: CallbackContext):
    text = update.message.text
    dict_list = get_guitar_message(0, text)
    update.message.reply_text(dict_list)
    print(text)

def get_main_keyboard(update: Update, context: CallbackContext):
    update.message.reply_text('Основное меню', reply_markup=main_keyboard())