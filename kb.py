from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

all_valuete_kb = InlineKeyboardBuilder()
currency = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'z', 'x', 'p']
for i in range(0, len(currency)):
    all_valuete_kb.button(text=f"{currency[i]}", callback_data=f"{currency[i]}")
all_valuete_kb.button(text="◀️ Назад в главное меню", callback_data="backmenu")
all_valuete_kb.adjust(2)

