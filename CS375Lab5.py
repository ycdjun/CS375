def coinChange(demoninations, N):
    # If N == 0, then it is impossible
    if N == 0:
        print("Not Possible")

    combos = {}

    # set i to the last index of demoninations
    i = len(demoninations)-1

    # Go through all demoninations
    while(i >= 0):
        # While the demonination is greater than N, keep using the largest demonination until N is no longer bigger than N
        while(N >= demoninations[i]):
            N -= demoninations[i]
            # if demonination has not been previously used, update the dictionary
            if demoninations[i] in combos:
                combos[demoninations[i]] += 1
            # update the current number of demoninations if it was found before
            else:
                combos[demoninations[i]] = 1

        i -= 1

    # Check if demoninations can sum up to N
    if N != 0:
        print("Not Possible")
    else:
        print(combos)
        print(len(combos))


def main():
    coinChange((1, 5, 10, 25, 100), 137)


main()
