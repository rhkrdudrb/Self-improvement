#평균 구하기 38p 백준1546번
n = input()
avg =list(map(int, input().split()))
myavg = max(avg)
sum = sum(avg)  
print(sum*100/myavg/int(n))