from flask import Flask, request, jsonify, render_template
from db import get_data
app = Flask(__name__)


@app.route("/")
def index():
    limit = request.args.to_dict().get('limit')
    data = get_data(str(50 if limit is None else limit))
    return render_template('index.html', data=data)


@app.route("/test")
def test():
    return jsonify({
        "test": "1"
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
