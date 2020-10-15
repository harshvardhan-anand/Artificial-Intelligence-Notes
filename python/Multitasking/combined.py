from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time

print('\n')


def t1():
    start = time.time()
    '''
    Function for thread 1
    '''
    count = 0
    print('t1 started')
    a = [6760, 8450, 3390, 7730, 9920, 9940, 5430]
    x = []
    for i in a:
        print(f"Processing value {count+1} in loop of t1")
        x.append(i**5)
        count += 1
    print("t1 done")
    end = time.time()
    return end-start


def t2():
    '''
    Function for thread 2
    '''
    start = time.time()
    count = 0
    print('t2 started')
    a = [6760, 8450, 3390, 7730, 9920, 9940, 5430]
    x = []
    for i in a:
        print(f"Processing value {count+1} in loop of t2")
        x.append(i**5)
        count += 1
    print('t2 done')
    end = time.time()
    return end-start


def main():
    print("\nPrinting line 1 from main thread")
    print("Printing line 2 from main thread")
    print("Printing line 3 from main thread\n")


def print_thread_info(future, futurex):
    try:
        future
    except Exception as e:
        print(e)
        return None
    print()
    print(f"{futurex}.cancel = {future.cancel()}")
    print(f'{futurex}.done = {future.done()}')
    print(f'{futurex}.running = {future.running()}')
    print(f'{futurex}.result = {future.result()}')


def print_process_info(process, processx):
    try:
        future
    except Exception as e:
        print(e)
        return None
    print()
    # print(f"{processx}.cancel = {process.cancel()}")
    # print(f'{processx}.done = {process.done()}')
    # print(f'{processx}.running = {process.running()}')
    print(f'{processx}.result = {process.result()}')


# creating context manager
with ThreadPoolExecutor(max_workers=2) as executor:
    future1 = executor.submit(t1)
    future2 = executor.submit(t2)
    main()
print('\n')
with ProcessPoolExecutor(max_workers=2) as executor:
    process1 = executor.submit(t1)
    process2 = executor.submit(t2)
    main()

print('\n')
print_thread_info(future1, 'future1')
print_thread_info(future2, 'future2')
print_process_info(process1, 'future1')
print_process_info(process2, 'future2')

print("\nEnd Main thread\n")
