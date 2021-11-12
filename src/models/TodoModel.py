from . import db, schema
from datetime import datetime


class Todo(db.Model):
    __tablename__ = "todo"
    __table_args__ = {"schema": schema}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    content = db.Column(db.String(), nullable=False)
    type = db.Column(db.String(20), nullable=False, default='pending')
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, content):
        self.content = content
        self.type = 'pending'
        self.created_at = datetime.utcnow()
        self.modified_at = datetime.utcnow()

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        records = Todo.query.with_entities(Todo.id, Todo.content, Todo.type,
                                           Todo.created_at).order_by(Todo.created_at.desc())\
            .all()
        return records
