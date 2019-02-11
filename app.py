from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flask'
mysql = MySQL(app)

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM computer")
    rv = cur.fetchall()
    cur.close()
    return render_template('home.html', computers=rv)

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/simpan', methods=["POST"])
def simpan():
    nama = request.form['nama']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO computer (data) VALUES (%s)", (nama,))
    mysql.connection.commit()
    return redirect(url_for('home'))
