score = int(input('점수를 입력하세요: '))
if score >= 90:
    print(score, '점은 A 입니다.')
elif score >= 80:
    print(score, '점은 B 입니다.')
elif score >= 70:
    print(score, '점은 C 입니다.')
elif score >= 60:
    print(score, '점은 D 입니다.')
else:
    print(score, '점은 F 입니다.')

