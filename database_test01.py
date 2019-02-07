from app import db
from app.models import Admin,Course,Assignment
import hashlib

password = "testing123"
pass_hash = hashlib.md5(password.encode())
a = Admin(id=1,username="user01",password_hash=pass_hash.hexdigest())
