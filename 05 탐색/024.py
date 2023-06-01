import sys
sys.setrecursionlimit(10000)

N = int(input())


def is_prime(num):
    for i in range(2, int(num / 2 + 1)):
        if num % i == 0:
            return False
    return True


def dfs(number):
    if len(str(number)) == N:
        print(number)
    else:
        for i in [1, 3, 5, 7, 9]:
            if is_prime(number * 10 + i):
                dfs(number * 10 + i)


# 일의 자리 소수는 2, 3, 5, 7이므로 4가지 수에서만 시작
dfs(2), dfs(3), dfs(5), dfs(7)
