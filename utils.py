from telegram import InlineKeyboardButton, InlineKeyboardMarkup
def main_inline_keyboard():
    inlinekeyboard = [
        [
            InlineKeyboardButton("Нравится", callback_data='1'),
            InlineKeyboardButton("Не нравится", callback_data='-1')
        ]
    ]
    return InlineKeyboardMarkup(inlinekeyboard)