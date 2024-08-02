from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

from src.model.games import Game


user_base = ReplyKeyboardMarkup([['Узнать погоду', 'Ачивки'], ['Ввести ключ OpenXBL', 'Обновить игры', 'Аккаунт', 'Games'], ['Помощь']], resize_keyboard=True)

def game_page(games: Game):
    mass_buttons = []
    for game in games:
        mass_buttons.append([game.name])

    return ReplyKeyboardMarkup(mass_buttons, resize_keyboard=True)


#Кнопка "Оплатить покупку"
buy_button = InlineKeyboardButton('Оплатить покупку', callback_data="payment")

#Кнопка "Да"
yes = InlineKeyboardButton('Да', callback_data="yes")

#Кнопка "Нет"
no = InlineKeyboardButton('Нет', callback_data="no")

apply_order = InlineKeyboardButton('Взять в работу', callback_data="apply_order")

cancle_order = InlineKeyboardButton('Отменить заказ', callback_data="cancle_order")

co = InlineKeyboardMarkup([[cancle_order]])

admin_first = InlineKeyboardMarkup([[apply_order], [cancle_order]])

#Когда бот присылает админу квитанцию
apply_recipt = InlineKeyboardButton('Принять квитанцию', callback_data="apply_recipt")
cancle_recipt = InlineKeyboardButton('Отменить квитанцию', callback_data="cancle_recipt")
admin_recipt = InlineKeyboardMarkup([[apply_recipt], [cancle_recipt]])


complete_order = InlineKeyboardButton('Заказ выполнен', callback_data="complete_order")
error_order = InlineKeyboardButton('Не получилось выполнить заказ', callback_data="error_order")
admin_order = InlineKeyboardMarkup([[complete_order], [error_order]])


class Admin():
    def __init__(self) -> None:
        pass

    def admin_buttons(self):
        return ReplyKeyboardMarkup(
            [['Заказы'], ['Курс', 'Маржа', 'Переменные'], ['Калькулятор', 'Статистика', 'Админы']],
            resize_keyboard=True)

    def orders(self):
        return ReplyKeyboardMarkup([['В работе'], ['Заявки'], ['Выполненые', 'Отмененные'], ['Главное меню']], resize_keyboard=True)

    def course(self):
        return ReplyKeyboardMarkup([['Узнать курс'], ['Изменить курс'], ['Главное меню']], resize_keyboard=True)

    def marje(self):
        return ReplyKeyboardMarkup([['Узнать маржу'], ['Изменить маржу'], ['Главное меню']], resize_keyboard=True)

    def vars(self):
        return ReplyKeyboardMarkup([['Телефон'], ['Способ оплаты'], ['Главное меню']], resize_keyboard=True)

    def calculate(self):
        return ReplyKeyboardMarkup([['Рубль в доллары'], ['Доллар в рубль'], ['Главное меню']], resize_keyboard=True)

    def stats(self):
        return ReplyKeyboardMarkup([['Пользователи'],['Кол-во выполненых заказов'], ['Выручка'], ['Главное меню']], resize_keyboard=True)

    def admins(self):
        return ReplyKeyboardMarkup([['Список админов'],['Добавить админа', 'Удалить админа'], ['Главное меню']], resize_keyboard=True)

admin = Admin()