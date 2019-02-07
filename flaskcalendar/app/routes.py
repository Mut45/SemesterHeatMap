from app import app
from app import db
from flask import url_for
from form import LoginForm
from flask_login import current_user, login_user, logout_user
from app.models import Admin,Course,Assignment
from flask import render_template,request,jsonify,flash,redirect,session,abort
import hashlib
from app import login

@login.user_loader
def load_user(id):
    return Admin.query.get(int(id))

@app.route('/')
def home():
    return redirect(url_for('login'))
# @app.route('/add')
# def add():
#     users = Admin.query.all()
#     u = User(username='john', email='john@example.com')
@app.route('/index')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    # if not session.get('logged_in'):
    #     return render_template("login.html")
    # else:
    #     return render_template("json.html")
    return render_template("json.html")

@app.route('/login',methods=['GET',"POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin is None or not admin.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(admin, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


    #     user = Admin.query.filter_by(username=request.form["username"]).first()
    #     if(user!= None):
    #         pass_hash = user.password_hash
    #         input_pass = request.form['password']
    #         input_hash =  hashlib.md5(input_pass.encode())
    #         print '1'
    #         if(input_hash == user.password_hash):
    #             session["logged_in"] = True
    #             session["username"] = request.form["username"]
    #             flash("You are now logged in")
    #             print '2'
    #             return redirect(url_for('index'))
    #         else:
    #             flash("Your password is incorrect.")
    #     else:
    #         print 'no'
    #         flash("Your username is incorrect.")
    # print '3'
    # return calendar()

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))



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
