n = int(input())
count = 1
start_index = 1
end_index = 1
s = 1

while end_index != n:
    if s == n:
        count += 1
        end_index += 1
        s += end_index
    elif s > n:
        s -= start_index
        start_index += 1
    else:
        end_index += 1
        s += end_index

print(count)
