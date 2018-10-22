while True:
    while True:
        a = int(input("正の整数を入力してください："))
        if a > 0:
            break
        print("正でない整数を入力しないでください")
    for i in range(a):
        print("*", end = "")
    print()
    b = int(input("もう一度？【Yes：０/No：９】："))
    if b == 9:
        break
