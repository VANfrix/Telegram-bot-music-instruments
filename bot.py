import logging
from token_bot import bot_token
from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters, ConversationHandler
from avito import get_avito
from model_search_gitar import invite_model_search, search_name
logging.basicConfig(filename='bot.log', level=logging.INFO)



def start(update: Update, context: CallbackContext):
    text_greeting = "Привет, я бот для поиска объявлений по продаже гитар!\nЧто я умею:\n- искать гитару по определённым характеристикам\n- присылать новые объявления, нужно только меня об этом попросить)))\n- если ждёшь гитару мечты, я пришлю обявление, когда появится!"
    update.message.reply_text(text_greeting, reply_markup=main_keyboard())

def get_guitar_message(pages, search_string):
    guitars = get_avito(search_string)
    dict_list = ''
    for guitar in guitars[pages:pages+10]:
        name_=guitar['name_guitar']
        price_=guitar['price_guitar']
        saler_=guitar['name_saler']
        place_=guitar['place_guitar']
        search_new = f'\t{name_}\n цена {price_}\n продаёт {saler_}\n место {place_}\n\n'
        dict_list += search_new
    return dict_list

def search(update: Update, context: CallbackContext):
    pages = 0
    dict_list = get_guitar_message(pages)
    # print(len(dict_list))
    context.user_data["pages"] = pages+10
    update.message.reply_text(dict_list, reply_markup= ReplyKeyboardMarkup([['Далее', 'В основное меню']]))

def search_next(update: Update, context: CallbackContext):
    pages = context.user_data["pages"]
    dict_list = get_guitar_message(pages, 'электрогитара')
    # print(len(dict_list))
    context.user_data["pages"] = pages+10
    update.message.reply_text(dict_list, reply_markup= ReplyKeyboardMarkup([['Далее', 'В основное меню']]))
    
def news(update: Update, context: CallbackContext):
    update.message.reply_text('Здесь я буду присылать новые объявления', reply_markup=main_keyboard())

def dream(update: Update, context: CallbackContext):
    update.message.reply_text('Здесь я пришлю объявление с гитарой твоей мечты', reply_markup=main_keyboard())

def main_keyboard():
    return ReplyKeyboardMarkup

def search_by_model(update, context):
    text = update.message.text
    dict_list = get_guitar_message(0, text)
    update.message.reply_text(dict_list)

def main_keyboard():
    return ReplyKeyboardMarkup([
        ['Показать гитары', 'Присылать новости', 'Ждать гитару мечты', 'Начать поиск']
    ])

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
    dp.add_handler(MessageHandler(Filters.regex('^(Присылать новости)$'), news ))
    dp.add_handler(MessageHandler(Filters.regex('^(Ждать гитару мечты)$'), dream ))
    # dp.add_handler(MessageHandler(Filters.regex('^(Далее)$'), search_next))
    dp.add_handler(MessageHandler(Filters.regex('^(В основное меню)$'), main_keyboard))
    
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

main()