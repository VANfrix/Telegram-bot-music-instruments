from ast import Store
from distutils.ccompiler import show_compilers
import logging
from token_bot import bot_token
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters
from avito import get_avito
logging.basicConfig(filename='bot.log', level=logging.INFO)

def start(update: Update, context: CallbackContext):
    
    my_keyboard = ReplyKeyboardMarkup([['Найти гитару'],
    ['Присылать новости'],
    ['Ждать гитару мечты']
    ])
    text_greeting = "Привет, я бот для поиска объявлений по продаже гитар!\nЧто я умею:\n- искать гитару по определённым характеристикам\n- присылать новые объявления, нужно только меня об этом попросить)))\n- если ждёшь гитару мечты, я пришлю обявление, когда появится!"
    update.message.reply_text(text_greeting, reply_markup=my_keyboard)

guitars = get_avito()

def search(update: Update, context: CallbackContext):
    for guitar in guitars:
        name_=guitar['name_guitar']
        price_=guitar['price_guitar']
        saler_=guitar['name_saler']
        search_new = f'{name_} цена {price_} продаёт {saler_}'
        update.message.reply_text(search_new)
    
def news(update: Update, context: CallbackContext):
    update.message.reply_text('Здесь я буду присылать новые объявления')

def dream(update: Update, context: CallbackContext):
    update.message.reply_text('Здесь я пришлю объявление с гитарой твоей мечты')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater (bot_token, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", start )) 
    dp.add_handler(MessageHandler(Filters.regex('^(Найти гитару)$'), search))
    dp.add_handler(MessageHandler(Filters.regex('^(Присылать новости)$'), news ))
    dp.add_handler(MessageHandler(Filters.regex('^(Ждать гитару мечты)$'), dream ))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

main()