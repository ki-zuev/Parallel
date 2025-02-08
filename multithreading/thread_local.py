import threading
import time

# Create a thread-local storage object (1)
thread_local = threading.local()


def init_data(number):
    thread_local.number = number * 100


def show_data():
    print(f"Thread {threading.current_thread().name} has number {thread_local.number}")


def worker(number):
    init_data(number)

    for _ in range(4):
        time.sleep(1)
        show_data()


thread1 = threading.Thread(target=worker, name="A", kwargs={"number": 4})
thread2 = threading.Thread(target=worker, name="B", kwargs={"number": 5})

thread1.start()
thread2.start()

thread1.join()
thread2.join()