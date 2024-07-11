from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from gpt_4 import answer_to_question


router = Router()
router.message.filter(F.chat.type == "private")


@router.message(Command("start")) 
async def cmd_start(message: Message):
    await message.answer("Привет, я GPT-4o и помогу ответить на твой вопрос)")


@router.message(F.text)
async def message_with_text(message: Message):
    answer = await answer_to_question(message.text)
    await message.answer(answer)
