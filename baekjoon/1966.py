def check_order(first_order, arr):
    for item in arr:
        if item[1] > first_order:
            return True

    return False


n = int(input())

for i in range(n):
    tt = input().split()
    arr_size = int(tt[0])
    target = int(tt[1])
    order_cnt = 0

    arr = [int(x) for x in input().split()]
    qq = [(idx, x) for idx, x in enumerate(arr)]

    while len(qq) != 0:
        first_node = qq[0]
        del qq[0]

        if check_order(first_node[1], qq):
            qq.append(first_node)
        else:
            order_cnt += 1

            if first_node[0] == target:
                print(order_cnt)
                break

        # print(qq)
