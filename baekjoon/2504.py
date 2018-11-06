s = input()
m_stack = []

for i in s:
    if len(s) == 0:
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
            temp_num = temp
            m_stack.pop()
            m_stack.pop()
            
    print(m_stack)
