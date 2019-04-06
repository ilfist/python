# 파이썬에서 문자열처리
# 문자열은 ""혹은 ''로 감싸면 모두 문자열

print("Life is too short, You need Python")

a = "Life is too short"
print(a)
a= 'Life is too shrot'
print(a)

# """ """, ''' ''' 입력한 형태대로 출력할 때 사용
# 다른 언어는 ;(세미콜론) 사용하기 때문에 ;이 나오기 전가지 입력된 부분이 줄이 바껴도 에러 안남
# 파이썬은 ;을 사용안해. 입력 라인이 변경되면 입력 완료로 인식. 오류 발생할 가능성 있음
a="Life is too short, You need Python"
print(a)

b="""Life if
too short, 
You nedd Python"""
print(b)

# "''" : 문자열 내부에 홑따옴표 출력
# '""' 문자열 내부에 쌍따옴표 출력
# 
# 
c="쌍따옴표 "" 문자열을 출력합니다"
print(c)
c='쌍따옴표 "" 문자열을 출력합니다'
print(c)

d='홑따옴표 ''문자열을 출력합니다'
print(d)

d="홑따옴표 ''문자열을 출력합니다"
print(d)

d="쌍따옴표 \"\"문자열을 출력합니다"
print(d)
d='홑따옴표 \'\'문자열을 출력합니다'
print(d)
d="역슬래시 \\ 문자열을 출력"
print(d)

# 이스케이프 문자
# 문자열을 처리할 때 지정된 특수문자를 사용할 수 있도록 해주는 문자
# 주로 사용하는 이스케이프 문자 \n \t \\ \' \"

e="이스케이프 문자를 사용하면 이렇게 변경됩니다"
print(e)

f="이스케이프\n문자를\t\t사용하면 \b이렇게 \a 변경됩니다"
print(f)

# 문자열 연산
# 문자열 연산자는 +(문자열 연결 연산자) 뿐이었다. 
# 파이썬에는 문자열 곱셈 연산자 *가 있다. 입력된 숫자만큼 반복 출력한다

a="Hello"
b="World"
c=a+b
print(c)

c=a*3
print(c)

# 문자열 포매팅
# 문자열 출력 때 특수문자를 사용해 해당 위치에 원하는 데이터를 입력, 전체 문자열을 출력하는 방식
# 문자열 포맷코드 p.56 
# %s : 문자열 
# %c : 문자 1개
# %d : 정수
# %f : 실수
# %o : 8진수
# %x : 16진수
# %% : 문자 %
# {순번} .format(변수1, 변수2)

a=3
str="i eat %d apples" %a
print(str)

print("i eat %s apple" % "five")

number=10
day="three"

# 사용되는 특수문자마ㅏ 자료형이 지정돼 있어 사용될 데이터의 값을 구분하여 입력할 수 있음
print("i ate %d apples. So I was sick for %s days" % (number, day))
# 사용방법이 더 직관적. 자료형태를 구분할 필요가 없음.
print("i ate {0} apples. So I was Sick for {1} days".format(number, day))

# 문자열 관련 함수
# count : 문자 개수 확인
# 사용된 문자의 개수를 확인
a="hobby"
print("a=hobby")
print(a.count("b"))
print("변수 a에 포함된 문자 b의 개수")
# len : 문자열의 길이 확인
a="Hello World"
print(len(a))
print("변수 a에 포함된 문자 총 개수")

print("변수 a의 길이 : %d" %len(a))

# find : 문자의 위치 알려주기. 문자가 없으면 -1 출력

a="Python is best choice"
print("변수 a에서 문자 b의 위치는 {0}". format(a.find("b")))

# index : 문자의 위치 알려주기. 문자가 없으면 오류발생

# join : 지정한 위치에 문자 삽입
a=","
print(a.join("abcd"))

# strip : 양쪽 공백 삭제
a=" hi "
print(a)
print(a.strip())

# replace : 문자열 바꾸기
a="Life is too short"
print(a.replace("Life","Your leg"))

# split : 문자열 나누기
a="미세먼지:20, 초미세먼지:50, 날씨:흐림, 온도:19도"
b="20,50,흐림,19"
print(b.split(","))
c=a.split(",")
print(c)
print(c[0].split(":"))
b="20,50,흐림,19"
print(b.split(","))  

# 리스트는 하나의 이름으로 여러개의 변수를 모은 것