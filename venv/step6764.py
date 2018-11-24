#https://stepik.org/lesson/24459/step/15?unit=6764

def combination (n, k):
    if k > n:
        return 0
    elif k == 0:
        return 1
    else:
        return combination(n-1,k) + combination(n-1, k-1)

n, k = map(int, input().split())
combination(n, k)
