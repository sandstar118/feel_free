from flask import jsonify, request
import sqlite3

dbname = 'FeelFree.db'

def registration(request):
    return