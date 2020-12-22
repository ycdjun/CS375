# Runtime: O(log(m+n))
def findMedianSortedArray(a, b):
    # Determine which array is bigger
    if (len(a) > len(b)):
        smaller = b
        bigger = a
    else:
        smaller = a
        bigger = b

    # Used to partition
    minNum = 0
    maxNum = len(smaller)

    while(minNum <= maxNum):
        # Used to partition into Lower and Higher
        partitionLower = (minNum + maxNum)//2
        partitionHigher = (len(a) + len(b) + 1)//2 - partitionLower

        # If partitionLower == 0, nothing is on left side
        # If partitionLower == len(smaller), partitionLower is the size of the smaller array and nothing is on right side

        maxPartitionLower = smaller[partitionLower-1] if partitionLower != 0 else float("-inf")
        minPartitionLower = smaller[partitionLower] if partitionLower != len(
            smaller) else float("inf")

        maxPartitionHigher = bigger[partitionHigher - 1] if partitionHigher != 0 else float("-inf")
        minPartitionHigher = bigger[partitionHigher] if partitionHigher != len(
            bigger) else float("inf")

        # Checks if the greatest element within the first half of the smaller array is less than or equal to the smallest element within the second half of the bigger array
        # Checks if the greatest element within the first half of the bigger array is less than or equal to the smallest element within the second half of the smaller array
        if(maxPartitionLower <= minPartitionHigher and maxPartitionHigher <= minPartitionLower):
            # If the total length of both arrays combined is odd or even
            if((len(a) + len(b)) % 2 == 0):
                return (max(maxPartitionLower, maxPartitionHigher) + min(minPartitionLower, minPartitionHigher))/2
            else:
                return max(maxPartitionLower, maxPartitionHigher)
        # Search left
        elif (maxPartitionLower > minPartitionHigher):
            maxNum = partitionLower - 1
        # Search right
        else:
            minNum = partitionLower + 1

# Runtime: O(nlogn)


def largestContiguousSubArraySum(A, low, high):
    # Check if there is only one element
    if low == high:
        return(A[low])
    else:
        # divide
        mid = (low + high)//2
        leftMax = float("-inf")
        rightMax = float("-inf")

        sum = 0

        # Find the sum of the current left and right subarray
        for i in range(mid, low - 1, -1):
            sum += A[i]
            if sum > leftMax:
                leftMax = sum
        sum = 0
        for i in range(mid+1, high + 1):
            sum += A[i]
            if sum > rightMax:
                rightMax = sum

        # Recursively find the maximum subarray sum for left, right, and mid
        return max(largestContiguousSubArraySum(A, low, mid),
                   largestContiguousSubArraySum(A, mid+1, high), leftMax + rightMax)


def main():
    a = [[1, 2, 3, 4, 6], [2, 4, 5, 6, 7]]
    b = [[5, 7, 11, 12], [20, 21, 25, 30, 40]]
    A = [[6, -2, -2, 20, -3, -2, 4], [6, -10, -5, 20, -3, -2, 4]]
    print(findMedianSortedArray(a[0], b[0]))
    print(findMedianSortedArray(a[1], b[1]))
    print(largestContiguousSubArraySum(A[0], 0, len(A[0]) - 1))
    print(largestContiguousSubArraySum(A[1], 0, len(A[1]) - 1))


main()

# Runtime Analysis of Algorithms:
# Q1: The runtime of this algorithm is O(log(m+n)). The algorithm runs in log time because the range of elements to traverse decreases after every iteration in the while loop. Depending on size of m,n, the runtime will be O(logm) or O(logn) depending on which one is bigger.
# Q2: The runtime of this algorithm is O(nlogn). The algorithm makes two recursive calls with inputs of size n/2. Utilizing the master theorem, T(n) = 2T(n/2) + O(n) which means the runtime complexity is O(n log n).
