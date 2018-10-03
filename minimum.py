#determine the minimum member of a list of numbers 2 ways
import random

def min_n2(list):
#return minimum number in a list, O(n^2) time
    for i in list:
        is_min = True
        for j in list:
            if i > j:
                is_min = False
        if is_min:
            return i

def min_n(list):
#return minimum number in a list, O(n) time
    min = list[0]
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
    return min

def kth_min_nlogn(k, list):
# return kth minimum number in a list, O(nlog n) time
# from https://wiki.python.org/moin/TimeComplexity sort is O(nlog n)

    tmp = sorted(list)
    print tmp
    return tmp[k - 1]

def kth_min_n(k,list):
# return kth minimum number in a list, O(n) time

# optimization 1: store index of min, replace with max. find absolute min each iteration
# optimization 2: if k > n/2, find n-k max elements
    min = [''] * k
    min[0] = list[0]
    max = list[0]
    #first find min, max
    for num in list:
        if num < min[0]:
            min[0] = num
        if num > max:
            max = num
    #then fill in min + 1 until we get to kth min
    for round in range(1, k):
        min[round] = max
        for num in list:
            if num < min[round] and num > min[round - 1]:
                min[round] = num
    print min
    return min[k - 1]

def main():
    list = [353, 635, 132, 665, 382, 351, 925, 1000, 516, 429]#[random.randint(0, 1000) for x in range(10)]
    print list
    print min_n2(list)
    print min_n(list)

    print kth_min_nlogn(4, list)
    print kth_min_n(4, list)

main()
