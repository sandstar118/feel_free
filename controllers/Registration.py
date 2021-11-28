from flask import jsonify, request, make_response
import sqlite3

dbname = 'FeelFree.db'

def registration(request):

    body = request.json
    
    if(body is None):
        return make_response('', 400)
    if(not ('title' in body and  'address' in body and 'image_url' in body )):
        return make_response('', 400)

    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("INSERT INTO places (title, address, image_url) VALUES (:title, :address, :image_url)", (body['title'], body['address'], body['image_url']))
    conn.commit()
    conn.close()

    return make_response('', 200)