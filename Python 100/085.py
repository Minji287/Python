w, h, b = map(int, input().split())

var = format(round((w * h * b / 8 / 1024 / 1024), 2), ".2f")
print(str(var) + " MB")