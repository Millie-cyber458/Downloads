from flask import Flask, render_template, jsonify
import pymysql
from config import DB_CONFIG
app = Flask(__name__)
@app.route('/')
#helper functioin to fetch companies that are already on the grid
def home():
    conn = pymysql.connect(**DB_CONFIG)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM Companies")
    companies = cursor.fetchall()
    conn.close()
    return render_template('home.html', Companies=companies)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)



