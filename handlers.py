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
    context.user_data["pages"] = pages+5
    update.message.reply_text(dict_list, reply_markup= ReplyKeyboardMarkup([['Далее', 'В основное меню']], resize_keyboard=True))

def search_next(update: Update, context: CallbackContext):
    pages = context.user_data["pages"]
    dict_list = get_guitar_message(pages, 'электрогитара')
    context.user_data["pages"] = pages+5
    update.message.reply_text(dict_list, reply_markup= ReplyKeyboardMarkup([['Далее', 'В основное меню']], resize_keyboard=True))    

def news(update: Update, context: CallbackContext):
    update.message.reply_text('Здесь я покажу гитары', reply_markup=main_keyboard())

def search_by_model(update, context):
    text = update.message.text
    dict_list = get_guitar_message(0, text)
    update.message.reply_text(dict_list)