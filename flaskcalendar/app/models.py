from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# Note: foriegn key constraints are not added due to the fact that SQLite is not enforcing it anyway and its causing
# the migration to fail
class Assignment(db.Model):
    __tablename__ = 'assignment'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=False, unique=False)
    start = db.Column(db.DateTime, index=False, unique=False)
    end = db.Column(db.DateTime, index=False, unique=False)
    weight = db.Column(db.String(64), index=False, unique=False)
    course_id = db.Column(db.Integer,db.ForeignKey('course.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('admin.id'))
    time_stamp = db.Column(db.DateTime, index=True, default= datetime.utcnow)


    def __repr__(self):
        return '<Assignment {}:{}, start:{}, end:{}>'.format(self.id,self.title,self.start,self.end)

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=False, unique=False)
    semester = db.Column(db.String(64), index=False, unique=False)
    year = db.Column(db.Integer, index=False, unique=False, default = 2017)
    teacher = db.Column(db.String(128), index=False, unique=False)
    session = db.Column(db.String(32), index=False, unique=False)
    assignments = db.relationship('Assignment',backref = 'course',lazy= 'dynamic',primaryjoin = "Assignment.course_id==Course.id")

    def __repr__(self):
        return '<Course {}:{}, session:{}>'.format(self.id,self.title,self.session)


class Admin(UserMixin,db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    assignments = db.relationship('Assignment',backref = 'author',lazy= 'dynamic',primaryjoin = "Assignment.user_id ==Admin .id") # The lazy argument defines how the database query for the relationship will be issued
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self):
        return '<Admin {}>'.format(self.id)
