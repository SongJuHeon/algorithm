# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
# 책에서는 실행속도가 list > deque > slising 이였으나,
# 내 맥북에서 돌린 결과 slising > list, deque (list, deque는 비슷한 수준) 이였다.
# 정반대의 결과 -> 정규식으로 검증하는 부분이 시간이 오래걸렸음
import collections
import time
import collections
import re
from datetime import timedelta


class palindrom:
    def is_palindrom_list(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

    def is_palindrom_deque(self, s: str) -> bool:
        strs = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True

    def is_palindrom_slising(self, s: str) -> bool:
        """
        s = s.lower()
        s = re.sub('[^a-z@0-9]', '', s)

        return s == s[::-1]
        """
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        return strs == strs[::-1]


if __name__ == '__main__':
    in_str0 = "my name is song"
    in_str1 = "A man, a plan, a canal: Panama"
    pal = palindrom()


    start = time.process_time()
    pal.is_palindrom_list(in_str1)
    end = time.process_time()

    print(f'Time elapsed: {end - start: .6f}')
    print("Time elapsed: ", timedelta(seconds=end - start))

####################################

    start = time.process_time()

    pal.is_palindrom_deque(in_str1)
    end = time.process_time()

    print(f'Time elapsed: {end - start: .6f}')
    print("Time elapsed: ", timedelta(seconds=end - start))

####################################
    start = time.process_time()
    pal.is_palindrom_slising(in_str1)
    end = time.process_time()

    print(f'Time elapsed: {end - start: .6f}')
    print("Time elapsed: ", timedelta(seconds=end - start))