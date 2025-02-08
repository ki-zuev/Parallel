import multiprocessing as mp

class MyAwesomeClass:
    def __init__(self):
        self.x = 100
    def __str__(self):
        return str(self.x)
    def change(self):
        self.x = 600

def changer(obj):
    tmp = obj[0]
    tmp.x = 500
    obj[0] = tmp
    print('Hello! ',obj[0])
    tmp.change()
    obj[0] = tmp
    print('Hello! ',obj[0])
    tmp.x += 1
    obj[0] = tmp
    print('Hello! ',obj[0])

if __name__ == '__main__':
    manager = mp.Manager()
    sharedList = manager.list()
    MAC = MyAwesomeClass()
    sharedList.append(MAC)
    p = mp.Process(target = changer, args=(sharedList,))
    p.start()
    p.join()					
    print('Here I am: ', sharedList[0])