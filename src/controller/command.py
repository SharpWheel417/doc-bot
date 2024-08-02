from telegram import Update
from telegram.ext import ContextTypes

from src.model import users

import src.view.send as view
import src.view.buttons as buttons

from src.parsing.weather import get_weather

import config as config

### Комманда Старт ###
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

  u = users.User(update.effective_user.full_name, update.effective_chat.id)

  u.add()

  await context.bot.send_message(chat_id=update.effective_chat.id, text="Кароче этот бот ковертирует:\n\ndoc,docx -> pdf\n\nСжимает html, css, js\n\nПросто скинь нужный файл, а он вернет тебе обработанный\n\nУдачи!", reply_markup=buttons.user_base)


async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
  '''
    Отправка пользователю погоды
  '''

  w = get_weather()

  await view.sendmess(f'''Сейчас в городе {config.CITY} {w.temp}°C\nОщущается как, {w.feels_like} °C'\nСкорость ветра: {w.wind_speed}\nОблачность: {w.clouds})''', update=update, context=context)
