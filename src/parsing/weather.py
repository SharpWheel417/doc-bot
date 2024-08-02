from telegram import Update
from telegram.ext import ContextTypes
import requests

from config import WEATHER_API_KEY, CITY
from src.model import users as u
from src.view import send as v

class Weather:
  def __init__(self, temp, feels_like, wind_speed, clouds) -> None:
    self.temp = temp
    self.feels_like = feels_like
    self.wind_speed = wind_speed
    self.clouds = clouds
    pass

url = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&units=metric&lang=ru&appid={WEATHER_API_KEY}'




def get_weather_by_city(city, update: Update, context: ContextTypes):
  url_city = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={WEATHER_API_KEY}'
  weather_data = requests.get(url_city).json()

  w = Weather(weather_data['main']['temp'], weather_data['main']['feels_like'], weather_data['wind']['speed'], weather_data['clouds']['all'])

  # Отправляем значения пользователюы
  v.sendmess(f'''Сейчас в городе {CITY} {w.temp}°C\nprint(Ощущается как, {w.feels_like} °C'\nСкорость ветра: {w.wind_speed}\n Облачность: {w.clouds})''', update=update, context=context)


def send_weather_for_all():
  users = u.get_all()

  try:
    weather_data = requests.get(url).json()

    w = Weather(weather_data['main']['temp'], weather_data['main']['feels_like'], weather_data['wind']['speed'], weather_data['clouds']['all'])
  except Exception as e:
    print(e)

  for user in users:
    v.sendmess_user_id(f'''Сейчас в городе {CITY} {w.temp}°C\nОщущается как, {w.feels_like} °C'\nСкорость ветра: {w.wind_speed}\nОблачность: {w.clouds})''', user.chat_id)



def get_weather(update: Update, context: ContextTypes) -> Weather:
  try:
    weather_data = requests.get(url).json()

    w = Weather(weather_data['main']['temp'], weather_data['main']['feels_like'], weather_data['wind']['speed'], weather_data['clouds']['all'])

  except Exception as e:
    print(e)

  return w

  # Отправляем значения пользователюы
  v.sendmess(f'''Сейчас в городе {CITY} {w.temp}°C\nprint(Ощущается как, {w.feels_like} °C'\nСкорость ветра: {w.wind_speed}\n Облачность: {w.clouds})''', update=update, context=context)


def send_weather_for_all(update: Update, context: ContextTypes):
  users = u.get_all()

  try:
    weather_data = requests.get(url).json()

    w = Weather(weather_data['main']['temp'], weather_data['main']['feels_like'], weather_data['wind']['speed'], weather_data['clouds']['all'])
  except Exception as e:
    print(e)

  # for user in users:
  #   v.sendmess_user_id(f'''Сейчас в городе {CITY} {w.temp}°C\nОщущается как, {w.feels_like} °C'\nСкорость ветра: {w.wind_speed}\nОблачность: {w.clouds})''', user.chat_id)
