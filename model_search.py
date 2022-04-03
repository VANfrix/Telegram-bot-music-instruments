from telegram import ReplyKeyboardRemove

def invite_model_search(update, context):
    update.message.reply_text(
        "Введите модель гитары для поиска",
        reply_markup=ReplyKeyboardRemove()
    )
    return "guitar_name"