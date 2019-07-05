import random

#  숫자 랜덤 생성
num = set()
while(True):
    num.add(random.randint(1,9))
    if(len(num)) == 3:
        break
Num = list(num)
print(Num)

print("숫자 야구 게임을 시작 합니다")
print('-'*30)
total = 0
while True:
    temp = []
    strike = 0
    ball = 0
    ans = input('숫자 3자리를 입력하세요 : ')
    if len(ans) >= 4:
        print('잘못입력했습니다. 4자리의 숫자를 입력했습니다')
    elif len(ans) < 3:
        print('잘못입력했습니다. 2자리의 숫자를 입력했습니다')
    else:
        temp.append(int(ans[0]))
        temp.append(int(ans[1]))
        temp.append(int(ans[2]))
        # temp = list(ans)
        # print(temp)
        if temp[0] in Num:
            if temp[0] == Num[0]:
                strike += 1
            else:
                ball += 1

        if temp[1] in Num:
            if temp[1] == Num[1]:
                strike += 1
            else:
                ball += 1

        if temp[2] in Num:
            if temp[2] == Num[2]:
                strike += 1
            else:
                ball += 1
        total += 1

        if strike == 3:
            print('축하합니다 {} 번만에 맞추셨습니다'.format(total))
            break

        print('스트라이크 : {}, 볼 : {}'.format(strike, ball))



