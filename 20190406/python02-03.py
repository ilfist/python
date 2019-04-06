# 리스트 자료형
# 파이썬의 리스트는 다른 언어의 '배열'과 동일한 기능을 가지고 있다
# 여러개의 데이터를 하나의 이름으로 묶어서 사용하는 자료형
# 각각의 데이터를 구별하기 위한 식별자로 인덱스를 사용
# index는 숫자 0부터 사용
# index 선언 방법 - 대괄호 사용해 구분해고, 리스트 내 데이트는 쉼표 사용 구분
# 리스트명 = [값1, 값2, 값3, ...]
# 리스트명 = [index] = 값
# print(리스트명[index])
# 리스트 요소로 거의 모든 자료형 사용 가능
# 리스트의 요소로 리스트 사용 가능

lista = [1, 2, 3]
print(lista)
print(lista[1])
lista[1]=100
print (lista)
print(lista[1])

listb=["Life", "is", "too", "short"]
print(listb)
print(listb[0])
print(listb[1])
print(listb[2])
print(listb[3])

value1 = "life"
value2 = "is"
value3 ="too"
value4 ="shrot"
print(value1, value2, value3, value4)

print(listb[0] + listb[1] + listb[2] + listb[3])
print(listb[0] + listb[1] + listb[2] + listb[3])

a=[] #빈리스트
b=[1, 2, 3] #일반적인 형태 숫자를 입력한 리스트
c=["Life", "is", "too", "short"] #문자형 리스트
d=[1, 2, "too", "short"] #숫자 문자열 혼합 리스트
e=[1, 2, ["too", "shrot"],4, 5] #리스트의 요소로 리스트를 가진 리스트
print(e)
print(e[1])
print(e[2])
print(e[3])

# 문제1. a=["Life ", "is ", "too ", "short"] 리스트를 이용해서 Life is too short 출력
a=["Life", "is", "too", "short"]
print(a[0]+" "+a[1]+" "+a[2]+" "+a[3])
# 문제2. 문제1의 각 인덱스에 값을 변경해서 출력
a[0]="You"
a[1]="need"
a[2]="Python"
a[3]="...?"
print(a[0]+" "+a[1]+" "+a[2]+" "+a[3])

# 리스트의 연산자 +, *
# + : 2개 이상의 리스트를 하나의 리스트로 통합
a=[1, 2, 3]
b=[4, 5, 6]
print(a+b)
c=a+b
print(c)

# * : 리스트를 지정한 횟수로 반복 출력(하나의 리스트로)
print(a*3)
print(a*2, b*2, c)

# 리스트의 수정
a[2]=100 #수정
print(a[2])

# 리스트의 지정한 요소를 삭제
# del 리스트명[index]
a=[1, 2, 3, 4, 5]
print("원본리스트 a : {0}".format(a))
del a[2]
print("del 사용 후 리스트 a: {0}".format(a))

# len : 리스트의 길이 확인
# len(리스트명)
a=[1, 2, 3, 4, 5]
del a[2]
del a[0]
print("원본 리스트 a : {0}\ndel 사용 후 리스트의 길이 : {1}".format(a, len(a)))

# append : 리스트에 요수 추가하기(가장 마지막 자리)
# 리스트명.append(요소)

a.append(60)
a.append(70)
print("append 사용 후 리스트 a : {0}\nappend 사용 후 리스트의 길이 : {1}".format(a, len(a)))

# sort: 리스트의 요소를 정렬(오름차순)
# 리스트명.sort()
a=[38, 2, 10, 27, 37, 43]
print("원본리스트 a :{0}".format(a))
a.sort()
print("sort 후 리스트 a : {0}".format(a))
b=["M", "S", "C", "E", "L"]
b.sort()
print(b)

# reverse : 리스트 요소의 순서를 반대로 뒤집음
# 리스트명.reverse()
a=[1, 2, 3, 4, 5]
a.reverse()
print(a)
# index : 해당 리스트에서 지정한 값의 index 위치를 반환
# 리스트명.index(값)
a=[1, 2, 3, 4, 5]
result = a.index(5)
print("리스트 a에서 5가 있는 위치는 : {0}".format(result))
print("리스트 a에서 검색한 위치는 {0}, 이고, 값은 {1}이다". format(result, a[4]))

# insert : 리스트에 요소 삽입하기(지정한 위치에)
# 리스트명.insert(index, 요소)
a.insert(2, 100)
print("insert 사용 후 리스트 a: {0}".format(a))

# remove : del과 함께 리스트의 요소를 삭제(첫 번째로 나오는 값)
# 리스트명.remove(값, )
a=[1,2,3,1,2,3]
print("원본리스트 a : {0}".format(a))
a.remove(2)
print("remove 후 리스트 a : {0}".format(a))

# pop : 리스트의 가장 마지막 요소를 끄집어 냄. (원본리스트에서 지정한 요소를 출력하고, 원본 리스트에서 삭제)
# 리스트명.pop(index)
a=[1, 2, 3, 4, 5]
print("원본리스트 a : {0}".format(a))
print("pop를 사용하여 꺼낸 값 : {0}". format(a.pop(3)))
a.pop(3)
print("pop 후 리스트 a : {0}".format(a))