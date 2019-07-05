print('문제 1')

kor = 80
eng = 75
math = 55
total = kor + eng + math
print('평균 점수 : ', total / 3)

print('-' * 30)
print('문제 2')
num = 13
if(num % 2 == 1):
    print('홀수 입니다.')
else:
    print('짝수입니다.')



print('-' * 30)
print('문제 3')

pin = "881120-1068234"
print('yyyymmdd =', pin[0:6])
print('num = ', pin[7: len(pin)])

print('-' * 30)
print('문제 4')
print(pin[7])

print('-' * 30)
print('문제 5')
a = "a:b:c:d"
b = a.replace(':', '#')
print(b)

print('-' * 30)
print('문제 6')
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

print('-' * 30)
print('문제 7')
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

print('-' * 30)
print('문제 8')
a = (1, 2, 3)
a += (4,)
print(a)

print('-' * 30)
print('문제 9')
a = dict()
a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python'
a[250] = 'python'
print(a)

print('-' * 30)
print('문제 10')
a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a)
print(result)

print('-' * 30)
print('문제 11')
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

print('-' * 30)
print('문제 12')
import copy
# a = b = [1, 2, 3]
a = [1, 2, 3]
b = copy.deepcopy(a)
# b = copy.copy(a)
a[1] = 4
print(a)
print(b)
