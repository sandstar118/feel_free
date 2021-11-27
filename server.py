from flask import Flask, jsonify
import sqlite3

dbname = 'FeelFree.db'


def get_places():
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("SELECT * FROM places WHERE purpose IS NULL")
    data = []
    for row in cur:
        data.append({ "id":  row[0], "title": row[1], "created_at": row[3]})
    conn.close()
    return data

def get_place(id):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("SELECT * FROM places WHERE  purpose IS NULL AND id = :id", { "id": id})
    row = cur.fetchone()
    if(row):
        data = { "id":  row[0], "title": row[1], "address": row[2], "created_at": row[3]}
        result = True
    else:
        data = {}
        result = False
    conn.close()
    return data, result

def registration(title, address):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute('INSERT INTO places(title, address) VALUES(:title, :address)', (title, address))
    conn.commit()
    conn.close()

def reserve(id, purpose):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute('UPDATE places set purpose = ? WHERE id = ?', (id, purpose))
    conn.commit()
    conn.close()

app = Flask(__name__)

@app.route('/places', methods = ["GET"])
def places():
    return jsonify( get_places() )

@app.route('/place/<id>', methods = ["GET"])
def place(id):
    data, result = get_place(id)
    return jsonify( data ), 200 if result else 404

if __name__ == '__main__':
    app.run()