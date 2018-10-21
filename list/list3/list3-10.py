a = int(input("整数を入力してください"))
if a > 0:
    if a % 2 == 0:
        print("その数は偶数です")
    elif a % 2 != 0:
        print("その数は奇数です")
elif a <= 0:
    print("正でない値が入力されました")