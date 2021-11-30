from flask import Flask
from flask_restful import Api
from infrastructure.configuration.controller import register_controllers
from infrastructure.configuration.database import register_database


def create_app():
    app = Flask(__name__.split(".")[0])
    api = Api(app)
    register_controllers(api)
    register_database(app)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
