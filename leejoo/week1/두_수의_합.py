import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

#투 포인터를 사용하기 위해 필요한 변수 정의
arr.sort()
start, end = 0, n-1
tmp = 0
count = 0

while start < end:
    #start와 end 위치에 있는 값을 더한 것을 tmp에 대입
    tmp = arr[start] + arr[end]
    #tmp가 x와 값이 같을 때 count해주고 start,end를 각각 +1, -1 해줌
    if tmp == x:
        count += 1
        start += 1
        end -= 1
    
    #만약 tmp가 x보다 크다는 것은 큰 수를 더한거기 때문에 end를 -1해줌
    elif tmp > x:
        end -= 1
    #만약 tmp가 x보다 작은 것은 start 수가 작기 때문에 start에 +1를 해줌
    else:
        start += 1

print(count)