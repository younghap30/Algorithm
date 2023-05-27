import sys
input_ = sys.stdin.readline
suNo, quizNo = map(int, input_().split())
numbers = list(map(int, input_().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)

for i in range(quizNo):
    s, e = map(int, input_().split())
    print(prefix_sum[e] - prefix_sum[s-1])
