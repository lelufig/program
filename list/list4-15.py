a = int(input("整数値："))
for i in range(1,a+1):
    if a % i == 0:
        print(i, end =" ")
print()