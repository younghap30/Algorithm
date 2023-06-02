s = input()
alpha_list = "abcdefghijklmnopqrstuvwxyz"

for alpha in alpha_list:
    if alpha in s:
        print(s.index(alpha), end=" ")
    else:
        print(-1, end=" ")
