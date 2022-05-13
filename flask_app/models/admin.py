from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class Admin:
    db = "web3_resources"
    def __init__(self,data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO admins (username,email,password) VALUES(%(username)s,%(email)s,%(password)s)"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM admins;"
        results = connectToMySQL(cls.db).query_db(query)
        admins = []
        for row in results:
            admins.append( cls(row))
        return admins

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM admins WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        print("//////////////////")
        print(results)
        print("//////////////////")
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM admins WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])

    @staticmethod
    def validate_register(admin):
        is_valid = True
        query = "SELECT * FROM admins WHERE email = %(email)s;"
        results = connectToMySQL(Admin.db).query_db(query,admin)
        print("//////////////////")
        print(results)
        print("//////////////////")
        if len(results) >= 1:
            flash("Email already taken.","register")
            is_valid=False
        if not EMAIL_REGEX.match(admin['email']):
            flash("Invalid Email!!!","register")
            is_valid=False
        if len(admin['username']) < 3:
            flash("Username must be at least 3 characters","register")
            is_valid= False
        if len(admin['password']) < 8:
            flash("Password must be at least 8 characters","register")
            is_valid= False
        if admin['password'] != admin['confirm']:
            flash("Passwords don't match","register")
        return is_valid