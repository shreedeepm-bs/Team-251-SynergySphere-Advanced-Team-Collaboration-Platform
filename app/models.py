from . import db
from flask_login import UserMixin
from datetime import datetime

# Association tables
task_tags = db.Table('task_tags',
    db.Column('task_id', db.Integer, db.ForeignKey('task.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

project_tags = db.Table('project_tags',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)

    # Relationships
    tags = db.relationship('Tag', secondary=project_tags, backref='projects')

    project_manager_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    project_manager = db.relationship('User', foreign_keys=[project_manager_id])

    deadline = db.Column(db.Date)
    priority = db.Column(db.String(10))  # e.g. 'low', 'medium', 'high'

    image = db.Column(db.String(255))  # store filename or full path

    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    assignee_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    due_date = db.Column(db.Date)
    status = db.Column(db.String(50), default="To-Do")
    image = db.Column(db.String(200))  # stores filename/path

    tags = db.relationship('Tag', secondary=task_tags, backref='tasks')
