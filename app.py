from flask import Flask
from flask_restful import reqparse, Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
api = Api(app)
# @todo Use env vars to use local or docker connection string
# Docker uri for database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/postgres'
# Localhost uri for database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:8001/postgres'
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idea = db.Column(db.Text)

    def __repr__(self):
        return '<Idea %r>' % self.idea


class IdeaSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "idea",)


idea_schema = IdeaSchema()
ideas_schema = IdeaSchema(many=True)

try:
    db.create_all()
except Exception as e:
    print(e)
    print("database already exists")

parser = reqparse.RequestParser()
parser.add_argument('idea')


class IdeaController(Resource):
    def get(self, idea_id):
        return idea_schema.dump(Idea.query.get(idea_id))

    def delete(self, idea_id):
        Idea.query.filter(Idea.id == idea_id).delete()
        db.session.commit()
        return '', 204

    def put(self, idea_id):
        args = parser.parse_args()

        Idea.query.filter(Idea.id == idea_id).update({
            Idea.idea: args['idea']
        })

        db.session.commit()
        return self.get(idea_id), 201


class IdeasController(Resource):
    def get(self):
        ideas = Idea.query.all()
        return ideas_schema.dump(ideas)

    def post(self):
        args = parser.parse_args()
        new_idea = Idea(idea=args['idea'])
        db.session.add(new_idea)
        db.session.commit()
        return idea_schema.dump(new_idea), 201


##
## Actually setup the Api resource routing here
##
api.add_resource(IdeasController, '/ideas')
api.add_resource(IdeaController, '/ideas/<idea_id>')

if __name__ == '__main__':
    app.run(debug=True)
