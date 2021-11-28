from flask import jsonify
import sqlite3

dbname = 'FeelFree.db'

# 場所一覧の取得
def get_places():
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("SELECT * FROM places")
    data = []
    for row in cur:
        data.append({ "id":  row[0], "title": row[1], "image_url": row[3], "created_at": row[4]})
    conn.close()
    return jsonify(data)

# 場所の詳細の取得
def get_place(id):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("SELECT * FROM places WHERE  id = :id", { "id": id})
    row = cur.fetchone()
    if(row):
        data = { "id":  row[0], "title": row[1], "address": row[2], "image_url": row[3], "created_at": row[4]}
        result = True
    else:
        data = {}
        result = False
    conn.close()
    return jsonify( data ), 200 if result else 404