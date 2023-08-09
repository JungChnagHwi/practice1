tc = int(input())
for tc in range(tc):
    n=int(input())

    def Pascal(n):
        dp = [list([0] * n) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
            for j in range(1,n):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                # 현재값 = 현재값 위 숫자 + 위 왼쪽 숫자
        for i in range(n):
            print()
            for j in range(i + 1):
                print(dp[i][j], end=' ')


    print(f'#{tc + 1}', end=' ')

    Pascal(n)
    print()






