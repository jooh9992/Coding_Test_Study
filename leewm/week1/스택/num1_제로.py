K = int(input())

li=[]
for i in range(K):
    num=int(input())
    if num==0: # 0 입력되면 입력된 수 제거
        li.pop()
    else: # 0 아니면 수 입력
        li.append(num)

if len(li)==0: # 입력된 수 없으면 0 출력
    print(0)
else: # 입력된 수 있으면 합 출력
    print(sum(li))