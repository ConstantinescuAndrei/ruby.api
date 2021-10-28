from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

prediction = 0

@app.route('/prediction', methods=['GET'])
def prediction():
    if request.method == 'GET':
        print(prediction)
        return '<h1>Prediction page</h1>'
    else:
        return '<h1>Wrong method</h1>'

if __name__ == '__main__':
    app.run()
