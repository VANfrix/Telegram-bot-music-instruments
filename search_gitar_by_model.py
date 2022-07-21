from telegram import ReplyKeyboardRemove
def invite_model_search(update, context):
    update.message.reply_text(
        "Введите модель гитары для поиска",
        reply_markup=ReplyKeyboardRemove()
    )
    return "model"

# def search_name(update, context):
#     model_search = update.message.text
#     if model_search == :
#         update.message.reply_text("Пожалуйста введите модель гитары", )
#         return "model"
