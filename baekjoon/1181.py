# https://www.acmicpc.net/problem/1181

num = int(input())

word_arr = []
word_dict = dict()

for i in range(num):
    temp_str = input()
    temp_size = len(temp_str)
    
    if temp_size in word_dict.keys():
        word_dict[temp_size].append(temp_str)
    else:
        word_dict[temp_size] = [temp_str]
    
target_arr = []
k_arr = list(word_dict.keys())
k_arr.sort()

for k in k_arr:
    new_arr = list(set(word_dict[k]))
    new_arr.sort()

    target_arr += new_arr

for t in target_arr:
    print(t)
