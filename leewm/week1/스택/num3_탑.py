N = int(input())
send_top_li=list(map(int, input().split())) # 송신하는 탑 높이 입력받기

push=[] #송신하는 전체 탑 높이 저장
result=[] #수신할 탑 번호 저장
for i in range(len(send_top_li)):
    send_top=send_top_li[i] # 송신하는 탑 높이

    push_pop=push.append(send_top)
    push_pop=push.copy()

    recept_top=0
    while(len(push_pop))!=0:
        compare_num = push_pop.pop() #수신할 탑 번호 저장 할 변수 생성 
        if compare_num>send_top: # send_top을 수신하는 top의 번호 찾기
            recept_top=len(push_pop)+1
            break
    result.append(recept_top)

#각 탑별로 수신하는 탑 번호 반칸 두고 출력
for i in result:
    print(i, end=' ')


