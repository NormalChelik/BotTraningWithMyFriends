from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

import pars

currency = pars.createCurrency()
all_valuete_kb = InlineKeyboardBuilder()

for i in range(len(currency)):
    all_valuete_kb.button(text=f"{list(currency.keys())[i]}", callback_data=f"{currency[list(currency.keys())[i]]}")
all_valuete_kb.adjust(2)
