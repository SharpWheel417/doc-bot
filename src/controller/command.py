from telegram import Update
from telegram.ext import ContextTypes

### Комманда Старт ###
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await context.bot.send_message(chat_id=update.effective_chat.id, text="Кароче этот бот ковертирует:\n\ndoc,docx -> pdf\n\nСжимает html, css, js\n\nПросто скинь нужный файл, а он вернет тебе обработанный\n\nУдачи!")
