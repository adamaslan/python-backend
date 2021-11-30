from infrastructure.configuration.database import database

# Alias common SQLAlchemy names
column = database.Column
relationship = database.relationship
backref = database.backref

class CRUDMixin(object):
    """Mixin that adds convenience methods for CRUD (create, read, update, delete) operations."""

    @classmethod
    def create(cls, **kwargs):
        """Create a new record and save it the database."""
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        """Save the record."""
        database.session.add(self)
        if commit:
            database.session.commit()
        return self

    def delete(self, commit=True):
        """Remove the record from the database."""
        database.session.delete(self)
        return commit and database.session.commit()


class Model(CRUDMixin, database.Model):
    """Base model class that includes CRUD convenience methods."""

    __abstract__ = True


class DbModel(Model):
    """Base model class that includes CRUD convenience methods"""

    __abstract__ = True

    @classmethod
    def get_by_id(cls, record_id):
        """Get record by ID."""
        if any(
            (
                isinstance(record_id, basestring) and record_id.isdigit(),
                isinstance(record_id, (int, float)),
            )
        ):
            return cls.query.get(int(record_id))
        return None


class PkModel(DbModel):
    """Base model class that includes CRUD convenience methods, plus adds a 'primary key' column named ``id``"""

    __abstract__ = True
    id = column(database.Integer, primary_key=True)


def reference_col(
    tablename, nullable=False, pk_name="id", foreign_key_kwargs=None, column_kwargs=None
):
    """Column that adds primary key foreign key reference.
    Usage: ::
        idea_id = reference_col('idea')
        idea = relationship('Idea', backref='ideas')
    """
    foreign_key_kwargs = foreign_key_kwargs or {}
    column_kwargs = column_kwargs or {}

    return column(
        database.ForeignKey(f"{tablename}.{pk_name}", **foreign_key_kwargs),
        nullable=nullable,
        **column_kwargs,
    )