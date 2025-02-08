import  multiprocessing as mp

# Данные можно хранить в разделяемой памяти, используя объекты Value или Array.

def sharedMemDemo(targetNum, targetArr):
    targetNum.value = 3.1415927
    for i in range(len(targetArr)):
        targetArr[i] = -targetArr[i]

if __name__ == '__main__':
    myNum = mp.Value('d', 0.0)
    myArr = mp.Array('i', range(10))

    p = mp.Process(target=sharedMemDemo, args=(myNum, myArr))
    p.start()
    p.join()

    print(myNum.value)
    print(myArr[:])