# random 모듈의 randint()를 사용하여 1에서 1000까지의 임의의 정수를 10개 생성하여
# random_numbers.txt 라는 이름의 파일로 저장하여라.
import random

numList = []

for i in range(10):
    num = random.randint(1, 1000)
    numList.append(num)

file = open("ramdomNum.txt", "w")
file.write(str(numList))
file.close
