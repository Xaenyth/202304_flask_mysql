from flask_app.config.mysql_connection import connectToMySQL
from flask_app.models import ninja

DATABASE = 'dojos_and_ninjas_schema'


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.students = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []
        if results:
            for dojo in results:
                dojo_actual = cls(dojo)
                all_dojos.append(dojo_actual)
            return all_dojos
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos(name, created_at, updated_at) VALUES(%(name)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_dojo_with_students(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        # results will be a list of topping objects with the students attached to each row.
        dojos = cls(results[0])
        for row_from_db in results:
            data = {
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "age": row_from_db["age"],
                "created_at": row_from_db["ninjas.created_at"],
                "updated_at": row_from_db["ninjas.updated_at"],
            }
            dojos.students.append(model_ninjas.Ninja(data))
        return dojos