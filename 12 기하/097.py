import sys

x1, y1 = map(int, sys.stdin.readline().split())
x2, y2 = map(int, sys.stdin.readline().split())
x3, y3 = map(int, sys.stdin.readline().split())

# CCW 공식
result = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

if result > 0:
    print(1)
elif result < 0:
    print(-1)
else:
    print(0)
