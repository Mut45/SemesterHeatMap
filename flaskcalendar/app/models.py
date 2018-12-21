from app import db
from datetime import datetime
# Note: foriegn key constraints are not added due to the fact that SQLite is not enforcing it anyway and its causing
# the migration to fail
class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=False, unique=False)
    start = db.Column(db.DateTime, index=False, unique=False)
    end = db.Column(db.DateTime, index=False, unique=False)
    weight = db.Column(db.String(64), index=False, unique=False)
    course_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    time_stamp = db.Column(db.DateTime, index=True, default= datetime.utcnow)

    #password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Assignment {}:{}, start:{}, end:{}>'.format(self.id,self.title,self.start,self.end)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=False, unique=False)
    semester = db.Column(db.String(64), index=False, unique=False)
    year = db.Column(db.Integer, index=False, unique=False, default = 2017)
    teacher = db.Column(db.String(128), index=False, unique=False)
    session = db.Column(db.String(32), index=False, unique=False)
    assignments = db.relationship('Assignment',backref = 'course',lazy= 'dynamic')

    def __repr__(self):
        return '<Course {}:{}, session:{}>'.format(self.id,self.title,self.session)


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(128))
    assignments = db.relationship('Assignment',backref = 'author',lazy= 'dynamic') # The lazy argument defines how the database query for the relationship will be issued
    def __repr__(self):
        return '<Admin {}>'.format(self.id)
