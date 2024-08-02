import subprocess
import os
from telegram import Game, Update, Bot
from telegram.ext import CallbackContext
import subprocess

from config import ADMIN_ID
from src.model.users import User
from ..view.send import send_pic, sendmess, senddoc, sendmess_buttons

from ..parsing import openxbl as xbox
from src.model.games import Game

from src.model.achivment import Achievement

import src.view.buttons as buttons

# TODO
# terminal = subprocess.Popen(['gnome-terminal'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

async def handle_message(update: Update, context: CallbackContext):

    text = update.message.text

    u = User('', update.effective_user.id, '', '').get()

    if u.stage == 'get_xapi':
        u.xapi = text
        u.stage = 'home'
        u.set_xapi()
        u.set_stage()
        await sendmess('Ключ установлен', update, context)
        return

    if u.stage == 'home':
        if text == 'Ввести ключ OpenXBL':
            u.stage = 'get_xapi'
            u.set_stage()
            await sendmess('Введи ключ', update, context)
            return

        if text == 'Обновить игры':
            xbox.update_games(u.get_id(), u.xapi)
            games = Game(u.get_id()[0], '', '').get_all()
            txt=''
            for game in games:
                txt+=f'{game.name}\n'

            await sendmess(txt, update, context)

        if text == 'Ачивки':
            games = Game(u.get_id()[0], '', '').get_all()
            u.stage = 'change_games'
            u.set_stage()
            await sendmess_buttons("Выбериет игру", buttons.game_page(games), update, context)

    if u.stage == 'change_games':
        game = Game(u.get_id()[0], text, '')
        game_id = game.get_game_id()
        achivments = xbox.get_achivments(game_id, u.xapi)
        i=0
        messages = []
        for achivment in achivments:
            if achivment.progressState == 'Achieved':
                continue
            if i > 5:
                # Append the achievement text to the messages list
                messages.append(f'{achivment.name}\n{achivment.description}\nСекретное: {achivment.isSecret}\nПрогресс: {achivment.progressState}\nG:{achivment.value}')
            else:
                # Display the achievement with image
                await send_pic(f=achivment.iconURL, text=f'{achivment.name}\n{achivment.description}\nСекретное: {achivment.isSecret}\nПрогресс: {achivment.progressState}\nG:{achivment.value}', update=update, context=context)
            i+=1


        if messages:
            # Split the messages into chunks of 2000 characters
            message_chunks = [messages[i:i+255] for i in range(0, len(messages), 255)]

            # Send each chunk as a separate message
            for i, chunk in enumerate(message_chunks):
                await sendmess('\n'.join(chunk), update=update, context=context)








    if text == 'Аккаунт':
        account = xbox.get_acc()
        await send_pic(account.GemrIconUrl, f'Tag: {account.GamerTag}\nScore: {account.GamerScore}', update, context)

    if text == 'Achievements':
        account = xbox.get_acc()
        await send_pic(account.GemrIconUrl, f'Tag: {account.GamerTag}\nScore: {account.GamerScore}', update, context)

    if text == 'Games':
        user = User(update.effective_user.name, update.effective_user.id, 'games')




# TODO
    # global terminal
    # if context._user_id in ADMIN_ID:

    #     print(text)

    #     output = os.popen(text).read()
    #     await sendmess(f'```bash\n{output}```', update, context)
    # await sendmess(f'```bash\nxs```', update, context)