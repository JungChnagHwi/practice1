tc = int(input())
V, E = map(int, input().split())
graph=[]
stack=[]
for i in range(E):
  start = list(map(int, input().split()))
  graph.append(start)

end = list(map(int, input().split()))


f