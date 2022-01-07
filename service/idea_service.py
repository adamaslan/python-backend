from repository.orm.Idea import Idea


class IdeaService:
    def __init__(self):
        return

    def get_all(self):
        return Idea.query.all()

    def get_by_id(self, idea_id):
        return Idea.get_by_id(idea_id)

    def delete_by_id(self, idea_id):
        Idea.query.filter(Idea.id == idea_id).delete()

    def update_by_id(self, idea_id, args):
        Idea.query.filter(Idea.id == idea_id).update({
            Idea.idea: args['idea']
        })

    def new(self, args):
        new_idea = Idea(idea=args['idea'])
        new_idea.create().save()

        return new_idea
