C = []
adj = []

def rec(i,parent):
    m = 0
    
    for j in range(adj[i]):
        if j != parent:
            m = max(m, rec(j,i))
    
    return C[i] + m

def solve():
    N = int(input())