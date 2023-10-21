
from app.config.mysql_connection import connect_to_mysql



class User:

    def __init__(self, data):

        self.id = data["id"]
        self.first_name = data["first_name"]
        self.email = data["email"]
        self.password = data["password"]

    @classmethod
    def get_by_email(cls, data):

        query = """
        SELECT *
        FROM users WHERE email = %(email)s;
        """
        results = connect_to_mysql().query_db(query, data)
    
        if results:
            return cls(results[0])
        return None
    
    @classmethod
    def register(cls, data):
        
        query = """
        INSERT INTO users (first_name, email, password)
        VALUES (%(first_name)s, %(email)s, %(password)s);
        """
        user_id = connect_to_mysql().query_db(query, data)
        data = {"user_id": user_id}

        if user_id:
            user = cls.get_one(data)
            return user
        return None

    
    @classmethod
    def get_one(cls, data):

        query = """
        SELECT * FROM users WHERE id = %(id)s;
        """
        results = connect_to_mysql().query_db(query, data)
        if results:
            user = cls(results[0])
            return user

        return None