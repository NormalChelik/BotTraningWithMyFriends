from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

import parser

currency = parser.createCurrency()
print(currency)

all_valuete_kb = InlineKeyboardBuilder()

for i in range(0, len(currency)):
    all_valuete_kb.button(text=f"{currency[i]}", callback_data=f"{currency[i]}")
all_valuete_kb.button(text="◀️ Назад в главное меню", callback_data="backmenu")
all_valuete_kb.adjust(2)

