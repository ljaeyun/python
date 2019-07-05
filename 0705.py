#  비교연산자
'''
a = 1
b = 1
print(a == b)

#  if
if True:
    print('조건 제어문')

a = 1
b = 10

if a>b:
    print('a는 b보다 크다')
# if a<b:
else:
    print('a는 b보다 작다')

money = 10
if money:
    print('택시를 타고')
    print('택시를 타고')
print('가자')

print('-'*30)

data = int(input('정수를 입력하세요 : '))

if data > 0:
    print('양수입니다')
elif data == 0:
    print('0')
# if data < 0:
else:
    print('음수입니다.')

print('-'*30)

age = int(input("나이를 입력하세요 : "))

if age >= 19:
    print('성인입니다.')
elif 17 <= age:
    print('고등학생입니다.')
elif 14 <= age:
    print('중학생입니다.')
elif 8 <= age:
    print('초등학생입니다.')

print('-'*30)

tall = int(input('키를 입력하세요 : '))
weight = int(input('체중을 입력하세요 : '))

bmi = weight / ((tall / 100)**2)
print(bmi)
if bmi > 35:
    print('고도비만')
elif bmi >= 30:
    print('중등도 비만')
elif bmi >= 25:
    print('경도 비만')
elif bmi >= 23:
    print('과체중')
elif bmi >= 18.5:
    print('정상')
else:
    print('저체중')

print('-'*30)

#  in, not in
#  문자열에서 사용
print('ana' in 'banana')
print('a' in 'Python')

print('ana' not in 'banana')
print('a' not in 'Python')
#  리스트에서 사용가능
userName = ['a', 'b', 'c', 'd']
print('a' in userName)

#  set에서 사용가능
userName = {'a', 'b', 'c', 'd'}
print('a' in userName)

#  딕셔너리에 있는가 - 키 , 값
userName = {'name': 'kim', 'city': 'seoul', 'grade': 'b'}
print('name' in userName)  # 키에서 찾기
print('seoul'in userName.values())  # 값에서 찾기
print('paris'in userName.values())



#  시간 모듈 import
import datetime

now = datetime.datetime.now()
print('now = ', now)

print('년도 = ', now.year)
print('월 = ', now.month)
print('일 = ', now.day)
print('시 =', now.hour)
print('분 =', now.minute)
print('초 =', now.second)

print('오늘은 {} 년 {}월 {}일 입니다'.format(now.year, now.month, now.day))
print('작성일자 {}'.format(now.strftime('%Y-%m-%d %H:%M:%S')))  # 시간 포매팅 함수

#  시간 문자열 저장
newdt = datetime.datetime.strptime('2019-07-05', '%Y-%m-%d')  # 2019-07-05 사용자입력 대체 가능
print(newdt, type(newdt))


#  while 반복문
i = 0
sum = 0
while i < 100:
    i += 1
    if i % 5 == 0:
        sum += i
print(sum)



#  for 문
#  리스트
test_list = ['a','b','c','d']
for  i in test_list:
    print(i)
#  튜플
aa = [('a', 'b'), ('c', 'd'), ('e', 'f')]
for (i, j) in aa:
    print(i, j)


for j in range(1, 10):
    for i in range(2, 10):
        print('{} * {} = {}'.format(i, j, i*j), end="\t")

    print(' ')

'''
#  별찍기
i = 0
while i < 6:
    print('*'*i)
    i += 1

#  1부터 50까지의 합
sum = 0
n = 1
while n <= 50:
    sum += n
    n += 1
print(sum)

#  리스트에서 최대값 출력
myList = [50, 44, 68, 98, 42, 10]
result = myList[0]
for i in myList:
    if result < i:
        result = i
print('최대값 :', result)
