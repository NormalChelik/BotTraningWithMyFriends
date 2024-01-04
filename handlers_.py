from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router

import kb_

router = Router()
@router.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.username}, меня зовут Coursbot! Я смогу подсказать тебе текущий курс валюты. Выбери интересующую тебя валюту ниже!", reply_markup=kb_.all_valuete_kb.as_markup())


@router.callback_query(F.data == 'backmenu')
async def backmenu(clbck: CallbackQuery):
    await clbck.message.edit_text(f"Привет, меня зовут Coursbot! Я смогу подсказать тебе текущий курс валюты. Выбери интересующую тебя валюту ниже!", reply_markup=kb_.all_valuete_kb.as_markup())

@router.callback_query(F.data.startswith(""))
async def inlinebuttons(clbck: CallbackQuery):
    await clbck.message.edit_text(clbck.data, reply_markup=kb_.all_valuete_kb.as_markup())



# F.data == 'a'
# await clbck.message.edit_text('a=1', reply_markup=kb.all_valuete_kb.as_markup())
