import sys
input = sys.stdin.readline

N = input().rstrip() #방번호 입력받기
count = [0] * 10 #숫자초를 위한 배열 생성

#6, 9는 뒤집어서 사용할 수 있기 때문에 9도 다 6배열에 넣어줌
for i in str(N):
    if (i == "9"):
        count[6] += 1
    else:
        count[int(i)] += 1

#6과9를 합친 숫자를 2로 나누어줌
count[6] = (count[6]+1)//2

print(max(count))
    