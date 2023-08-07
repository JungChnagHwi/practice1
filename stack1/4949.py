while True:

    str = input()
    stack = []

    if str == ".":
        break

    for i in str:
        if i == '(':
            stack.append('(')
        elif i == '[':
            stack.append('[')


        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            elif stack.append(')'):
                break


        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            elif stack.append(']'):
                break

    if len(stack) != 0:
        print('no')
    else:
        print('yes')




