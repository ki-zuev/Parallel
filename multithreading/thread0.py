import threading
import time

start = time.perf_counter()

def something(seconds):
    print(f'start {seconds}')
    time.sleep(seconds)
    print(f'finish {seconds}')

threads = []

for _ in range(10):
    t = threading.Thread(target=something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()
print(finish-start)