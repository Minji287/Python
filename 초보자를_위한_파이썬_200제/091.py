txt = 'A lot of things occur each day, every day.'

word_count1 = txt.count('o')
word_count2 = txt.count('day')
word_count3 = txt.count(' ')
print(word_count1)
print(word_count2)
print(word_count3)
print()

offset1 = txt.find('e')
offset2 = txt.find('day')
offset3 = txt.find('day', 30)
print(offset1)
print(offset2)
print(offset3)
print()

ret1 = txt.split(' ')
ret2 = txt.split('a')
print(ret1)
print(ret2)
print()

log = 'name:홍길동 age:17 sex:남자 nation:조선'
ret3 = log.split()
for data in ret3:
    d1, d2 = data.split(':')
    print('%s->%s'%(d1,d2))