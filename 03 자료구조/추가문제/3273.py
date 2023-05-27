n = int(input())
A = list(map(int, input().split()))
x = int(input())

A.sort()

count = 0
i = 0
j = n - 1
while i < j:
    if A[i] + A[j] == x:
        count += 1
        i += 1
        j -= 1
    elif A[i] + A[j] < x:
        i += 1
    else:
        j -= 1

print(count)
