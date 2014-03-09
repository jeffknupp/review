"""Application to create, display, and vote on project reviews."""
import markdown
from flask import Flask, render_template, current_app, request, redirect, flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import login_required, login_user, logout_user, current_user
from slugify import slugify

from review.models import db, Review, Project, User
from review.forms import LoginForm
from review import app, bcrypt, login_manager

@login_manager.user_loader
def load_user(email):
    """Return a the user object with id=*user_id*."""
    return db.session.query(User).get(email)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log in a user."""
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.get(form.email.data)
            print user
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                if login_user(user):
                    user.authenticated = True
                    db.session.add(user)
                    db.session.commit()
                    return redirect(request.args.get('next') or '/')
        flash('Invalid username or password')
    return render_template('login.html', form=form)

@app.route('/')
def review_list():
    """Display a list of reviews."""
    reviews = db.session.query(Review).all()
    return render_template('list.html', reviews=reviews)

@app.route('/profile')
def profile():
    """Display a list of reviews."""
    return render_template('profile.html')

@app.route('/reviews/<review_slug>/<review_id>/')
def review_details(review_slug, review_id):
    """Show the details for a single review."""
    review = db.session.query(Review).get(int(review_id))
    return render_template('detail.html', review=review)

@app.route("/logout")
@login_required
def logout():
    """Logout the currently logged-in user.
    
    TODO: make this POST only."""
    current_user.authenticated = False
    db.session.add(current_user)
    db.session.commit()
    logout_user()
    return redirect('/')

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
    """Upload a review from a Markdown file."""
    if request.method == 'POST':
        file_contents = request.files['file'].read()
        review_html = markdown.markdown(file_contents)
        print request.form['project-name']
        project = Project(
                name=request.form['project-name'],
                author=request.form['project-author'],
                description=request.form['project-description'],
                source=request.form['project-source'],
                slug=slugify(request.form['project-name']),
                documentation=request.form['project-documentation'])
        db.session.add(project)
        db.session.commit()
        review = Review(
                project=project,
                author='Jeff Knupp',
                content=review_html)
        db.session.add(review)
        db.session.commit()
        return redirect('/reviews/{}/{}/'.format(project.slug, project.id))
    else:
        return render_template('upload.html')
