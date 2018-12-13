# Import Dependencies
from flask import Flask, jsonify, render_template
from analyzer import analyzer
from handles import get_handles

# Create flask app
app = Flask(__name__)

# Default route
@app.route('/')
def index():

    return render_template('index.html')

@app.route('/data')
def data():
    data = analyzer()

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
