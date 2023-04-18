from time import process_time
from multiprocessing import Process



def factorize(number):
    return [x for x in range(1, number + 1) if not number % x]


nums = (128, 255, 99999, 10651060)

def one_process(nums):
    for i in nums:
        factorize(i)
    print(process_time())


def multi_process(nums):
    processes = []
    for i in nums:
        process = Process(target=factorize, args=(i, ))
        process.start()
        processes.append(process)
    [el.join() for el in processes]
    [print(el.exitcode, end=' ') for el in processes]
    print(process_time())


if __name__ == "__main__":
   
    multi_process(nums)
    one_process(nums)
