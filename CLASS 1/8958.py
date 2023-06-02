t = int(input())

for _ in range(t):
    s = input()
    score_sum = 0
    score = 0
    for i in range(len(s)):
        if s[i] == "O":
            score += 1
            score_sum += score
        else:
            score = 0
    print(score_sum)
