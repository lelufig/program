a = int(input("何月ですか："))
season = "ありません"
if 3 <= a <= 5:
    season = "春です"
elif 6 <= a <= 8:
    season = "夏です"
elif 9 <= a <=11:
    season = "秋です"
elif 1 <= a <= 12:
    season = "冬です"

print(f"{a}月は{season}")