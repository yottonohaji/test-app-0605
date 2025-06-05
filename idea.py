import random

# ダミーの選手名とチーム名
players = [
    {"name": "山田 太郎", "team": "東京スワローズ"},
    {"name": "佐藤 健", "team": "大阪タイガース"},
    {"name": "鈴木 一郎", "team": "名古屋ドラゴンズ"},
    {"name": "田中 直樹", "team": "広島カープ"},
    {"name": "松本 亮", "team": "福岡ホークス"},
    {"name": "John Smith", "team": "New York Yankees"},
    {"name": "Mike Brown", "team": "Los Angeles Dodgers"},
    {"name": "David Lee", "team": "Chicago Cubs"},
    {"name": "Chris Johnson", "team": "Boston Red Sox"},
    {"name": "Alex Miller", "team": "San Francisco Giants"}
]

# 打席数（200～600）、安打数（打席数の1/6～1/2）をランダム生成
for player in players:
    at_bats = random.randint(200, 600)
    hits = random.randint(at_bats // 6, at_bats // 2)
    average = round(hits / at_bats, 3)
    player["at_bats"] = at_bats
    player["hits"] = hits
    player["average"] = average

# 表示
print(f"{'名前':<15} {'チーム':<20} {'打席数':<6} {'安打数':<6} {'打率':<5}")
for p in players:
    print(f"{p['name']:<15} {p['team']:<20} {p['at_bats']:<6} {p['hits']:<6} {p['average']:<5}")

# ...end of file...