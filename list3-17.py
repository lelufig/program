a = int(input("何月ですか："))
if 3 <= a <= 5:
    print(f"{a}月は春です")
if 6 <= a <= 8:
    print(f"{a}月は夏です")
if 9 <= a <=11:
    print(f"{a}月は秋です")
if 0 < a <=2 or 12 == a:
    print(f"{a}月は冬です")
else:
    print(f"{a}月はあっりませーーーーん")