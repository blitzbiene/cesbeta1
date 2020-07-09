from flask import Flask,render_template,redirect,request, session, g
import sqlite3
app = Flask(__name__)

app.config['SECRET_KEY'] = "Thisisasecret!!!"


# database connection code
def connect_db():
    sql = sqlite3.connect('data.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g,'sqlite_db'):
        g.sqlite_db=connect_db()
    return g.sqlite_db
@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close()
#database connection code ends


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/executives')
def executives():
    return render_template('executives.html')

@app.route('/vidhaan')
def vidhaan():
    return render_template('vidhaan.html')



@app.route('/verify',methods=["GET","POST"])
def verify():
    if request.method=="POST":
        reference = request.form['certiverify']
        db=get_db()
        try:
            cur = db.execute('select * from certi where reference_no=?',[reference])
            res = cur.fetchone()
            if res:
                return render_template('after_verify.html',res=res,fraud=True)
        except:
            return render_template('after_verify.html',fraud='False')

    return render_template('verification_portal.html')


if __name__ == "__main__":
    app.run(debug=True)
