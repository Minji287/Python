# 다음과 같은 list1, list2가 있을 경우 list1과 list2의 각 원소의 곱셈을 다음과 같이 출력하시오.
"""
- 실행 결과
- 3 * 2 = 6
- 3 * 3 = 9
- 3 * 4 = 12
- 3 * 5 = 15
- 3 * 6 = 18
...
- 7 * 2 = 14
- 7 * 3 = 21
- 7 * 4 = 28
- 7 * 5 = 35
- 7 * 6 = 42
"""

list1 = [3, 5, 7]
list2 = [2, 3, 4, 5, 6]

for i in range(len(list1)):
    for j in range(len(list2)):
        print(str(list1[i]) + " * ", end='')
        print(str(list2[j]) + " = " + str(list1[i]*list2[j]))

