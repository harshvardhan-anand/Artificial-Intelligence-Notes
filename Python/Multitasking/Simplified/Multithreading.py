from concurrent.futures import ThreadPoolExecutor
import time

def t1(x):
    time.sleep(1)
    start = time.time()
    count = 0
    print(' t1 started')
    a = [6760, 8450, 3390, 7730, 9920, 9940, 5430]
    x = []
    for i in a:
        print(f" Processing value {count+1} in loop of t1")
        x.append(i**10)
        count += 1
    print(" t1 done")
    end = time.time()
    return end-start


def t2(x,y,z):
    time.sleep(1)
    start = time.time()
    count = 0
    print(' t2 started')
    a = [6760, 8450, 3390, 7730, 9920, 9940, 5430]
    x = []
    for i in a:
        print(f" Processing value {count+1} in loop of t2")
        x.append(i**10)
        count += 1
    print(' t2 done')
    end = time.time()
    return end-start

def main():
    print("\n Printing line 1 from main thread")
    print(" Printing line 2 from main thread")
    print(" Printing line 3 from main thread\n")


with ThreadPoolExecutor(max_workers=2) as executor:
    future1 = executor.submit(t1,1)
    future2 = executor.submit(t2,2,3,4)
    main()

print(f'\n Returned value from t1: {future1.result()}')
print(f' Returned value from 21: {future2.result()}')