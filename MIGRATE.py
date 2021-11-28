import sqlite3


# データベース名
dbname = 'FeelFree.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# 場所
cur.execute("DROP TABLE IF EXISTS places")
cur.execute("CREATE TABLE places(id INTEGER PRIMARY KEY, title TEXT NOT NULL, address TEXT NOT NULL, image_url TEXT, created_at  DATETIME DEFAULT CURRENT_TIMESTAMP)")

# 貸し出し履歴
cur.execute("DROP TABLE IF EXISTS lend")
cur.execute("CREATE TABLE lend(id INTEGER PRIMARY KEY, place_id INT NOT NULL,  begin_date DATETIME NOT NULL, end_date DATETIME NOT NULL, purpose TEXT)")

# 初期データの挿入
cur.execute('INSERT INTO places(title, address) VALUES("ABCスペース", "○○県○○市○○")')
conn.commit()

# 初期データの確認
# cur.execute("SELECT * FROM places")
cur.execute("SELECT * FROM places WHERE id = :id", { "id": "1" })
for row in cur:
    print("id: " + str(row[0]) + ", title: " + str(row[1]) + ", address: " + str(row[2]) + ", image_url: " + str(row[3]) + ", created_at: " + str(row[4]) )

# データベースへのコネクションを閉じる。(必須)
conn.close()

