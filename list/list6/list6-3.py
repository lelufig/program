def sq(a,b):
    if a > b:
        squ = a**2 - b**2
    else:
        squ = b**2 - a**2
    return squ
a = int(input("整数１："))
b = int(input("整数２："))
print(f"aの２乗とｂの２乗の差は{sq(a,b)}です")