from telegram import ReplyKeyboardRemove

def invite_model_search(update, context):
    update.message.reply_text(
        "Введите модель гитары для поиска",
        reply_markup=ReplyKeyboardRemove()
    )
    return "model"

def search_name(update, context):
    user_search = update.message.text
    if len(user_search.split()) <2:
        update.message.reply_text("Пожалуйста введите модель гитары")
        return "model"
