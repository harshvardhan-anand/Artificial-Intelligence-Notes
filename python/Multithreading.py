import threading as t
import time
class f1(t.Thread):
    def run(self):
        time.sleep(0)
        for _ in range(5):
            print(1)

class f2(t.Thread):
    def run(self):
        time.sleep(0)
        for _ in range(5):
            print(2)

t1 = f1()
t2 = f2()

t1.start()
t2.start()

t1.join()
t2.join()

print('Executed')