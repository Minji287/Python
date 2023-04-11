a, b = map(int, input().split())
print(bool((a and b) or (not a and not b)))