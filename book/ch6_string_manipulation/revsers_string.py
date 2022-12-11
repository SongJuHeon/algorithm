#문자열을 뒤집는 함수를 작성하라, 입력값은 문자 배열이며, 리턴없이 리스트 내부를 직접 조작하라

# type hint를 언어 차원에서 지원하기 위해 typing 모듈이 추가되었음,
# List, Dict, Tuple, Set 지원
from typing import List

class revers_string:
    def reverse_string_two_pointer(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def revers_string_pythonic(self, s: List[str]) -> None:
        s.reverse()
        #s = s[::-1]
        #s[:] = s[::-1]


in_list = ["h", "e", "l", "l", "o"]

print(in_list)

rs = revers_string()
rs.reverse_string_two_pointer(in_list)

print(in_list)

rs.revers_string_pythonic(in_list)
print(in_list)