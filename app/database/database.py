import os
import psycopg2
from urllib.parse import urlparse
from flask import jsonify
from passlib.hash import pbkdf2_sha256 as sha256
# from app.app import app1
from flask_jwt_extended import \
    (create_access_token, create_refresh_token, jwt_required,
     jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from dotenv import find_dotenv, load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Database:
    def __init__(self):
        self.con = ''
        self.cur = ''

    def create_connection(self):
        try:
            database = urlparse(os.environ.get("DATABASE_URI"))
            print(database)
            username = database.username
            password = database.password
            print (database.username)
            database = database.path[1:]
            hostname = database.hostname
            portno = 5432
            con = psycopg2.connect(
                database="fastfoodapp",
                user=username,
                host=hostname,
                password=password,
                port=portno
            )
            self.cur = con.cursor()
            return self.cur
        except ValueError:
            return ("Cannot connect to database")

    def commit(self):
        result = urlparse(os.environ.get('DATABASE_URI'))
        username = result.username
        password = result.password
        print (result.username)
        database = result.path[1:]
        hostname = result.hostname
        portno = 5432
        con = psycopg2.connect(
                database="fastfoodapp",
                user=username,
                host=hostname,
                password=password,
                port=portno
            )
        return con.commit()

    def check_table(self, table_name):
        self.create_connection().execute("select * from information_schema.tables where table_name=%s", (table_name,))
        return bool(self.cur.rowcount)
        # self.connection().execute("select * from information_schema.tables where table_name=%s", (table_name,))
        # if (self.connection().rowcount) == -1:
        #     return False
        # return True
        
        

    def add_user(self, email, name, password):
        """method inserts new user into db"""
        insert_command = "INSERT INTO users(email, name, password, role) VALUES('%s', '%s', '%s');" % (
            email, name, password)
        try:
            self.cur.execute(insert_command)
            self.cur.execute(
                "SELECT * FROM users WHERE email = '%s';" % (email,))
            item = self.cur.fetchone()
            if item:
                return jsonify({"msg": "User successfully created"}), 201
        except psycopg2.IntegrityError:
            output = {
                'message': 'Email address already exists: ',
            }
            return jsonify(output), 400

    def create_table(self, table_name, table_columns):
        """method creates a single table"""
        create_table_command = "CREATE TABLE IF NOT EXISTS %s(%s);" % (
            table_name, table_columns)
        self.cur.execute(create_table_command)

