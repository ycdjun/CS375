# Input: string s and list of strings m
# Output: Possible setntence combinations

def spaceBar(s, m):
    memo = {}
    # Convert m into a set
    wordDict = set(m)
    # Helper function for subproblem

    def helper(s, wordDict):
        if s not in memo:
            result = []
            # Traverse through all the element of the dictionary
            for word in wordDict:
                # check if prefix exists in the dictionary
                if s[:len(word)] == word:
                    # Base Case
                    if len(s) == len(word):
                        result.append(word)

                    else:
                        # Recursively call helper to find other words later in the string
                        for w in helper(s[len(word):], wordDict):
                            result.append(word+" "+w)
            memo[s] = result
        return memo[s]

    return helper(s, wordDict)


def main():
    s1 = "amantentononewitheel"
    m1 = ["a", "an", "am", "ant", "ent", "tent", "man", "ten", "on", "one",
          "ton", "no", "none", "new", "with", "pass", "the", "he", "heel", "wit"]
    if len(spaceBar(s1, m1)) > 0:
        print("Yes")
    else:
        print("No")
    print(spaceBar(s1, m1))
    s2 = "amango"
    m2 = ["a", "am", "an", "man", "go"]
    if len(spaceBar(s2, m2)) > 0:
        print("Yes")
    else:
        print("No")
    print(spaceBar(s2, m2))


main()
