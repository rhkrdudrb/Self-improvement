#구간 합 구하기 1 백준 11659번 복습필요
n, m = map(int, input().split()) #숫자갯수,질의갯수
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
   temp = temp + i
   prefix_sum.append(temp)

for i in range(m):
  s,e = map(int, input().split()) #질의 범위 받기
  print(prefix_sum[e] - prefix_sum[s-1])
