n = int(input())
souoc = 0
for i in range(1, n + 1):
    if n % i == 0:
        souoc += 1
    if souoc > 2:
        break
if souoc == 2:
    print(n, "là số nguyên tố")
else:
    print(n, "không là số nguyên tố")