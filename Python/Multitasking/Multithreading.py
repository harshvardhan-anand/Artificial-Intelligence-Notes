import threading as t
import time

def funk1(arg):
    # time.sleep(1)
    for i in range(arg):
        print(arg, end='   ')

def funk2(arg):
    time.sleep(3)
    for i in range(arg):
        print(arg, end='    ')

print(1)
t1 = t.Thread(target=funk1, args=(10,))
t2 = t.Thread(target=funk2, args=(20,))

t1.start()
t2.start()

t1.join()
print('2sadasda')
t2.join()

print('Executed')