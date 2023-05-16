# 1~45번 숫자에서 6개의 숫자로 이루어진 로또 추출기를 아래 실행화면과 같이 구현하시오
# (조건 1 : 1초후에 1줄씩 출력할 것, 조건 2 : 로또 횟수를 입력받으시오)

import time
import random

numList = []
game = int(input("로또 게임 횟수를 입력하시오 : "))

for i in range(1, game+1):
    for j in range(6):
        num = random.randint(1, 45)
        numList.append(num)
    time.sleep(1)
    print("로또번호[" + str(i) + "] : " + str(numList))
    numList = []
