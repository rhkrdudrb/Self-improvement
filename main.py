n,m = map(int ,input().split())
numbers = list(map (int,input().split()))
psum = [0]
temp = 0 
for i in numbers :
  temp = temp + i
  psum.append(temp)
for i in range(m) :
  s,l = map(int,input().split())
  print(psum[l] - psum[s - 1])
  