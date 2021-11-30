from flask_restful import Api
from controller.idea import Idea, IdeaList


##
## Actually setup the Api resource routing here
##
def register_controllers(app):
    api = Api(app)
    api.add_resource(IdeaList, '/ideas')
    api.add_resource(Idea, '/ideas/<idea_id>')
