import random
# Input: an unordered array A[1,...,n]
# one of its longest palindromic subsequences.


def longestPalindromicSubsequence(A):

    # Setup
    S = [[0]*len(A)]*len(A)

    # Traversing every possible length of substrings
    for j in range(len(A)):
        for i in range(j, -1, -1):
            # Base Case where the start and end index are the same so S[i][j] = A[i] = A[j]
            if (i == j):
                S[i][j] = [A[i]]
            # Checks when were are two values
            elif(i == j - 1):
                # If there are the same, then it is a palindrome so append both values
                if(A[i] == A[j]):
                    S[i][j] = [A[i]] + [A[j]]
                else:
                    # Choose the first value
                    S[i][j] = [A[i]]
            # If the first and last values are the same, utilize previous solution and append current values
            elif(A[i] == A[j]):
                S[i][j] = [A[i]] + S[i+1][j-1] + [A[j]]
            # If they are not the same values, check for the longestPalindromicSubsequence and set s[i][j] to the previous solution
            elif(len(S[i+1][j]) >= len(S[i][j-1])):
                S[i][j] = S[i+1][j]
            else:
                S[i][j] = S[i][j-1]
    return(S[0][len(A)-1])


# Input: an array A[1,...,n] of n items and a budget W, Each item A[i] = [weight, value]
# Output: the highest total value of the items whose total weight is no more than W
def greedyKnapsack(A, W):

    total = 0

    # Sorting based on Value/Weight ratio
    sorted(A, key=lambda x: float(x[1])/x[0])

    # Keep using the greatest Value/Weight ratio item while W>0 and weight of item <= W
    while W > 0:
        temp = W
        for i in range(len(A)):
            # Subtract from weight and add to total and remove item from list
            if(A[i][0] <= W):
                W -= A[i][0]
                total += A[i][1]
                A.pop()
                break
        # When there are no longer items less than W in the list
        if temp == W:
            break

    return total

# Referenced from Textbook


def dynamicKnapsack(A, W):
    K = [[0 for i in range(len(A)+1)]for j in range(W+1)]

    for w in range(1, W+1):
        for j in range(1, len(A)+1):
            if (A[j-1][0] <= w):
                K[w][j] = max(K[w-A[j-1][0]][j-1]+A[j-1][1], K[w][j-1])
            else:
                K[w][j] = K[w][j-1]
    return K[W][len(A)]


# -----------------------------------------------------------------------------------------------------------------
A = [7, 2, 4, 6, 9, 11, 2, 6, 10, 6, 15, 6, 14, 2, 7, 5, 13, 9, 12, 15]
B = [7, 23, 31, 7,  5, 10, 1, 15, 1, 13, 7]
print(longestPalindromicSubsequence(B))
A = [random.randint(1, 101) for _ in range(1000)]
print(len(longestPalindromicSubsequence(A)))
# -----------------------------------------------------------------------------------------------------------------

A = [[96, 91], [96, 92], [96, 92], [97, 94], [98, 95], [100, 94], [100, 96], [102, 97], [103, 97], [104, 99], [
    106, 101], [107, 101], [106, 102], [107, 102], [109, 104], [109, 106], [110, 107], [111, 108], [113, 107], [114, 110]]
W = [100, 200, 300]
print(greedyKnapsack(A, W[0]))
print(greedyKnapsack(A, W[1]))
print(greedyKnapsack(A, W[2]))
# -----------------------------------------------------------------------------------------------------------------
A = [[96, 91], [96, 92], [96, 92], [97, 94], [98, 95], [100, 94], [100, 96], [102, 97], [103, 97], [104, 99], [
    106, 101], [107, 101], [106, 102], [107, 102], [109, 104], [109, 106], [110, 107], [111, 108], [113, 107], [114, 110]]
W = [100, 200, 300]
print(dynamicKnapsack(A, W[0]))
print(dynamicKnapsack(A, W[1]))
print(dynamicKnapsack(A, W[2]))
# -----------------------------------------------------------------------------------------------------------------
