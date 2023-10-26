import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

num = list(str(A*B*C))
answer = [0,0,0,0,0,0,0,0,0,0]

for i in num:
    answer[int(i)] += 1

for j in answer:
    print(j)