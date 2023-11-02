import random

n=int(input())
#array=random.sample(range(1,1000000),n)
array = list(map(int, input().split()))
x=int(input())

count=0 # 쌍의 개수 (출력값) 저장할 변수 생성
for i in range(0, n-1):
    target = array[i]
    subarray = array[i+1:n] # target값 빼고 sublist 생성
    target2 = x-target # target값 과의 짝 찾기

    if target2 in subarray: # sublist에서 target2값 있으면 count++
        count+=1

print(count)