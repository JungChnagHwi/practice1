tc = int(input())

for tc in range(tc):
    str = input()
    stack = []


    for i in str:
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')' or i =='}':
            if len(stack) == 0:
                stack.append(i)
                break
            elif (stack[-1]=='(' and i == ')') or (stack[-1] == '{' and i == '}'):
                stack.pop()

    if len(stack) != 0:
        print(f'#{tc+1} 0')
    else:
        print(f'#{tc+1} 1')