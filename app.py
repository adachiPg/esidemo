from flask import Flask, jsonify

from inquiry import procAq

app = Flask(__name__)
# app.config.from_object('config.DevConfig')
app.config.from_object('config.ProdConfig')

data = [
        {
            "id": 1,
            "library": "Pandas",
            "language": "Python"
        },
        {
            "id": 2,
            "library": "requests",
            "language": "Python"
        },
        {
            "id": 3,
            "library": "NumPy",
            "language": "Python"
        }
    ]

@app.route('/')
def hello():
    return "Hello Flask-Heroku"

@app.route('/inquiry', methods=['GET'])
def inquiry():
    procAq()
    return 'test inquiry'


@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=False)