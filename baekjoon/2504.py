def is_int(i):
    try:
        int(i)
        return True
    except:
        return False


def is_good(ss):
    temp_stack = []

    try:
        for c in ss:
            if c == '(' or c == '[':
                temp_stack.append(c)
            elif c == ')' and temp_stack[-1] == '(':
                temp_stack.pop()
            elif c == ']' and temp_stack[-1] == '[':
                temp_stack.pop()
            else:
                return False

        return True
    except:
        return False


s = input()

if not is_good(s):
    print(0)
    exit()

m_stack = []

for i in s:
    if i == '(' or i =='[' or is_int(i) :
        m_stack.append(i)
    else:
        temp = m_stack[-1]

        if i == ')' and temp == '(':
            m_stack.pop()
            m_stack.append(2)
        elif i == ']' and temp == '[':
            m_stack.pop()
            m_stack.append(3)
        elif i == ')':
            m_stack.pop()
            m_stack.pop()
            m_stack.append(int(temp) * 2)
        elif i == ']':
            m_stack.pop()
            m_stack.pop()
            m_stack.append(int(temp) * 3)

    if len(m_stack) > 1 and is_int(m_stack[-1]) and is_int(m_stack[-2]):
        temp_sum = m_stack[-1] + m_stack[-2]
        m_stack.pop()
        m_stack.pop()
        m_stack.append(temp_sum)

    # print(m_stack)

print(m_stack[0])

