from flask import Flask, jsonify
from random import randint

from flask_cors import CORS

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#   return 'Hello World!'
cors = CORS(app, resources={"/api/*": {"origins": "*"}})


@app.route('/api/test')
def random_number():
  response = {
    'randomNumber': randint(1, 100)
  }
  return jsonify(response)


if __name__ == '__main__':
  app.run()
