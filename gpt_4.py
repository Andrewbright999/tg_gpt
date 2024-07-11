import time
from openai import AsyncOpenAI
from config import OPENAI_API_KEY

client = AsyncOpenAI(api_key=OPENAI_API_KEY)
async def answer_to_question(message_text):
    messages = [{"role": "user","content": message_text}]
    chat_completion = await client.chat.completions.create(model="gpt-4o",
                                                                messages=messages,
                                                                   temperature =  0.5)
    try:
        response = chat_completion.choices[0].message.content
        return response
    except:
        time.sleep(20)
        await answer_to_question(message_text)