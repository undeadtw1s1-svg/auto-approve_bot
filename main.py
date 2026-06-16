import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import ChatJoinRequest

bot = Bot(token="ТВОЙ_ТОКЕН")
dp = Dispatcher()

# заявка на вступление в канал
@dp.chat_join_request()
async def approve_request(chat_join: ChatJoinRequest):
    await chat_join.approve()
    
    try:
        await bot.send_message(
            chat_id=chat_join.from_user.id, 
            text="👋 Привет! Твоя заявка в наш закрытый канал одобрена.\n\n"
                 "🎁 Как и обещали, держи свой бонус за подписку: [Ссылка на крутой материал]"
        )
    except Exception:
        pass

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())