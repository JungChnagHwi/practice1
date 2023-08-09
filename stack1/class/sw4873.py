tc = int(input())
for tc in range(tc):
    str = input()
    stack = []

    for i in str:
        stack.append(i)
        if len(stack) == 1:
            continue
        elif stack[-2] == stack[-1]:
            stack.pop()
            stack.pop()

    print(f'#{tc + 1} {len(stack)}')