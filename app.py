from flask import Flask
from flask_restful import reqparse, Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/postgres'
db = SQLAlchemy(app)


class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idea = db.Column(db.Text)

    def __repr__(self):
        return '<Idea %r>' % self.idea


try:
    db.create_all()
except Exception as e:
    print(e)
    print("database already exists")

parser = reqparse.RequestParser()
parser.add_argument('idea')


class IdeaController(Resource):
    def get(self, idea_id):
        return Idea.query.get(idea_id)

    def delete(self, idea_id):
        Idea.query.filter(Idea.id == idea_id).delete()
        return '', 204

    def put(self, idea_id):
        args = parser.parse_args()

        Idea.query.get(idea_id).update({
            Idea.idea: args['idea']
        })

        return Idea.query.get(idea_id), 201


class IdeasController(Resource):
    def get(self):
        return Idea.query.all()

    def post(self):
        args = parser.parse_args()
        new_idea = Idea(idea=args['idea'])
        db.session.add(new_idea)
        db.session.commit()
        return new_idea, 201


##
## Actually setup the Api resource routing here
##
api.add_resource(IdeasController, '/ideas')
api.add_resource(IdeaController, '/ideas/<idea_id>')

if __name__ == '__main__':
    app.run(debug=True)
