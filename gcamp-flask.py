from flask import Flask, jsonify
from random import randint
import mysql.connector
from flask_cors import CORS
import ast

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#   return 'Hello World!'
cors = CORS(app, resources={"/api/*": {"origins": "*"}})

@app.route('/api/goods/default')
def get_goods_default():
    conn = mysql.connector.connect(
        user='root',
        password='root',
        host='39.106.28.185',
        port=3306,
        database='gcamp')

    cur = conn.cursor()
    query = "select * from goods"
    cur.execute(query)
    values = cur.fetchall()
    response = {
        'goods': [{
        'item_id': item_id,
        'title': title,
        'describe': describe,
        'link_map': ast.literal_eval(link_map),
        'image_map': ast.literal_eval(image_map),
        'answer_id': answer_id,
        'upvote': upvote
    } for (item_id, title, describe, link_map, image_map, answer_id, upvote) in values]}
    cur.close()
    conn.close()
    return jsonify(response)

@app.route('/api/test')
def random_number():
  response = {
    'randomNumber': randint(1, 100)
  }
  return jsonify(response)


if __name__ == '__main__':
  app.run()
