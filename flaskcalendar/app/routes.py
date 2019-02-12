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

@app.route('/backend', methods=["POST", "GET"])
def backend():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    if request.method == "POST":
            title = request.form["title"]
            couse_id = request.form["course_id"]
            start = datetime.strptime(request.form['start'], '%d-%m-%Y %H:%M %p')
            end = datetime.strptime(request.form['end'], '%d-%m-%Y %H:%M %p')
            weight = request.form["weight"]
            new_assignment = Assignment(title=title, course_id=course_id, start=start,weight=weight , end=end,user_id=cuurrent_user.get_id())
            db_session.add(new_assignment)
            db_session.commit()

            return redirect("/backend", code=200)
    else:
            assignments = Assignment.query.all()
            return render_template('table.html', assignments=assignments)


@app.route('/index')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

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
