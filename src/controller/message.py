import subprocess
import os
from telegram import Game, Update, Bot
from telegram.ext import CallbackContext
import subprocess

from config import ADMIN_ID
from model import achivment
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

            for achivment in achivments:
                await send_pi , f'Tag: {account.GamerTag}\nScore: {account.GamerScore}', update, context)








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