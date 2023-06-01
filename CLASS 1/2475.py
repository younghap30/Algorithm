my_list = list(map(int, input().split()))
s = 0
for num in my_list:
    s += (num * num)
print(s % 10)
