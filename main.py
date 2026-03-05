import asyncio
import logging
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pydantic import BaseModel

from config import BOT_TOKEN, RECIPIENTS

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ConsultationRequest(BaseModel):
    name: str
    phone: str
    message: str = "Без комментария"

# --- ФУНКЦИЯ СОЗДАНИЯ КНОПКИ (Спит до лучших времен) ---
def get_claim_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Я взял в работу", callback_data="claim_lead")]
    ])

@app.post("/api/new_request")
async def create_request(data: ConsultationRequest):
    clean_phone = data.phone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    if not clean_phone.startswith("+"):
        clean_phone = "+" + clean_phone

    text = (
        f"🆕 <b>НОВАЯ ЗАЯВКА С САЙТА</b>\n"
        f"➖➖➖➖➖➖➖➖➖➖\n"
        f"👤 <b>Имя:</b> {data.name}\n"
        f"💬 <b>Жалоба:</b> {data.message}\n"
        f"➖➖➖➖➖➖➖➖➖➖\n"
        f"📞 <b>Клиент:</b> <a href='tel:{clean_phone}'>{clean_phone}</a>\n"
    )

    count = 0
    for chat_id in RECIPIENTS:
        try:
            # === ЗДЕСЬ НАСТРОЙКА КНОПКИ ===
            # Сейчас кнопка ОТКЛЮЧЕНА (reply_markup=None).
            # Чтобы включить, читай инструкцию в файле "инструкция по добавлению.txt"
            
            await bot.send_message(
                chat_id=chat_id, 
                text=text, 
                parse_mode="HTML",
                reply_markup=None  # <-- СЕЙЧАС СТОИТ None (КНОПКИ НЕТ)
                # reply_markup=get_claim_keyboard() # <-- В БУДУЩЕМ РАСКОММЕНТИРОВАТЬ ЭТУ СТРОКУ
            )
            count += 1
        except Exception as e:
            logging.error(f"Ошибка отправки {chat_id}: {e}")

    return {"status": "success", "message": f"Sent to {count}"}

@app.on_event("startup")
async def on_startup():
    asyncio.create_task(dp.start_polling(bot))

@dp.callback_query(F.data == "claim_lead")
async def process_claim(callback: types.CallbackQuery):
    user_name = callback.from_user.full_name
    new_text = callback.message.html_text + f"\n\n✅ <b>ЗАБРАЛ(А): {user_name}</b>"
    try:
        await callback.message.edit_text(text=new_text, parse_mode="HTML", reply_markup=None)
        await callback.answer(text="Вы забрали заявку!")
    except Exception as e:
        logging.error(f"Ошибка редактирования: {e}")

app.mount("/", StaticFiles(directory="static", html=True), name="static")