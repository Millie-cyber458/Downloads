from flask import Flask, render_template, jsonify

app = Flask(__name__)
@app.route('/')

def home():  return render_template('home.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

    app.route('/Community')

    app.route('/About')

    @app.routr('/')
    def home():
        return render_template('home.html', LiveClass=LiveClass)
