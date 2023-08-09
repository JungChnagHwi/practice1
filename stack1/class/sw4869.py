# 4869
def Factorial(number):
    if number == 0:
        return 1
    else:
        return Factorial(number - 1) * number


ts = int(input())
for ts in range(ts):
    length = int(input())  # 길이
    square = length // 20  # 정사각형 최대 개수
    remainder = (length % 20) / 10  # 직사각형의 개수

    count = 0
    while remainder <= length / 10:
        ans = Factorial(square + remainder) / (Factorial(square) * Factorial(remainder))  # 세로 직사강형 + 정사각형 이 올 수 있는 경우의 수
        count += ans * (2 ** square)  # 세로 직사각형 + 각 정사각형을 가로 직사각형 2개로 바꾸거나 아니거나 합친 경우의 수
        square -= 1
        remainder += 2  # 정사각형이 없어질 때까지 반복

    print(f'#{ts + 1} {int(count)}')