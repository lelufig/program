a = int(input("整数１："))
b = int(input("整数２："))
def max(a,b):
    if a > b:
        max2 = a
    else:
        max2 = b
    return max2
print(f"大きい方の値は{max(a,b)}です")