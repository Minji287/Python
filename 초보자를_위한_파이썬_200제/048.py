# f1 = open("mylib.py", "r") # r = 텍스트 모드로 읽기
# f2 = open("D:\python\Python\초보자를_위한_파이썬_200제\images\10.jpg", "rb") # 파일이 반드시 존재
# f3 = open('text.txt', 'w') # 파일이 존재하면 기존 데이터 삭제, 존재하지 않으면 생성
# f4 = open('text.txt', 'a') # append(파일 지우지 않고 추가)

# f1.close()
# f2.close()
# f3.close()
# f4.close()

f1 = open("D:\python\Python\초보자를_위한_파이썬_200제\mylib.py", "r")

while True:
    line = f1.readline()
    if not line :
        break
    print(line, end='')

f1.close()