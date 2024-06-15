import threading
import time

def func():
    print('ran')
    time.sleep(2)
    print('done')

x = threading.Thread(target=func)
x.start()
print(threading.active_count())