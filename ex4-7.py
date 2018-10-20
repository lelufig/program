a = int(input("正の整数："))
for i in range(1,a):
    if 2**i < a:
        print(2**i)