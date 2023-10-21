from flask_app.config.mysql_connection import connectToMySQL

DATABASE = 'dojos_and_ninjas_schema'

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(id)s);"
        results = connectToMySQL(DATABASE).query_db(query, data)
        
    @classmethod
    def pull_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def pull_dojo_info(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)