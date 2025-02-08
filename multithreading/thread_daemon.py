from threading import Thread
import time

# Поток-демон — это поток, который выполняет задачи в фоновом режиме.
# Потоки-демоны полезны для выполнения задач, которые не являются критическими.
# Программа не ждет завершения работы потока-демона перед завершением.
# При завершении программы поток-демон автоматически завершается.

def show_timer():
    count = 0
    while True:
        count += 1
        time.sleep(1)
        print(f'Пршло {count} секунд...')

t = Thread(target=show_timer, daemon=True)
t.start()

time.sleep(5)
answer = input('Выйти\n')