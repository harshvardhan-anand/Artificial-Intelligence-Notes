from concurrent.futures import ProcessPoolExecutor
import time

print('\n')

def t1():
    time.sleep(2)
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
    time.sleep(2)
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


def print_process_info(process, processx):
    try:
        process
    except Exception as e:
        print(e)
        return None
    print()
    print(f"{processx}.cancel = {process.cancel()}")
    print(f'{processx}.done = {process.done()}')
    print(f'{processx}.running = {process.running()}')
    print(f'{processx}.result = {process.result()}')

# https://stackoverflow.com/a/45302590
# If you dont't use "if __name__ == '__main__':" then you will get error when running multiprocessing.


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=2) as executor:
        process1 = executor.submit(t1)
        process2 = executor.submit(t2)
        main()
    print('\n')
    time.sleep(2)    
    print_process_info(process1, 'Process1')
    print_process_info(process2, 'Process2')

    print("\nEnd Main thread\n")
