from flask.ext.sqlalchemy import SQLAlchemy
import datetime

from review import app
db = SQLAlchemy(app)

_REVIEW_METRICS = (
    'documentation',
    'project_infrastructure',
    'ease_of_use',
    'ease_of_contribution',
    'code_quality',
    'overall',
    )


class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String)
    name = db.Column(db.String)
    description = db.Column(db.String)
    source = db.Column(db.String)
    documentation = db.Column(db.String)
    slug = db.Column(db.String)


class ReviewMetric(db.Model):
    __tablename__ = 'review_metric'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    stars = db.Column(db.Integer)
    content = db.Column(db.String)


class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String)
    review_date = db.Column(db.DateTime, onupdate=datetime.datetime.now)
    content = db.Column(db.String)
    project_id = db.Column(db.Integer, db.ForeignKey(Project.id))
    project = db.relationship('Project', backref=db.backref('review'))

for metric in _REVIEW_METRICS:
    setattr(Review, metric + '_review_id',
            db.Column(db.Integer, db.ForeignKey(ReviewMetric.id)))
    setattr(Review, metric + '_review', db.relationship('ReviewMetric',
            foreign_keys=[getattr(Review, metric + '_review_id')]))


class User(db.Model):
    __tablename__ = 'user'
    email = db.Column(db.String, primary_key=True)
    user_name = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)
    password = db.Column(db.String)

    def is_authenticated(self):
        return self.is_authenticated

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.email

db.metadata.create_all(db.engine)
