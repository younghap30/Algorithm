a = int(input())
b = int(input())
c = int(input())

abc = a * b * c
abc_str = str(abc)

count = [0] * 10

for char in abc_str:
    count[int(char)] += 1

for i in range(0, 10):
    print(count[i])
