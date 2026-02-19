#1
a = 1
while True:
    print(a)
    if a == 5:
        break
    a += 1
#2
a = int(input())
while True:
    if a == 0:
        break
    print(a)
    a = int(input())
#3
a = 1
while a <= 10:
    if a == 6:
        break
    print(a)
    a += 1
#4
a = int(input())
while a > 0:
    if a == 3:
        break
    print(a)
    a -= 1
#5
a = 0
while True:
    a += 1
    if a == 4:
        break
    print(a)