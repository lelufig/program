while True:
    a = int(input("正の整数を入力してください"))
    if a > 0:
        break
    print("正でない整数を入力しないでください")
while True:
    if a > 0:
        print(f"{a % 10}", end="")   
        a = int(a / 10)
    else:
        break
print()




    