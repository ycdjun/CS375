import random
import math
import numpy as np
import time

# Input:an ordered array A[1,...n] and a number k such that 1<=k<=#
# Output: the k-th smallest element in A


def randomizedSelection(A, k):
    pivot = random.choice(A)

    # Divides A into less, equal, or greater based on the pivot
    less = [i for i in A if i < pivot]
    greater = [i for i in A if i > pivot]
    equal = [i for i in A if i == pivot]

    #  Decides next path to recurse or if kth smallest element has been found
    if k <= len(less):
        return randomizedSelection(less, k)
    elif k > (len(less) + len(equal)):
        return randomizedSelection(greater, k - len(less) - len(equal))
    else:
        return pivot


# Input:an ordered array A[1,...n] and a number k such that 1<=k<=n
# Output: the k-th smallest element in A
def deterministicSelection(A, k):

    if len(A) <= 10:
        return sorted(A)[k-1]

    # Stores all elements divided into groups
    groupsof5 = []

    # Current group of 5
    current = []
    for i in range(len(A)):
        # Checks to see 5 elements are in the current list
        if i % 5 != 0 or i == 0:
            current.append(A[i])
        # Append the current list to groupsof5 if 5 elements are in the current list
        else:
            groupsof5.append(current)
            # resets the current to the first element to be added to the next current group of 5
            current = [A[i]]
    if len(current) > 0:
        groupsof5.append(current)

    # stores all the medians of the groupsof5
    medians = [group[(len(current)//2)] for group in groupsof5]

    # recursively find the median of medians
    median_of_medians = deterministicSelection(medians, len(medians)//2)

    less = [i for i in A if i < median_of_medians]
    greater = [i for i in A if i > median_of_medians]
    equal = [i for i in A if i == median_of_medians]

    if k <= len(less):
        return deterministicSelection(less, k)
    elif k > (len(less) + len(equal)):
        return deterministicSelection(greater, k - len(less) - len(equal))
    else:
        return median_of_medians


# Input:an unordered array A[1,...n] and a number k such that 1<=k<=n
# Output: the k-th smallest element in A
def quicksort(A, k):

    # Input:an unordered Array
    # Output: Sorted Array
    def helper(A):
        if len(A) > 1:
            pivot = random.choice(A)
            less = [i for i in A if i < pivot]
            greater = [i for i in A if i > pivot]
            equal = [i for i in A if i == pivot]
            return helper(less)+equal + helper(greater)
        else:
            return A
    return helper(A)[k-1]


def main():
    A = [4, 16, 19, 9, 17, 2, 11, 16, 8, 16, 9, 14, 9, 11, 8, 13, 10, 9, 14, 17]
    k = 10
    n = 10**7
    rand = [random.randint(0, n//100) for _ in range(n)]

    start = time.time()
    print(randomizedSelection(A, k))
    end = time.time()
    print(f"Runtime of randomizedSelection is {end - start}")

    start = time.time()
    print(deterministicSelection(A, k))
    end = time.time()
    print(f"Runtime of deterministicSelection is {end - start}")

    start = time.time()
    print(quicksort(A, k))
    end = time.time()
    print(f"Runtime of quickSort is {end - start}")

    start = time.time()
    print(randomizedSelection(rand, len(rand)//2))
    end = time.time()
    print(f"Runtime of randomizedSelection is {end - start}")

    start = time.time()
    print(deterministicSelection(rand, len(rand)//2))
    end = time.time()
    print(f"Runtime of deterministicSelection is {end - start}")

    start = time.time()
    print(quicksort(rand, len(rand)//2))
    end = time.time()
    print(f"Runtime of quickSort is {end - start}")


main()
