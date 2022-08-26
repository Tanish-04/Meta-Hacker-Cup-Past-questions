
def isVowel(s):
    if s == 'A' or s == 'E' or s == 'I' or s == 'O' or s == 'U':
        return True


def solution():

    string = input()
    ans = float('inf')
    # Outer loop for going through every alphabet to find minimum cost for consistent string
    for i in range(ord('A'), ord('Z') + 1):
        cost = 0
        # Inner loop going through string and if our outer alphabet is same as string do nothing and if it's different then use function
        # isVowel and add cost 2 if it is vowel and add cost 1 if it is not vowel
        for var in string:
            if var != chr(i):
                cost += 2 if isVowel(var) == isVowel(chr(i)) else 1
                

        ans = min(cost, ans)

    return ans


if __name__ == "__main__":
    numberOfbirthdays = int(input())

    for i in range(1, numberOfbirthdays + 1):
        print("Case #{}: {}".format(i, solution()))
