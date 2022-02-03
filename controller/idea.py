from flask_restful import reqparse, Resource
from service.idea_service import IdeaService
from repository.orm.Idea import IdeaSchema

idea_schema = IdeaSchema()
ideas_schema = IdeaSchema(many=True)

parser = reqparse.RequestParser()
parser.add_argument('idea')

idea_service = IdeaService()


class Idea(Resource):
    def get(self, idea_id):
        try:
            idea = idea_service.get_idea(idea_id)
            response = idea_schema.dump(idea), 200
        except KeyError:
            response = '', 404
        return response

    def delete(self, idea_id):
        idea_service.delete_by_id(idea_id)
        return '', 204

    def put(self, idea_id):
        idea_service.update_by_id(idea_id, parser.parse_args())
        return '', 201


class IdeaList(Resource):
    def get(self):
        return ideas_schema.dump(idea_service.get_all())

    def post(self):
        new_idea = idea_service.dump(idea_service.new(parser.parse_args()))
        return idea_schema.dump(new_idea), 201
