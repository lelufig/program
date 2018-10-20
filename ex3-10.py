print("3つの整数を入力して下さい")
a = int(input("整数a："))
b = int(input("整数b："))
c = int(input("整数c："))
if a == b == c:
    print("３つの値は正しいです")
elif a == b or b == c or a == c:
    print("２つの値が等しいです")
else:
    print("3つの値は異ります")