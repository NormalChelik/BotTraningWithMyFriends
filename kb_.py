from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

import pars

currency = pars.createCurrency()
list_currency = []
print("=================")
for n in currency:
    list_currency.append([n, currency[n]])
    print(n, currency[n])
print("=================")
all_valuete_kb = InlineKeyboardBuilder()
backmenu = InlineKeyboardBuilder()
backmenu.button(text="◀️ Назад в главное меню", callback_data="backmenu")

for i in range(len(list_currency)):
    all_valuete_kb.button(text=f"{list_currency[i][0]}", callback_data=f"{list_currency[i][1]}")
all_valuete_kb.adjust(2)
