import random
import time

def Naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:

            return i

    return -1

def Binary_search(l, target, low = None, high = None):

    if low == None:
        low = 0

    if high == None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if target == l[midpoint]:
        return midpoint
    elif target < l[midpoint]:
        return Binary_search(l, target, low, midpoint - 1)
    else: #target > list[midpoint]
        return Binary_search(l, target, midpoint + 1, high)


if __name__ == '__main__':
   # l = [1,5,6,7,4,18,14]
    #target = 18

    #print(Naive_search(l, target))
    #print(Binary_search(l, target))

    length = 10000                                        
    sorted_list = set()

    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))

    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        Naive_search(sorted_list, target)
    end = time.time()

    print("Naive search Time Taken: ", (end-start)/length)

    start = time.time()
    for target in sorted_list:
        Binary_search(sorted_list, target)
    end = time.time()

    print("Binary search Time Taken: ", (end-start)/length)        


