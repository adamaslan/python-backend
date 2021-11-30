from infrastructure.configuration.database import db, ma, PkModel, Column


class Idea(PkModel):
    idea = Column(db.Text)

    def __repr__(self):
        return '<Idea %r>' % self.idea


class IdeaSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "idea",)
