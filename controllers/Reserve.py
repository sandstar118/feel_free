from flask import jsonify, request
import sqlite3

dbname = 'FeelFree.db'

def reserve(request):
    return