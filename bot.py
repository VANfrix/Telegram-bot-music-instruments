import logging
from token_bot import bot_token
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from model_search_gitar import invite_model_search, search_name
from handlers import start, search_next, search
from keyboard import get_main_keyboard
logging.basicConfig(filename='bot.log', level=logging.INFO)

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