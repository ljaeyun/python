# 1. a, b, c, d, e를 저장하는 튜플을 만들고 첫 번째 튜플값과 마지막 번째 튜플값을 출력하세요.
print('문제 1')
tup = ('a', 'b', 'c', 'd', 'e')

print('tup[0]= {0}, tup[1] = {1}'.format(tup[0], tup[4]))
print('tup[0]= {0}, tup[1] = {1}'.format(tup[0], tup[-1]))
# 2. 다음 코드를 작성해서 실행해보고 에러가 나는 이유를 설명하세요.
# tupledata = ('dave', 'fun-coding', 'endless')
# tupledata[0] = 'david'

# 읽기전용 수정 시도

# 3. 다음 튜플 데이터를 리스트 데이터로 변환한 후에 'fun-coding4' 데이터를 마지막에 추가하고,
#    다시 튜플 데이터로 변환하세요.
print('-' * 30)
print('문제 3')
tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3')
listdata = list(tupledata)
print('listdata = ', listdata, type(listdata))
listdata.append('fun-coding4')
tupledata = tuple(listdata)
print('tupledata = ', tupledata, type(tupledata))

# 4. 비어 있는 튜플, 리스트, 딕셔너리 변수를 하나씩 각각 만드세요.
print('-' * 30)
print('문제 4')
tup1 = ()
print(tup1, type(tup1))
list1 = []
print(list1, type(list1))
dic1 = {}
print(dic1, type(dic1))

# 5. 다음 actor_info 딕셔너리 변수를 만들고, 홈페이지, 배우 이름, 최근 출연 영화 갯수를 다음과 같이 출력하세요
print('-' * 30)
print('문제 5')
actor_info = {'actor_details': {'생년월일': '1971-03-01',
                   '성별': '남',
                   '직업': '배우',
                   '홈페이지': 'https://www.instagram.com/madongseok'},
 'actor_name': '마동석',
 'actor_rate': 59361,
 'date': '2017-10',
 'movie_list': ['범죄도시', '부라더', '부산행']}


#배우 이름: 마동석
#홈페이지: https://www.instagram.com/madongseok
#출연 영화 갯수: 3

print('배우 이름 : ', actor_info['actor_name'])
print('홈페이지 : ', actor_info['actor_details']['홈페이지'])
# actor_info.get('acotr_details').get('홈페이지')
print('출연 영화 개수 : ', len(actor_info['movie_list']))

# 6. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
print('-' * 30)
print('문제 6')
list2 = ['Banana', 'Apple', 'Orange']
list2.remove('Apple')
print('list2 = ', list2)

# 7. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
print('-' * 30)
print('문제 7')
tup2 = (1, 2, 3, 4)
list3 = list(tup2)
print('list3 = ', list3, type(list3))

# 8. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
print('-' * 30)
print('문제 8')
dic2 = {'성인': 100000, '청소년': 70000, '아동': 30000}
print('dic2 =', dic2, type(dic2))

dic = {}
dic['성인'] = 10000
dic['청소년'] = 70000
dic['아동'] = 30000
print(dic)

# 9. 8번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
print('-' * 30)
print('문제 9')
dic2['소아'] = 0
print('dic2 =', dic2, type(dic2))

# 10. 8번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
print('-' * 30)
print('문제 10')
print(dic2.keys())
print(list(dic2.keys()))
# 11. 8번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print('-' * 30)
print('문제 11')
print(dic2.values())
print(list(dic2.values()))

print(list(dic2.items()))
