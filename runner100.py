import random

# ダミーの名前リスト（日本人名と外国人名を混ぜて50名分）
names = [
    "佐藤 大輔", "鈴木 一郎", "高橋 健太", "田中 翔太", "伊藤 直樹",
    "渡辺 拓海", "山本 亮", "中村 優斗", "小林 海斗", "加藤 大地",
    "吉田 颯太", "山田 陸", "佐々木 悠真", "山口 智也", "松本 直人",
    "井上 颯", "木村 悠斗", "林 大和", "斎藤 陽斗", "清水 悠真",
    "Alex Johnson", "Michael Smith", "David Brown", "James Williams", "John Miller",
    "Robert Davis", "William Wilson", "Richard Moore", "Joseph Taylor", "Charles Anderson",
    "Thomas Jackson", "Christopher White", "Daniel Harris", "Matthew Martin", "Anthony Thompson",
    "Mark Garcia", "Paul Martinez", "Steven Robinson", "Andrew Clark", "Joshua Rodriguez",
    "Kevin Lewis", "Brian Lee", "George Walker", "Edward Hall", "Ronald Allen",
    "Timothy Young", "Jason King", "Jeffrey Wright", "Ryan Scott", "Jacob Green"
]

# 年齢（18～35歳）、身長（165～195cm）、タイム（9.56～12.99秒）をランダム生成
athletes = []
for name in names:
    age = random.randint(18, 35)
    height = round(random.uniform(166, 195), 1)
    time = round(random.uniform(9.56, 12.99), 2)
    athletes.append({
        "name": name,
        "age": age,
        "height": height,
        "time": time
    })

# タイムが良い順（昇順）に並び替え
athletes_sorted = sorted(athletes, key=lambda x: x["time"])

# 結果表示
print(f"{'順位':<4} {'名前':<20} {'年齢':<4} {'身長(cm)':<8} {'タイム(秒)':<8}")
for i, athlete in enumerate(athletes_sorted, 1):
    print(f"{i:<4} {athlete['name']:<20} {athlete['age']:<4} {athlete['height']:<8} {athlete['time']:<8}")

# ...end of file...