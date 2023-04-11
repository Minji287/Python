a, b = map(int, input().split())
print(bool(((not a) and b) or (a and (not b))))