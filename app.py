from flask import Flask
from infrastructure.configuration.database import register_database, create_all_table
from infrastructure.configuration.controller import register_controllers


def create_app():
    app = Flask(__name__)
    app = register_database(app)
    register_controllers(app)

    # turn this off on prod
    create_all_table(app)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
