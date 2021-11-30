from flask import Flask
from flask_restful import Api
from infrastructure.configuration.database import register_database, create_all_table



def create_app():
    app = Flask(__name__)
    api = Api(app)
    app = register_database(app)

    from infrastructure.configuration.controller import register_controllers
    register_controllers(api)

    return app


app = create_app()

# turn this off on prod
create_all_table(app)

if __name__ == '__main__':
    app.run(debug=True)
