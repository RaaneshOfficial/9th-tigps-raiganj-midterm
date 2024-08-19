# Pattern 1
a = "*"
for i in range(1, 6):
    print(a * i)

# Pattern 2
for j in range(5, 0, -1):
    for k in range(1, j + 1):
        print(k, end="")
    print()

# Pattern 3
for l in range(1, 6):
    for m in range(1, l + 1):
        print(chr(64 + m), end="")
    print()
