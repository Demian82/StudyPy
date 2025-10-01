# python basic grammar

# variable

# number type
x = 10    # int
y = 3.14    # flaot
a = 0o177    # octal/127
b = 0xABC    # hexadecimal/2748

# number operater
n = 3
m = 4
n / m    # 0.75
n ** m    # 81; powers

7 % 3    # 1; remainder
3 % 7    # 3
7 // 4    # 1; quotient

# string type
"Hello world"
'python is fun'
"""Life is too short, You need python"""
'''Life is too short, You need python'''

# 문자열 인덱싱
tail[2]    # 's', 문자열(배열) 0부터 시작

# 문자열 슬라이싱
# 변수[시작번호:끝번호]
tail[2:5]    # 's fu'

# 문자열 포매팅
# 문자열 포매팅에는 여러 형식이 있음으로 사용시 적합한 것을 찾아보기
# f 문자열 포매팅은 Python 3.6 이상에서만 가능
# "%포맷코드" % (변수1, 변수2, ...)
# 포맷 코드
# %s string, 어떤 형태의 값이든 변환해 삽입 가능
# %c character
# %d integer
# %f float
# %o octal
# %x hexadecimal
# %% literal % (문자 % 자체)

# "%10s" % a    -> 대입 값 우측정렬(길이가 10인 문자열 공간)
# "%-10s" % a    -> 대입 값 좌측정렬(길이가 10인 문자열 공간)
# "%.4f" % float    -> 소수점 4자리까지 표시

# list
# 리스트명 = [요소1, 요소2, 요소3, ...]

# tuple
# 요소값 변경 불가
# 생성 예시
# t1 = ()
# t2 = (1,)
# t3 = (1, 2, 3)
# t4 = 1, 2, 3
# t5 = ('a', 'b', ('ab', 'cd'))

# dictionary
# key를 통해 value를 얻음
# 순차성 보장x; 단, 3.7버전 이후 순서 보장
# dic {Key1: Value1, Key2: Value2, Key3: Value3, ...}
# key 값은 고유 불변, key값으로 리스트 사용불가 튜플은 사용가능

# 집합
# s1 = set([1, 2, 3])    # {1, 2, 3}
# s2 = set("Hello")    # {'e', 'H', 'l', 'o'}
# s3 = {1, 2, 3}    # {1, 2, 3}
# s4 = set()    # 빈 집합 / s = {} -> 딕셔너리
# 중복 x, 순서 x

# boolean
# True, False
# 자료형이 비어있음 or 0 or None-> False
# 자료형이 비어있지 않음 -> True
# and, or, not 연산자가 있음

# if 조건문 (control statement)
# if [condition expression]:
#     [statement1]
# elif [condition expression]:
#     [statement2]
# else:
#     [statement3]

# while 문
# while [condition expression]:
#     [statement1]
#     [statement2]
#     [statement3]
#     [continue/break]
# else:
#     [statement4]
# while 문의 else절은 while이 정상적으로 종료되었을때
#(break로 종료되지 않았을 때) 실행됨

# for 문
# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할_문장1
#     수행할_문장2
#     ...
# range함수를 자주 사용하게 됨
# list comprehension -> 리스트 안에 for 문을 포함하는 테크닉

# 함수
# def 함수_이름(매개변수):
#     수행할_문장1
#     수행할_문장2
#     ...
# 입력값이 여러개일 때 -> *매개변수 -> 입력값을 모아 튜플로 만듦
# 관례적으로 *args를 사용
# 키워드 인자에 대해서는
# https://docs.python.org/ko/3.13/tutorial/controlflow.html#defining-functions
# 의 4.9.2 항목 참고
# 리스트나 딕셔너리를 함수에 전달하면 원보이 변경될 수 있다

# 사용자 입출력
# input()
# 사용자가 키보드로 입력한 모든 것을 문자열로 저장
# 필요하다면 입력받은 값에 대한 형 변환 실행
# 
# 단지 디버깅을 위한 빠른 표시
# str(), repr()
# https://docs.python.org/ko/3.13/tutorial/inputoutput.html

# 파일 입출력
# 파일_객체 = open(파일_이름, 파일_열기_모드)
# 파일열기모드
# r : 읽기모드; 파일을 읽기만 할 때
# w : 쓰기모드; 파일에 내용을 쓸 때
# a : 추가모드; 파일의 마지막에 새로운 내용 추가할 때
# 파일 이름에 디렉터리를 포함할 수 있다
# 파일_객체.close()를 통해 파일을 직접 닫아 주는 것이 좋다

