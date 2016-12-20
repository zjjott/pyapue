import threading
from multiprocessing import Pool
mydata = threading.local()
mydata.number = 42
log = []


def f():
    items = mydata.__dict__.items()
    print mydata.__dict__
    items.sort()
    log.append(items)
    mydata.number = 11
    log.append(mydata.number)
    return log

p = Pool(2)
result = p.apply_async(f)
print result.get()
print log
thread = threading.Thread(target=f)
thread.start()
thread.join()
print log
