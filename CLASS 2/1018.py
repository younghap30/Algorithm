n, m = map(int, input().split())
board = []
answer_candidate = []

# 보드를 입력받는다.
for k in range(n):
    board.append(input())

for a in range(n - 7):
    for b in range(m - 7):
        # 두 가지 케이스를 생각해 볼 수 있다.
        # 1. 인데스 합이 홀수인 칸은 검은색, 짝수인 칸은 흰색
        # 2. 인덱스 합이 홀수인 칸은 흰색, 짝수인 칸은 검은색

        index1 = 0
        index2 = 0

        for i in range(a, a + 8):
            for j in range(b, b + 8):
                current_color = board[i][j]
                if ((i + j) % 2 == 1 and current_color != "B") or ((i + j) % 2 == 0 and current_color != "W"):
                    index1 += 1
                if ((i + j) % 2 == 1 and current_color != "W") or ((i + j) % 2 == 0 and current_color != "B"):
                    index2 += 1

        answer_candidate.append(index1)
        answer_candidate.append(index2)

print(min(answer_candidate))
