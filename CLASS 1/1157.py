word = input().upper()
alph_list = list(set(word))
count_list = []

for alph in alph_list:
    temp = word.count(alph)
    count_list.append(temp)

if count_list.count(max(count_list)) >= 2:
    print('?')
else:
    print(alph_list[count_list.index(max(count_list))])
