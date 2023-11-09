from collections import deque

N, M= map(int, input().split())
li_locate = list(map(int, input().split()))
deque_locate = deque(i+1 for i in range(N))

locate_count=0
for i in range(M):
    if li_locate[i]==deque_locate[0]:
            deque_locate.popleft()
    else:
        target_index=deque_locate.index(li_locate[i])
        if len(deque_locate)//2>=target_index: 
            deque_locate.rotate(-target_index)
            deque_locate.popleft()
            locate_count+=target_index
        else:
            deque_locate.rotate(len(deque_locate)-target_index)
            locate_count+=(len(deque_locate)-target_index)
            deque_locate.popleft()

print(locate_count)

### 구현 내용 설명 ###
# 1. line 9,11 에서
'''
line 9의 if문: 문제에서 1번 연산에 해당(삭제 하려는 값이 맨 앞에 있으면 삭제)
line 11의 else문: 문제에서 2,3번 연산에 해당(삭제 하려는 값이 맨 앞에 없으면 회전)
'''

# 2. line 13,17 에서
'''
1. deque_locate 길이의 중간값보다 삭제하려는 값의 위치가 더 앞에 있으면 오른쪽으로 회전하는게 더 적게 회전하고(if문),
   deque_locate 길이의 중간 위치보다 삭제하려는 값의 위치가 더 뒤에 있으면 왼쪽으로 회전하는게 더 적게 회전함(else문)
1-1. deque_locate의 길이가 짝수라면 len(deque_locate)//2=target_index가 if문이나 else문 중 어느곳에 적용돼도 같은 값이지만,
    deque_locate의 길이가 홀수라면 len(deque_locate)//2=target_index가 if문 조건에 적용되어야 더 적게 회전함 
'''

# 3. line 19,20 에서
'''
line 19와 20의 순서가 바뀌면 x => len(deque_locate) 값이 달라지기 때문에 계산 결과가 달라짐
            
'''