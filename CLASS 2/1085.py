x, y, w, h = map(int, input().split())
answer_candidate = [x, y, w - x, h - y]
print(min(answer_candidate))
