
 # arr = [[0]*26] * 26    Error occurs can write article
arr = [[0] * 26 for _ in range(26)]

   # Step 1: Create 2D array

def solve():

    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if i != j:
                arr[i][j] = float('inf')

    # Step 2:

    S = input()
    K = int(input())

    for i in range(0, K):
        a, b = input()

        arr[ord(a)-ord('A')][ord(b)-ord('A')] = 1

    for k in range(0, 26):
        for i in range(0, 26):
            for j in range(0, 26):
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

    ans = float('inf')
    for i in range(0, 26):
        curr = 0
        for c in S:
            curr += arr[ord(c)-ord('A')][i]
        ans = min(ans, curr)

    if ans == float('inf'):
        return -1
    else:
        return ans


if __name__ == "__main__":
    T = int(input())

    for i in range(1, T + 1):
        print("Case #{}: {}".format(i, solve()))
