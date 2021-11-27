import sqlite3


# データベース名
dbname = 'FeelFree.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# 場所
cur.execute("DROP TABLE IF EXISTS places")
#cur.execute("CREATE TABLE places(id INTEGER PRIMARY KEY, title TEXT NOT NULL, address TEXT NOT NULL, created_at  DATETIME DEFAULT CURRENT_TIMESTAMP)")
cur.execute("CREATE TABLE places(id INTEGER PRIMARY KEY, title TEXT NOT NULL, address TEXT NOT NULL, created_at  DATETIME DEFAULT CURRENT_TIMESTAMP, purpose TEXT DEFAULT NULL)")

# 貸し出し履歴
#cur.execute("DROP TABLE IF EXISTS lend")
#cur.execute("CREATE TABLE lend(id INTEGER PRIMARY KEY, place_id INT NOT NULL,  state INTEGER NOT NULL, purpose TEXT, timestamp  DATETIME DEFAULT CURRENT_TIMESTAMP)")

# 初期データの挿入
cur.execute('INSERT INTO places(title, address) VALUES("ABCスペース", "○○県○○市○○")')
conn.commit()

# 初期データの確認
# cur.execute("SELECT * FROM places")
cur.execute("SELECT * FROM places WHERE id = :id", { "id": "1" })
for row in cur:
    print("id: " + str(row[0]) + ", title: " + str(row[1]) + ", address: " + str(row[2]) + ", created_at: " + str(row[3]) + ", purpose: " + str(row[4]))

# データベースへのコネクションを閉じる。(必須)
conn.close()

