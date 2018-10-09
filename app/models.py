from app.database.database import Database
from passlib.hash import pbkdf2_sha256 as sha256

class Users:
    def __init__(self, username,password,email):
        self.username = username
        self.password = password
        self.email = email

    def check_user(self):
        db = Database()
        if db.check_table("users") :
            query = "insert into users(username, email, password) values (%s, %s, %s)"
            user_details = (self.username, self.email, sha256.hash(self.password))
            db.add_user(self.username, self.email, sha256.hash(self.password))
            return ("User added")
        else:
            db.create_connection().execute("create table users(user_id serial primary key,username varchar(25) not null, email varchar(25) not null, password varchar not null)")
            db.create_connection().close
            db.commit()
            query = "insert into users(username, email, password) values (%s, %s, %s)"
            user_details = ( self.username, self.email, self.password)
            db.create_connection().execute(query, user_details)
            db.create_connection().con.commit()
            return ("User created")