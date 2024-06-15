import threading
import time

def count(n):
    for i in range(1, n+1):
        print(f'{i} from count()')
        time.sleep(0.3)

def count1(n):
    for i in range(1, n+1):
        print(f'{i} from count1()')
        time.sleep(0.5)


x = threading.Thread(target=count, args=(7,))
x.start()

y = threading.Thread(target=count1, args=(5,))
y.start()

print(f'Active number of threads are: {threading.active_count()}')

# if i have global i can use x.join(), y.join()