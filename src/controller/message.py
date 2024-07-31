import subprocess
import os
from telegram import Update, Bot
from telegram.ext import CallbackContext
import subprocess

from config import ADMIN_ID
from ..view.send import sendmess, senddoc

# Получаем путь к дефолтному терминалу
terminal = subprocess.Popen(['gnome-terminal'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

async def handle_message(update: Update, context: CallbackContext):

  if context._user_id in ADMIN_ID:

    text = update.message.text
    # Выполняем команду
    # Создаем новый экземпляр терминала

    # Отправляем команду в терминал
    terminal.stdin.write(str(text))

    # Получаем вывод команды
    output, error = terminal.communicate()

    await sendmess("```"+output.decode()+"```", update, context)