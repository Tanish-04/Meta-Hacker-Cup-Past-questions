arr = [[0] * 50 for _ in range(50)]
S = set()


def solve():
    N = int(input())

    for i in range(0, N):
        for j in range(0, N):
            arr[i][j] = input()

    ans1 = float('inf')
    ans2 = 0
    # rows
    for i in range(0, N):
        empty = []
        for j in range(0, N):
            if arr[i][j] == 'O':
                break

            if arr[i][j] == '.':
                empty.append(j)
        j += 1
        if j == N:
            c = len(empty)
            if c < ans1:
                ans1 = c
                ans2 = 0

            if c == 1:
                S.add((i,empty[0]))
            elif (c == ans1):
                ans2 += 1

    # Columns
    for j in range(0, N):
        empty = []
        for i in range(0, N):
            if arr[i][j] == 'O':
                break

            if arr[i][j] == '.':
                empty.append(i)
        i += 1
        if i == N:
            c = len(empty)
            if c < ans1:
                ans1 = c
                ans2 = 0

            if c == 1:
                S.add((empty[0],j))
            elif (c == ans1):
                ans2 += 1

    if ans1 == float('inf'):
        return "Impossible"
    else:
        if ans1 == 1:
            return ans1, len(S)
        else:
            return ans1, ans2


if __name__ == "__main__":
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: {}".format(i, solve()))
