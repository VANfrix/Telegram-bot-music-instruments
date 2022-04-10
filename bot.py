import logging
from token_bot import bot_token
from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters, ConversationHandler
from muztorg import get_muztorg
from model_search_gitar import invite_model_search, search_name
logging.basicConfig(filename='bot.log', level=logging.INFO)

def start(update: Update, context: CallbackContext):
    text_greeting = "Привет, я бот для поиска гитар!\nЧто я умею:\n- искать гитару по определённым характеристикам"
    update.message.reply_text(text_greeting, reply_markup=main_keyboard())

def main_keyboard():
    keyboard = ReplyKeyboardMarkup([
        ['Показать гитары', 'Начать поиск']
    ], resize_keyboard=True)
    return keyboard

def get_main_keyboard(update: Update, context: CallbackContext):
    update.message.reply_text('Основное меню', reply_markup=main_keyboard())

def get_guitar_message(pages, search_string):
    guitars = get_muztorg(search_string)
    dict_list = ''
    for guitar in guitars[pages:pages+5]:
        name_=guitar['name_guitar']
        price_=guitar['price_guitar']
        available_=guitar['available_guitar']
        bonus_=guitar['bonus_guitar']
        search_new = f'\t{name_}\n цена {price_}\n {available_}\n бонусы {bonus_}\n\n'
        dict_list += search_new
    return dict_list

def search(update: Update, context: CallbackContext):
    pages = 0
    dict_list = get_guitar_message(pages, 'электрогитара')
    # print(len(dict_list))
    context.user_data["pages"] = pages+5
    update.message.reply_text(dict_list, reply_markup= ReplyKeyboardMarkup([['Далее', 'В основное меню']], resize_keyboard=True))

def search_next(update: Update, context: CallbackContext):
    pages = context.user_data["pages"]
    dict_list = get_guitar_message(pages, 'электрогитара')
    # print(len(dict_list))
    context.user_data["pages"] = pages+5
    update.message.reply_text(dict_list, reply_markup= ReplyKeyboardMarkup([['Далее', 'В основное меню']], resize_keyboard=True))
    
def news(update: Update, context: CallbackContext):
    update.message.reply_text('Здесь я покажу гитары', reply_markup=main_keyboard())

def search_by_model(update, context):
    text = update.message.text
    dict_list = get_guitar_message(0, text)
    update.message.reply_text(dict_list)

def main():
    mybot = Updater (bot_token, use_context=True)

    dp = mybot.dispatcher

    model_search = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Начать поиск)$'), invite_model_search)
            ],
        states={
            "model":[MessageHandler(Filters.text, search_name)]
        },
        fallbacks=[]
    )
    dp.add_handler(model_search)
    dp.add_handler(CommandHandler("start", start)) 
    dp.add_handler(MessageHandler(Filters.regex('^(Показать гитары)$'), search))
    dp.add_handler(MessageHandler(Filters.regex('^(Далее)$'), search_next))
    dp.add_handler(MessageHandler(Filters.regex('^(В основное меню)$'), get_main_keyboard))
    
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

main()