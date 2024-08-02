import threading
import schedule
import time

import src.parsing.weather as weather

lock = threading.Lock()
scheduler_thread = None


def run_scheduler():
    # Запуск шедулера каждый час
    schedule.every(1).day.at("09:00").do(lambda: run_with_lock(lambda: weather.send_weather_for_all(), arg=True))

    # Бесконечный цикл для запуска шедулера
    while True:
        schedule.run_pending()
        time.sleep(10)

def run_with_lock(func, arg):
    with lock:
        func()

# Остановка и завершение предыдущего потока, если он существует
if scheduler_thread is not None:
    scheduler_thread.join()

# Создание и запуск нового потока для шедулера
scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.start()