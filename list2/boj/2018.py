#수들의 합5
n=int(input())
num = list(range(n))
count=1
for i in range(1,n):
  for j in range(i,n):
    if sum(num[i:j]) == n:
      count+=1
      #print(num[i:j])
print(count)
#--시간초과--