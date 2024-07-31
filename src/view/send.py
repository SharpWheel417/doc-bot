from telegram import Update
from telegram.ext import ContextTypes

import telegram

async def sendmess(text: any, update: Update, context: ContextTypes):
  await context.bot.send_message(chat_id=update.effective_chat.id, text=str(text), parse_mode=telegram.ParseMode.MARKDOWN)

async def senddoc(f: any, text: any, update: Update, context: ContextTypes):
  await context.bot.send_document(chat_id=update.effective_chat.id, document=f, caption=str(text))