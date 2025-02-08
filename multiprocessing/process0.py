import multiprocessing
import time

start = time.perf_counter()

def something(seconds):
    print(f'start {seconds}')
    time.sleep(seconds)
    print(f'finish {seconds}')

processes = []
for _ in range(10):
    p = multiprocessing.Process(target=something, args=[1.5])
    p.start()
    processes.append(p)
for process in processes:
    process.join()

finish = time.perf_counter()
print(finish-start)