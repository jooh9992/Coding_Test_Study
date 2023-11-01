cal_result=1
for i in range(3): # 숫자 입력받아서 곱하기
    num=int(input())
    cal_result*=num 

# 계산 결과 리스트로 변환 (ex)17037300 -> [1,7,0,3,7,3,0,0] ) 
li = list(map(int, str(cal_result)))

# 각 숫자 count
for i in range(0,10): 
    print(li.count(i), sep='\n')