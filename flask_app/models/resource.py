from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Resource:
    db = 'web3_resources'
    def __init__(self,db_data):
        self.id = db_data['id']
        self.type = db_data['type']
        self.name = db_data['name']
        self.description = db_data['description']
        self.link = db_data['link']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO resources (type, name, description, link) VALUES (%(type)s,%(name)s,%(description)s,%(link)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM resources;"
        results =  connectToMySQL(cls.db).query_db(query)
        all_resources = []
        for row in results:
            all_resources.append( cls(row) )
        return all_resources
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM resources WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE resources SET type=%(type)s, name=%(name)s, description=%(description)s, link=%(link)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM resources WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def validate_resource(resource):
        is_valid = True
        if len(resource['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters","resource")
        if len(resource['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters","resource")
        return is_valid