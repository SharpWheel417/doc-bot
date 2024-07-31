import subprocess
import os
from telegram import Update, Bot
from telegram.ext import CallbackContext
import subprocess

from config import ADMIN_ID
from ..view.send import sendmess, senddoc

terminal = subprocess.Popen(['gnome-terminal'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

async def handle_message(update: Update, context: CallbackContext):
    global terminal
    if context._user_id in ADMIN_ID:
        text = update.message.text
        # Выполняем команду
        # Создаем новый экземпляр терминала

        # Отправляем команду в терминал
        terminal.stdin.write(text.encode() + b'\n')

        # Получаем вывод команды
        output = ''
        while True:
            line = terminal.stdout.readline()
            if not line:
                break
            output += line.decode()
            print(output)

        await sendmess(output, update, context)