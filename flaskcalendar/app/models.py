from app import db


class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=False, unique=False)
    start = db.Column(db.TIMESTAMP, index=False, unique=False)
    end = db.Column(db.TIMESTAMP, index=False, unique=False)
    weight = db.Column(db.String(64), index=False, unique=False)
    course_id = db.Column(db.String(120), index=False, unique=False)
    user_id = db.Column(db.String(120), index=False, unique=False)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Assignment {}:{}, start:{}, end:{}>'.format(self.id,self.title,self.start,self.end)
