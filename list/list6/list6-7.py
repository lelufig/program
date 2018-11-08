def f(a):
    for i in range(a):
        for j in range(i+1):
            print("*", end = "")
        print()

while True:
    f(int(input("整数を入力：")))