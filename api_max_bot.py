import asyncio
import logging

from maxapi import Bot, Dispatcher, F
from maxapi.types import BotStarted, Command, MessageCreated
from maxapi.filters.callback_payload import CallbackPayload
from maxapi.types import (
    ChatButton, 
    LinkButton, 
    CallbackButton, 
    RequestGeoLocationButton, 
    MessageButton, 
    ButtonsPayload,
    RequestContactButton, 
    OpenAppButton,
    MessageCreated, 
    MessageCallback, 
    MessageChatCreated,
    CommandStart, 
    Command
)
from maxapi.utils.inline_keyboard import InlineKeyboardBuilder

# логгирование
logging.basicConfig(level=logging.INFO)

# инициализация
bot = Bot('хехехехе? ищи токен')
dp = Dispatcher()
startMessageBotInfo = "Здравствуйте! Я автоматический справочный помощник №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№'\n\n" \
    "Выберите тему, нажав кнопку с цифрой:"

kb = InlineKeyboardBuilder()

def kb_on_start():
     kb.row(CallbackButton( 
            text='№№№№№№№№№№№№№№№№№№№№№№№№?',
            payload="appointmentInfo",
            ))
     kb.row(CallbackButton(
            text='№№№№№№№№№№№№№№№№№№№№№№№№№№',
            payload="AboutHospitalize",
            ))
     kb.row(CallbackButton(
            text='№№№№№№№№№№№№№№№№№№№№№№№',
            payload="contactInfo",
            ))
     kb.row(CallbackButton(
            text='№№№№№№№№№№№№№№',
            payload="more",
            ))

# ответ бота на команду /start
@dp.message_created(Command('start'))
async def hello(event: MessageCreated):
    await event.message.answer(startMessageBotInfo, attachments=[kb.as_markup()])

# Ответ бота при нажатии "начать"
@dp.bot_started()
async def bot_started(event: BotStarted):
        
        await event.bot.send_message(
        chat_id=event.chat_id,
        text= startMessageBotInfo, attachments=[kb.as_markup()])

        
# запуск бота
async def main():
    kb_on_start()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
