# 리스트
a = []  # 초기화
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'life', 'too']
e = [1, 2, ['life', 'too']]  # 리스트안에 리스트 가능

# 리스트 더하기
print(a + b + c)
# 리스트 반복
print(b * 3)
# 리스트 값 수정
b[1] = 99
print(b)
b[1:2] = ['a', 'b', 'c']
print(b)
# 요소 삭제
del b[1]
print(b)

# 값 추가
b.append(2)
print(b)
print(b.pop())  # 마지막 값 리턴, del 은 리턴값 x
print(b)
print(b.index(1))
# print(b.index(76))  # 에러 발생
b.clear()
print(b)

# 값 x 인덱스 리버스
c.reverse()
print(c)

# 값 끼워넣기
c.insert(1, 'long')
print(c)

# 문자열 변환
result = " ".join(c)
print(result)

print('-' * 30)

fruits = ['사과', '수박', '망고', '바나나', '망고', '바나나']
print('사과' in fruits)
print('fruits 목록 : {}'.format(fruits))
# 리스트 인덱싱
# 0부터 시작
# 음수일때는 역순 -1 : 마지막값 인덱싱
print('fruits[0] = {}'.format((fruits[0])))
print('fruits 리스트의 전체 길이 = {}'.format(len(fruits)))

print(fruits[:])
print(fruits[0:2])
print(fruits[2:])

#  문자열과 숫자열은 immutable 이므로 새로운 변수를 할당하고 참조
x = 1
y = x
print(id(x), id(y), x, y)  # 참조값 , 값 동일
y += 3
print(id(x), id(y), x, y)  # 새로 할당 y 가 참조

x = 'abcd'
y = x
print(id(x), id(y), x, y)
y += 'e'
print(id(x), id(y), x, y)

#  리스트는 mutable 이므로 같은 변수를 계속 가리키고 있다
x = [1, 2]
y = x
print(id(x), id(y), x, y)
y.append(3)
print(id(x), id(y), x, y)

print('-' * 30)
#  append 동적 추가
drama = []
data = '봄날'
drama.append(data)
print(drama)

#  insert 요소 추가
numbers = [100, 200, 300, 400]
print('number list = ', numbers)
numbers.insert(2, 10)
print('number list = ', numbers)

#  remove 요소 삭제 1 중복된 값에서 앞 하나만 삭제
numbers.remove(200)  # 값으로 하나만 삭제
print('number list = ', numbers)

#  pop 요소 삭제 2 뒤에서 하나의 값만 삭제, 리턴
numbers.pop()
print('number list = ', numbers)
numbers.pop(0)  # 위치값으로 삭제  -> 리스트.pop(위치값)
print('number list = ', numbers)

#  del 리스트 삭제 3 -> del 리스트이름[인덱스]
foods = ['라면', '돈까스', '볶음밥']
print("foods list = ", foods)
del foods[0]
print("foods list = ", foods)
# del foods[0:1]  # del만 슬라이싱 가능
print(foods.pop())
print("foods list = ", foods)
print(foods.pop())

foods.clear()  # 요소만 삭제
print("foods = ", foods)

#  리스트 확장 -> extend([리스트])
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 9]
a.extend(b)
print('a = ', a)
print('b = ', b)

#  리스트 구조 => 문자열
foods = ['피자', '햄버거', '밥', '치킨']
sep = ','

numStr = sep.join(foods)
print(numStr)
print(type(numStr))

#  문자열 => 리스트
myStr = '강/김/홍/박/선우/우/이/식'
print(myStr.split('/'))

print('-' * 50)
print('-' * 50)

#  튜플
#  튜플 수정, 삭제 불가능
#  순서, 중복 가능
#  튜플 요소 추가 => 새로운 튜플이 생성
t = (1, 2)
t += (3,)  # 새로운 참조값 생성 -> 새로운 튜플
print(t)

t1 = ('도', '레', '미', '라', '솔')
print(t1, type(t1))
print(t1)
print(t1[0])
print(t1[-1])
#  슬라이싱
print(t1[2:3])

t2 = 1, 2, 3, 4, 5  # 괄호 생략 가능
print(t2, type(t2))

myTuple = 100, '강아지', ('지렁이')
print('myTuple = ', myTuple)
print('myTuple[0] = ', myTuple[0])
#  튜플이름 += (값1, 값2, ...)
myTuple += (50, 100)
print('myTuple = ', myTuple)
myTuple += '끝',
print('myTuple = ', myTuple)

#  튜플 함수 적용
t1 = (100, 40, 20, 20, 20)
print('20의 반복 횟수 : ', t1.count(20))
print('40의 인덱스 : ', t1.index(40))

#  t1.sort() 불가능  -> 원본 수정 -> 튜플 수정 불가능
#  튜플의 길이 = 요소의 총 개수
print(len(t1))

