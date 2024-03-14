# shift + F10 : 설정된 파일 실행
# ctrl + shift + F10 : 현재 커서 위치의 파일 실행
# ctrl + / : 주석/해제
# ctrl + d : 커서행 복사
# shift + del : 커서행 삭제
# alt + enter : 모듈 import
import copy
import sys
from collections import deque

li = [1,2,3,4,5,6]
for x in li:
   print(x)

li = [1,2,3]
for x in li:
    print(x)

def func(l):
    print(id(l))
    l = [3,4,5]
    print(id(l))

func(li)
print(id(li))


#################################
sys.stdin = open('input.txt')

## 문자열 1개 입력받아서 처리시
s = input().strip() # 양쪽 white space(공백, 엔터) 제거

## 문자열 여러개 한줄에 공백 기준으로 입력
s = input().split() # 공백 기준 리스트로 분류, strip() 생략 가능

## 정수 한개 입력
s = int(input())

## 정수 두개 입력
s = input().split()
s = list(map(int, s))
print(s)

s = list(map(int, input().split()))
print(s)

# map(func, s)    # s의 각 원소 x에 대해 func(x) 값으로 변환
#                 # iterator 반환


## 3개의 줄마다 한개 문자열 입력
li = []
for i in range(3):
   li.append(input().strip())
print(li)

li = [input().strip() for _ in range(3)]
print(li)

## 3개의 줄마다 한개 정수 입력
li = [int(input()) for _ in range(3)]
print(li)

## 3개의 줄마다 문자열 5개 입력 : 3*5 2d list
li = [input().split() for _ in range(3)]
print(li)

## 3개의 줄마다 정수 5개 입력
li = [list(map(int,input().split())) for _ in range(3)]
print(li)

## print
li = [1,2,3,4,5]
print(li)
print(*li)   # 1 2 3 4 5
print(*li, sep=' ', end='\n')
print(*li, sep='', end='')
print(*li, sep='\n')

## f-string : 'li = [1,2,3,4,5]'
print(f'li = {li}')
print(f'li[3:] = {li[3:]}')
print('li = {}'.format(li))
print('li = {}{}'.format(li,li[3:]))

## 1차원 배열 생성
li = [0] * 10
li[0] = 10
print(li)

## 2차원 배열 생성
# X
li = [[0]*3] * 3
li[0][0]=10
print(li)

# O
li = [[0]*3 for _ in range(3)]
li[0][0]=10
print(li)

## 3차원 배열 생성
li = [[[0]*4 for _ in range(3)] for _ in range(2)]
print(li)

## 1d. copy
l1 = [1,2,3]

# reference copy
l2 = l1
# shallow copy
l3 = l1.copy()
l3 = l1[:]

## 2d. copy
l1 = [[0,0],[1,1],[2,2]]

# reference copy
l2 = l1

# shallow copy
l3 = l1.copy()
l3 = l1[:]

# deep copy
l4 = copy.deepcopy(l1)

# if , while false 조건
# None, False
# 0, 0.0, ..
# empty collection : (), [], {}, set(), ''

if not ():
    print(1)

# x,y = 0,1
# if x or y   # x ture 이면 y 확인 안함
# if x and y  # x false 이면 y 확인 안함

# x if C else y   # C 참이면 x, 거짓이면 y 반환
print(1 if () else 0)