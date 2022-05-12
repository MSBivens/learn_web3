from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Suggestion:
    db = 'web3_resources'
    def __init__(self,db_data):
        self.id = db_data['id']
        self.type = db_data['type']
        self.title = db_data['title']
        self.link = db_data['link']
        self.type = db_data['type']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO suggestions (type, title, link) VALUES (%(type)s,%(title)s,%(link)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM suggestions;"
        results =  connectToMySQL(cls.db).query_db(query)
        all_suggestions = []
        for row in results:
            # print(row['date_made'])
            all_suggestions.append( cls(row) )
        return all_suggestions
    
    # Do I need this?
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM suggestions WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls( results[0] )
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM suggestions WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

# How to validate a link?
# How to validate a checkbox?
    @staticmethod
    def validate_suggestion(suggestion):
        is_valid = True
        if len(suggestion['title']) < 3:
            is_valid = False
            flash("Title must be at least 3 characters","suggestion")
        return is_valid