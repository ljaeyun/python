import keyword
import sys
# 문자열 * 사용시 문자열 반복
print("*" * 50)

# 문자열 파싱 , 0부터 4번째 까지 -> 0 ,1 ,2 3
a = "life is "
print(a[0:4])

b = "20010331Rainy"
date = b[:8]
weather = b[8: len(b)]
print(date)
print(weather)

addr1 = "서울시"
addr2 = "서초구"
addr3 = "역삼동"
addr4 = "멀티로 123"

print("주소는 {0} {1} {2} {3}".format(addr1, addr2, addr3, addr4))

print("주소는 {2} {1} {2} {0}".format(addr1, addr2, addr3, addr4))

print("주소는 %10s %-10s %s" % (addr1, addr2, addr3))
# 소수점 뒤의 개수
print(' %.2f' % (1235.35849687))
print(' %.f' % (1235.35849687))

print(sys.maxsize)
print(sys.maxsize + 1)
# 자료형에 대한 크기의 제한 x
num = 1414654846464568786458746584653
print(num, type(num))
# float 15자리 까지 표현 가능
num2 = 2 * 5 * 3.14
print(num2, type(num2))
# 문자열 입출력 방식 출력
print(sys.stdout.encoding)
print(sys.stdin.encoding)
# 멀티 라인 출력 """ """ , ''' '''
print(""" 123
2334
3456""")

# 형변환
print(int(num2))

# print("키워드 목록")
# print(keyword.kwlist)
# print("키워드 개수 :", len(keyword.kwlist))

print('hello', end=', ')
print('hello')
print('hello')
txt = "hello python"

print("1", "2", "3", sep='\n')
print(txt, "test")


a = b = 1

print(id(a), id(b))

b = 2

print( id(a), id(b))
print(a ==b)

a=3
b = 5
print("a :", a, "b : ", b)
# 변수 값 바꾸기
a, b = b, a
print("a :", a, "b : ", b)
# 변수 삭제
del b
del a

# a = input("input : ")
# print(a)

# find 문자 위치 반환
temp2 = "python is best choice"
print(temp2.find('b'))
print(temp2.find('k'))
del temp2
# index 문자 위치 반환  find와 다르게 찾는 문자가 없을 경우 에러
temp2 = "life is too short"
# print(a.index('t'))
# print(a.index('k'))
del temp2

# 문자열 조작
temp2 = ","
print(temp2.join('abcd'))
del temp2

# 소문자 , 대문자 변환
temp2 = "HI"
print(temp2.lower())
print(temp2.upper())
del temp2

# 양쪽 공백 지우기 strip, lstrip, rstrip, 중간 공백 제거 x
temp2 = " hi "
print(temp2.strip())
del temp2

# 문자열 바꾸기 replace
temp2 = "Life is too short"
print(temp2.replace("Life", "your leg"))
del temp2

# 문자열 자료형의 리스트화
temp2 = "Life is too short"
print(temp2.split())
temp2 = "a:b:c:d"
print(temp2.split(':'))

print('-' * 30)

stName3 = stName4 = '기생충'
print(stName3 == stName4)
print(stName3 is stName4)
a = b = 10
print(a is b)

c = 10
print(a is c)
# is 와 ==는 서로 다름 레퍼런스 타입의 증명
beer = input()
if (beer == 'cass'):
    print('case is best')

# 7과 70000 과 결과값이 다름 작은값에 대해서 미리 할당
num = int(input())
if(num is 70000):
    print('my favorite num is 7')