n = int(input())
word_list = []
for _ in range(n):
    word_list.append(input())

# 단어의 중복을 제거하기 위해 set 자료구조로 변환 후 다시 list 자료구조로 변환!
word_list = list(set(word_list))

word_list.sort()            # 알파벳 순서로 정렬
word_list.sort(key=len)     # 문자열 길이 순서로 정렬

for word in word_list:
    print(word)
