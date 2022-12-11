# list comprehension
# 기존 리스트를 기반으로 새로운 리스트 생성
import collections
import re
import sys

print(list(map(lambda x : x + 10, [1, 2, 3])))

print([n * 2 for n in range(1, 10+1) if (n % 2 == 1)])

# 제너레이터
# 루프의 반복 동작을 제어할 수 있는 루틴 형태
# yield로 현재 값 내보내고, next로 값 추출해서 쓰기
"""
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

g = get_natural_number()

for _ in range(0, 100):
    print(next(g))

# range()도 제너레이터.
a = [n for n in range(1000000)]
b = range(1000000)

print(len(a))
print(len(b))
print(len(a) == len(b))

#print(a)
print(type(a))

#print(b)
print(type(b))

print(sys.getsizeof(a))
print(sys.getsizeof(b))
"""
# enumerate
# 여러가지 자료형을 인덱스를 포함한 enumerate 객체로 리턴
a = [1, 2, 3, 2, 45, 2, 6]
print(a)
print(list(enumerate(a)))

b = ['a1', 'a2', 'a3']

for i, j in enumerate(b):
    print(i, j)

# pass
# 개발 중 목업 먼저 만들고 진행할때 유용하게 사용, null연산

class MyClass(object):
    def method_a(self):
        pass
    def method_b(self):
        print("Method B")

c = MyClass()

# locals()
# 로컬에 선언된 모든 변수를 조회, 디버깅할때 많이 사용
import pprint
pprint.pprint((locals()))

# 리스트
a = list
#or
a = []
a = [1, 2, 3]

#리스트 마지막에 값 추가
a.append(4)
print(a)

#중간삽입, 인덱스, 값 순서
a.insert(3, 5)
print(a)

# 값 추가시 리스트 값에 구애받지 않음
a.append("hi")
a.append(True)
print(a)

#슬라이싱
#[i, j] -> 인덱스 i부터 j-1ㅂ까지 슬라이싱
print(a[1:3])
print(a[:3])
print(a[4:])
print(a[1:4:2])

#예외처리

try:
    print(a[9])
except IndexError:
    print("존재하지 않는 인덱스")

#값 삭제
#인덱스로 삭제할 수도, remove(값)로 삭제할 수도 있다.
del a[1]
print(a)
a.remove(3)
print(a)

#스택의 pop연산 가능
print(a.pop(3))
print(a)

#딕셔너리
a = dict #or
a = {}

a = {'key1': 'value1', 'key2': 'value2'}
print(a)
a['key3'] = 'value3'
print(a)

#없는 키 조회시
try:
    print(a['key4'])
    #del a['key4']
except KeyError:
    print("존재하지 않는 키")

print('key4' in a)

if 'key4' in a:
    print("존재 키")
else:
    print("미존재 키")

for k, v in a.items():
    print(k, v)

#defaultdict 객체
#없는 인덱스 조회시 에러 출력이 아닌 디폴트 값 기준으로 해당키의 딕셔너리를 생성해줌
a = collections.defaultdict(int)
a['A'] = 5
a['B'] = 4
print(a)

#counter 객체
# 아이템에 대한 개수 계산 후 딕셔너리로 리턴
a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
b = collections.Counter(a)
print(b)

#가장 많은 빈도수
print(b.most_common(2))