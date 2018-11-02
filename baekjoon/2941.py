# https://www.acmicpc.net/problem/2941

s = input()

cro_arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
sll = 0

for i in range(len(s)):
    if sll != 0:
        sll -= 1
        continue
    
    s_1 = s[i:i+2]
    s_2 = s[i:i+3]

    # print(s[i], s_1, s_2)

    if s_1 in cro_arr:
        sll = 1
        cnt += 1
        # print(s_1, s_2)    
    elif s_1 in cro_arr:
        sll = 2
        cnt += 1
        # print(s_2, s_1)

for cro in cro_arr:
    s = s.replace(cro, '@')

s = s.replace('@', '')

print(len(s) + cnt)
