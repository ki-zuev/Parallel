import concurrent.futures
import time

start = time.perf_counter()

def something(seconds):
    print(f'start {seconds}')
    time.sleep(seconds)
    return f'finish {seconds}'

with concurrent.futures.ThreadPoolExecutor() as executer:
    secs = [5, 4, 3, 2, 1]
    # results = [executer.submit(something, sec) for sec in secs]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    results = executer.map(something, secs)
    for result in results:
        print(result)

finish = time.perf_counter()
print(finish-start)