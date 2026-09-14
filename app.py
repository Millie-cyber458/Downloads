from flask import Flask, render_template, jsonify
import pymysql
from config import DB_CONFIG
app = Flask(__name__)
@app.route('/')
#helper functioin to fetch live classes from the database


def get_live_classes():
    conn = pymysql.connect(**DB_CONFIG)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM LiveClass")
    LiveClass = cursor.fetchall()
    conn.close()
    return LiveClass

    @app.route('/')
    def home():
        LiveClass = get_live_classes()
        return render_template('home.html', LiveClass=LiveClass)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)



