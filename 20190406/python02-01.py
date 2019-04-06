# 주석 사용 (ctrl+/)
# 파이썬 소스코드에 # 기호를 사용하면 주석이 입력된다
# 주석은 소스코드에 입력이 되어 있어도 아무런 영향이 없다.

# 파이썬은 숫자 자료형으로 정수형과 숫자형을 모두 지원
a = 123 #정수형 입력
print(a)

b = 1.5 #실수형 입력
print(b)
# 8진수 16진수 모두 사용 가능
# 8진수 입력 시 영어 대문자 0o숫자 형태로 사용
# 파이썬의 기본 숫자형은 10진수
c = 0o123
print(c)

# 16진수 입력시 숫자 0x숫자 형태로 사용
d = 0x123
print(d)

d = 0xABC
print(d)

# 복소수 사용가능
a=1+2j 
b=3-4j
print(a)
print(b)
print(a.real)
print(b.real)

# 기본 4칙연산을 사용할 수 있음
a = 3
b = 4
c = a + b
print(c)

c = a - c
print(c)

c=a*b
print(c)

c=a/b
print(c)

c=a%b
print(c)

# 파이썬은 제곱 연산자가 존재
c=a**b
print(c)
