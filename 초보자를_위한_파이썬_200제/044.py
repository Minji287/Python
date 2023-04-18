import time
import mylib as ml
import mypackage.mylib as mpml # 패키지(mypackage)는 디렉토리

ret1 = mpml.mylib.add_txt('대한민국', '1등')
ret2 = mpml.mylib.reverse(1, 2, 3)
print(ret1)
print(ret2)

time.sleep(1)
print(mylib.add_txt('나는','파이썬이다'))

from time import sleep # time에 있는 것에서 sleep만 import
from mypackage import mylib # mypackage에 있는 것에서 mylib만 import
from mypackage.mylib import reverse
# from 을 쓰면 모듈명 안쓰고 함수명만 사용 가능

sleep(2)
print(reverse(2, 3, 4))