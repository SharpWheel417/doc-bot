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
        # terminal.stdin.write(text.encode() + b'\n')

        # # Получаем вывод команды
        # output = ''
        # while True:
        #     line = terminal.stdout.readline()
        #     if not line:
        #         break
        #     output += line.decode()
        #     print(output)

        print(text)

        mass = text.split(' ')

        print('mass: ' + str(mass))
        command = ['gnome-terminal', '-e', 'bash -c']

        list_files = subprocess.run(command + mass, stdout=subprocess.PIPE, text=True)
        print(list_files.returncode)

        await sendmess(list_files.stdout, update, context)