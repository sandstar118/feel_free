from flask import jsonify
import sqlite3

dbname = 'FeelFree.db'

def get_lend(id):
    # 貸出状態の取得
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("SELECT * FROM lend")
    data = []
    for row in cur:
        data.append({ "id":  row[0], "place_id": row[1], "begin_date": row[3], "end_date": row[4], "purpose":row[5]})
    conn.close()
    return jsonify(data)
    
