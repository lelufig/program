a=int(input("正の整数："))
for i in range(a):
    if i % 3 == 0:
        print("+", end="")
    else:
        print("-", end="")
print()