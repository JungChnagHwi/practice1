#괄호 짝찾기

t = int(input())

for tc in range(t):
    str = input()
    stack = []

    for i in str:
        if i == '(' or i == '{':
            stack.append(i) # 문자열 돌며 괄호만 stack에 추가

        elif i == ')' or i =='}':
            if len(stack) == 0:
                stack.append(i)
                break  # 빈 stack에 ), } 이 들어가면 못 없애므로 무조건 '0' 출력
            elif (stack[-1] == '(' and i == ')') or (stack[-1] == '{' and i == '}'):
                stack.pop() # stack 마지막에 들어간 괄호와 짝이 맞으면 삭제
            else:
                stack.append(i) # 짝이 안 맞으면 추가 Ex) {( })
                break

    if len(stack) != 0:
        print(f'#{tc+1} 0')
    else:  # 빈 stack이면 1 출력
        print(f'#{tc+1} 1')