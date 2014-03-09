from flaskext.bcrypt import Bcrypt
import models
from slugify import slugify

from review import app, bcrypt

def create_project():
    """Create a new project."""
    project = models.Project(
            name='Sandman',
            source='http://www.github.com/jeffknupp/sandman',
            documentation='https://sandman.readthedocs.org',
            description='Give legacy databases a RESTful API and Admin interface with a single command.',
            slug=slugify('Sandman'),
            author='Jeff Knupp')
    models.db.session.add(project)
    models.db.session.commit()
    return project

def create_user():
    """Create a new user."""
    user = models.User(
            email='jeff@jeffknupp.com',
            user_name='jeffknupp',
            password=bcrypt.generate_password_hash('jeffknupp')
            )
    models.db.session.add(user)
    models.db.session.commit()
    return user

def create_review(project):
    """Create new review."""
    review = models.Review(
            author='Jeff Knupp',
            content='Sandman rules!',
            project=project)
    models.db.session.add(review)
    models.db.session.commit()

def main():
    """Main entry point for script."""
    project = create_project()
    create_user()
    create_review(project)

if __name__ == '__main__':
    main()
