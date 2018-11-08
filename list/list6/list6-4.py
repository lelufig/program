def max(a,b):
    if a > b:
        max2 = a
    else:
        max2 = b
    return max2

a = int(input("整数１："))
b = int(input("整数２："))
c = int(input("整数３："))
d = int(input("整数４："))
print(f"大きい方の値は{max(max(max(a,b),c),d)}です")