print("３つの整数を入力してください")
a = int(input("整数１："))
b = int(input("整数２："))
c = int(input("整数３："))
max = a
if max < b:
    max = b
if max < c:
    max = c
print(f"最大値は{max}です")
