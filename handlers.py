from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router

import kb

router = Router()
@router.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.username}, меня зовут Coursbot! Я смогу подсказать тебе текущий курс валюты. Выбери интересующую тебя валюту ниже!", reply_markup=kb.all_valuete_kb.as_markup())
@router.callback_query(F.data == 'backmenu')
async def a(clbck: CallbackQuery):
    await clbck.message.answer(f"Привет, меня зовут Coursbot! Я смогу подсказать тебе текущий курс валюты. Выбери интересующую тебя валюту ниже!", reply_markup=kb.all_valuete_kb.as_markup())

for n in kb.all_valuete_kb:
    @router.callback_query(F.data == f'{n}')               # Попытка сделать обработку InlineButton через цикл, лучше делать вручную
    async def a(clbck: CallbackQuery):
        for i in kb.currency:
            if F.data == i:
                await clbck.message.edit_text(f'{i}', reply_markup=kb.all_valuete_kb.as_markup())
