#1
a = 0
while a < 5:
    a += 1
    if a == 3:
        continue
    print(a)
#2
a = 0
while a < 6:
    a += 1
    if a % 2 == 0:
        continue
    print(a)
#3
a = int(input())
while a > 0:
    a -= 1
    if a == 2:
        continue
    print(a)
#4
a = 0
while a < 5:
    a += 1
    if a == 4:
        continue
    print("a =", a)
#5
a = 1
while a <= 5:
    if a == 2:
        a += 1
        continue
    print(a)
    a += 1