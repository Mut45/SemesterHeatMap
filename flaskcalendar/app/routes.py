from app import app
from app import db
from app.models import Admin,Course,Assignment
from flask import render_template,request,jsonify,flash,redirect,session,abort
import hashlib
from flask_login import LoginManager
from flask_security import login_required


@app.route('/')
@app.route('/add')
def add():
    users = Admin.query.all()
    u = User(username='john', email='john@example.com')
@app.route('/index')
def calendar():
    if not session.get('logged_in'):
        return render_template("login.html")
    else:
        return render_template("json.html")

@app.route('/login',methods=['GET',"POST"])
def login():
    users = Admin.query.all()
    print users
    if request.method == "POST":
        flash('yes')

        user = Admin.query.filter_by(username=request.form["username"]).first()
        if(user!= None):
            pass_hash = user.password_hash
            input_pass = request.form['password']
            input_hash =  hashlib.md5(input_pass.encode())
            print '1'
            if(input_hash == user.password_hash):
                session["logged_in"] = True
                session["username"] = request.form["username"]
                flash("You are now logged in")
                print '2'
                return redirect(url_for('index'))
            else:
                flash("Your password is incorrect.")
        else:
            print 'no'
            flash("Your username is incorrect.")
    print '3'
    return calendar()





@app.route('/data')
def return_data():
    start_date = request.args.get('start', '')
    end_date = request.args.get('end', '')
    # You'd normally use the variables above to limit the data returned
    # you don't want to return ALL events like in this code
    # but since no db or any real storage is implemented I'm just
    # returning data from a text file that contains json elements

    with open("app/events.json", "r") as input_data:
        # you should use something else here than just plaintext
        # check out jsonfiy method or the built in json module
        # http://flask.pocoo.org/docs/0.10/api/#module-flask.json
        return input_data.read()
