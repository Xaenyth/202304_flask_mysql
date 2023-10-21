from flask_app import app
from flask_app.controllers import cdojos, cninjas, croutes
DATABASE = 'dojos_and_ninjas_schema'


if __name__=="__main__":
    app.run(debug=True)