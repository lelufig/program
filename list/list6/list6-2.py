def max(a,b,c):
    max2 = a
    if max2 < b:
        max2 = b
    if max2 < c:
        max2 = c
    return max2
a = int(input("整数１："))
b = int(input("整数２："))
c = int(input("整数３："))
print(f"最大値は{max(a,b,c)}です")

    