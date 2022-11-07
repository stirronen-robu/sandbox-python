from flask import Flask, render_template
from flask_cors import cross_origin

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
@cross_origin()
def health():
    return 'hello, silja!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=False)
