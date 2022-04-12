import multiprocessing
import random, time, sys
from multiprocessing import Pool, Process, Pipe

def parallel_quicksort(list, n):
    processes = 2 ** n
    result = list(list)

    pool = Pool(processes=processes)
    results = [(0, list)]

    while len(results) > 0:
        temp = pool.map(wrap, results)
        results = []
        for i, plist in temp:
            for ll in plist:
                if len(ll) == 1:
                    result[i] = ll[0]
                    i += 1
                elif len(ll) > 1:
                    results.append((i, ll))
                    i += len(ll)
    return result

def divide(a, min, max):
    random_int = random.randint(min, max)
    axis = a[random_int]
    swap(a, max, random_int)
    temporary = min
    for i in range(min, max):
        if a[i] < axis:
            swap(a, i, temporary)
            temporary = temporary + 1
    swap(a, max, temporary)
    return temporary


def swap(a, i, j):
    temporary = a[i]
    a[i] = a[j]
    a[j] = temporary

def wrap(input_list):
    index, list = input_list
    if len(list) <= 1:
        return [list]
    b = divide(list, 0, len(list) - 1)
    return (list, [list[:b], [list[b]], list[b + 1:]])


def main(argv):
    N = int(argv[1])
    with open(argv[0], "r") as myfile:
        lyst = [float(next(myfile)) for _ in range(N)]

    start = time.time()
    n = multiprocessing.cpu_count()
    lyst = parallel_quicksort(lyst, n)
    elapsed = time.time() - start
    print('Parallel quicksort: %f sec' % (elapsed))

    with open("result.txt", "w") as file:
        out_str = ""
        for i in lyst:
            out_str += str(i) + "\n"
        file.write(out_str)













if __name__ == '__main__':
    main(sys.argv[1:])