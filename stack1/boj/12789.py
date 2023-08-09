#도키도키 간식드리미
n = int(input())
numbers = list(map(int, input().split()))
stack = []
count = 1

while numbers:
    if numbers[0] == count:
        numbers.pop(0)
        count += 1
    else:
        stack.append(numbers.pop(0))

    while stack:
        if stack[-1] == count:
            stack.pop()
            count += 1
        else:
            break

if not stack:
    print('Nice')
else:
    print('Sad')
