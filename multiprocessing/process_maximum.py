import multiprocessing
import time

def find_max(lock, barrier, mas, res, array):
    local = max(mas)
    with lock:
        if local > res.value:
            res.value = local
    barrier.wait()
    for i in range(len(mas)):
        mas[i] = res.value
    array.append(mas)

def func(data, n):
    csize = len(data) // n
    processes = []
    result = multiprocessing.Value('i', 0)
    manager = multiprocessing.Manager()
    lock = multiprocessing.Lock()
    barrier = multiprocessing.Barrier(n)
    array = manager.list()
    for i in range(n):
        start = i*csize
        end = len(data) if i == n - 1 else (i + 1)*csize
        p = multiprocessing.Process(target=find_max, args=(lock, barrier, data[start:end], result, array))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    
    for i in array:
        print(i)

    return result.value

if __name__ == '__main__':
    data = [1, 7, 3, 9, 5, 11, 12, 6, 4, 10, 15, 16, 17, 18, 19]
    n = 4
    start = time.time()
    max_value = func(data, n)
    finish = time.time()
    print(f"{max_value}")
    print(finish-start)
