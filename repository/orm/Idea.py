from infrastructure.utility.database import database, PkModel, column
from infrastructure.configuration.database import marshmallow


class Idea(PkModel):
    idea = column(database.Text)

    def __repr__(self):
        return '<Idea %r>' % self.idea


class IdeaSchema(marshmallow.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "idea",)
