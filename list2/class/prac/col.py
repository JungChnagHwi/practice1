import sys
sys.stdin = open('input.txt')

ts = int(input())
for num in range(ts):
  red_box=[]
  blue_box=[]
  n=int(input())

  for _ in range(n):
    arr = list(map(int, input().split()))

    if arr[-1] == 1:
      for i in range(arr[0], arr[2]+1):
        for j in range(arr[1], arr[3]+1):
          red_box.append((i,j))
    else:
      for i in range(arr[0], arr[2]+1):
        for j in range(arr[1], arr[3]+1):
          blue_box.append((i,j))



    new_set=set(red_box) & set(blue_box)

    print(f'#{num+1} {len(new_set)}')