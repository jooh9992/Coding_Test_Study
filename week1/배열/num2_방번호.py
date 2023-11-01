from collections import Counter

num=list(input()) # 입력한 수 리스트로 생성
li=Counter(num) # 입력한 수의 숫자 세기

# 66 또는 69 또는 99를 한쌍으로 엮어서 숫자 세기
if 6 or 9 in li:
    if (li['6']+li['9'])%2==1:
        li['6'], li['9'] = (li['6']+li['9'])//2+1, (li['6']+li['9'])//2+1
        
    elif (li['6']+li['9'])%2==0:
        li['6'], li['9'] = (li['6']+li['9'])//2, (li['6']+li['9'])//2

#가장 많이 나온 수가 필요한 세트의 수        
print(Counter(li).most_common(1)[0][1])
