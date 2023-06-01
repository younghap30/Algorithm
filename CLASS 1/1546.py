n = int(input())
my_list = list(map(int, input().split()))
m = max(my_list)
s = 0
for i in my_list:
    s += i
print(s * 100 / len(my_list) / m)
