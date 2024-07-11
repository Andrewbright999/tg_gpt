from aiogram import Router, F
from aiogram.types import Message
from gpt_4 import answer_to_question


router = Router()
router.message.filter(lambda message: message.message_thread_id == 202)


@router.message(F.text)
async def message_with_text(message: Message):
    answer = await answer_to_question(message.text)
    await message.answer(answer)
