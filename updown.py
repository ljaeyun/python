import random

n = random.randint(1, 100)
# print(n)
while True:
    ans = input("숫자를 입력하세요 (1~100)(종료키 Q)")

    if ans.upper() == 'Q':
        break

    ians = int(ans)

    if ians == n:
        print("정답")
        break
    elif ians > n:
        print('UP')
    else:
        print("DOWN")

#  exe 생성
#  pyinstaller 파일이름.py
#  exe 단일 파일 생성 -> pyinstaller --onefile 파일이름.py