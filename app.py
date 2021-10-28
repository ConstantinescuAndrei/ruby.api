from flask import Flask, request

app = Flask(__name__)

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
