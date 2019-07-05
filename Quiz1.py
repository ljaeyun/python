# 1. 화면에 "Hello World!"를 출력하세요.
print('Hello World!')


# 2. 화면에 "I don't like C language"를 출력하세요.
print('I don\'t like C language')


# 3. print 함수를 사용하여 3.1415의 값을 출력하세요.
# 단, 소수점 아래는 첫 번째 자리까지만 표시되도록 하세요.
print('%.1f' % 3.1415)

# 4. 문자열 '720'를 정수형으로 변환하세요. 정수 100을 문자열 '100'으로 변환하세요.
print(int('720'), type(int('720')))
print(str(100), type(str(100)))


# 5. 2와 4 숫자를 변수에 넣고, 두 변수를 더한 값, 곱한 값, 나눈 값을 출력하세요.
num1 = 2
num2 = 4

print('%d' % (int)(num1 + num2))
print('%d' % (int)(num1 * num2))
print('%.2f' % (float)(num1 / num2))

# 6. 사용자로부터 두 개의 숫자를 입력받은 후 두 개의 숫자를 더한 값, 곱한 값을 각각 출력하는 프로그램을 작성하세요
num1 = int(input("숫자 1 입력 :"))
num2 = int(input("숫자 2 입력 :"))

print('%d' % int(num1 + num2))
print('%d' % int(num1 * num2))

# 7. 'niceman', 'google.com' 문자열을 연속해서 출력할때 구분자를 @으로 변경하여 출력하세요.
str1 = 'niceman'
str2 = 'google.com'

# print("@".join(str1))
# print("@".join(str2))

print('niceman', 'google.com', sep='@')

#8. str = 'Niceboy' 이 변수를 이용해서 아래와 같은 결과가 나오도록 슬라이싱하여 출력하세요.
str = 'Niceboy'

print(str[0:3])
print(str[:])
print(str[0:len(str)-1])
print(str[0:len(str)])
print(str[1:5:2])
print(str[4:6])
print(str[-3:6])
print(str[1:5])
# print(str[len(str): 0: -1])
print(str[::-1])
print(str[0:len(str): 2])
'''
Nic
Niceboy
Nicebo
Niceboy
ie
bo
iceb
yobeciN
Ncby
'''

