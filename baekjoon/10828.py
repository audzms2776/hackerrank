stack_arr = []


def stack_push(x):
    stack_arr.append(x)
    return None


def stack_pop():
    if len(stack_arr) != 0:
        temp = stack_arr[-1]
        del stack_arr[-1]
        return temp
    else:
        return -1


def stack_size():
    return len(stack_arr)


def stack_empty():
    if len(stack_arr) == 0:
        return 1
    else:
        return 0

    
def stack_top():
    if len(stack_arr) != 0:
        return stack_arr[-1]
    else:
        return -1


def stack_func(c, n):
    func_dict = {
        'pop': stack_pop,
        'size': stack_size,
        'empty': stack_empty,
        'top': stack_top
    }

    if c == 'push':
        stack_push(n)
    else:
        print(func_dict[c]())


if __name__ == "__main__":
    n = int(input())

    for i in range(n):
        ss = input()
        cmd = ''
        num = 0

        tt = ss.split(' ')
        cmd = tt[0]

        if len(tt) > 1:    
            num = tt[1]

        stack_func(cmd, num)