#  튜플 요소의 위치값 반환
#  튜플 이름.index(위치값)
print(t1.index(20))
print('-' * 20)
#  문자열 -> 튜플
#  tuple(문자열변수 or 문자열)
myStr = 'Python'
print(myStr, type(myStr))
myTuple = tuple(myStr)
print(myTuple, type(myTuple))
print('-' * 20)
#   리스트 -> 튜플
myList = ['수학', '과학', '영어']
print(myList, type(myList))
myTuple = tuple(myList)
print(myTuple, type(myTuple))
print('-' * 20)
#  튜플 -> 리스트
myTuple = (100, 30, 40, 40, 40)
print(myTuple, type(myTuple))
myList = list(myTuple)
print(myList, type(myList))
print('-' * 20)
#  튜플 -> 문자열 1
#  str(튜플이름)
myTuple = ('도', '레', '미', '파', '솔')
print(myTuple, type(myTuple))
myStr = str(myTuple)
print(myStr, type(myStr))  # 하나의 문자열
print(myStr[0])
#  튜플 -> 문자열 2
#  '구분자'.join(튜플이름)
myTuple = ('도', '레', '미', '파', '솔')
myStr = ','.join(myTuple)   # list 를 통해서도 가능
print(myStr, type(myTuple))
myStr2 = '/'.join(myTuple)
print(myStr2, type(myStr2))

print('-' * 50)
print('-' * 50)

#  딕셔너리
#  키는 중복 x , 값은 중복 o
#  키값이 같을 경우 마지막에 정의한 것만 출력
dict1 = {'a': 'apple', 'b': 'banana', 'c': 'cat'}

#  딕셔너리 초기화
dict0 = {}
print("dict0 = ", dict0, type(dict0))

#  딕셔너리 호출
print("dict1['a']=  ", dict1['a'])

#  딕셔너리 요소 추가
dict1['d'] = 'drive'
print('dict1 = ', dict1)

#  딕셔너리 요소 삭제
del dict1['a']
print('dict1 = ', dict1)

grade = {'pey': 10, 'juliet': 99}
print(grade)
print(grade['pey'])
print(grade['juliet'])

#  딕셔너리 키만 출력
print(grade.keys())

#  딕셔너리 값만 출력
print(grade.values())

#  딕셔너리 키와 값이 하나의 쌍으로 출력(튜플의 리스트)
print(grade.items())

print(grade.get('pey2', 123))

print('pey'in grade)  # 키 여부 확인
print('pey2'in grade)

aa = dict()  # 아무것도 없는 딕셔너리 생성
print(aa)
aa['one'] = "첫번째"
print(aa)

print(grade.pop('pey'))
print(grade)


#  키값만 모아서 문자열 저장
myStr = " ".join(dict1)
print(myStr)

#  딕셔너리 얕은 복사
import  copy  # 복사 모듈
a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 14, 'suzy': 30}
# b = a.copy()
b = copy.deepcopy(a)  # 깊은 복사
b['alice'].append(5)  # 키값의 리스트에 append 한다
print("a=", a)
print("b=", b)  # a, b 동일한 값
b['test'] = 13

#  딕셔너리 -> 리스트
dict_list = list(a)
print('dict_list = ', dict_list)  # 키값만 리스트와

#  딕셔너리 -> 튜플
tuple_list = tuple(a)
print('tuple_list = ', tuple_list)


print('-' * 30)
# 집합 자료형 set

# 난수 생성
import  random
lotto = []
lotto.append(random.randint(1,6))
lotto.append(random.randint(1,6))
lotto.append(random.randint(1,6))
lotto.append(random.randint(1,6))
lotto.append(random.randint(1,6))
lotto.append(random.randint(1,6))
print(len(lotto), lotto)

lotto = set()
lotto.add(random.randint(1,6))
lotto.add(random.randint(1,6))
lotto.add(random.randint(1,6))
lotto.add(random.randint(1,6))
lotto.add(random.randint(1,6))
lotto.add(random.randint(1,6))
print(len(lotto), lotto)

lotto = set()
while(True):
    lotto.add(random.randint(1,19))
    if(len(lotto)) == 6:
        break

print(len(lotto), lotto)

#  난수 생성 함수
k = range(1, 49)
lotto_num = random.sample(k, 6)
print(lotto_num)

i = random.randint(1,100)
# 1부터 100사이의 정수

f = random.random()
# 0 부터 1사이의 임의의 float

f = random.uniform(1.0, 36.5)
# 1부터 36.5 사이의 임의의 float

i = random.randrange(1, 101, 2)
# 1부터 100사이의 짝수

i = random.randrange(10)
# 1부터 9까지 임의의 정수
