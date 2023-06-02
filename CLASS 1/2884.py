h, m = map(int, input().split())

if m >= 45:
    print(h, m - 45)
else:
    h = h - 1
    if h == -1:
        h = 23
    m = 60 - (45 - m)
    print(h, m)
