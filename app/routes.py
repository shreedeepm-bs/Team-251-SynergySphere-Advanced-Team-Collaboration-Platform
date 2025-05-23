from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager
from .models import User, Project, Task
from .forms import RegisterForm, LoginForm, ProjectForm, TaskForm
from wtforms import SelectMultipleField

main = Blueprint('main', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@main.route('/')
def index():
    return redirect(url_for('main.login'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        flash('Invalid email or password')
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route('/dashboard')
@login_required
def dashboard():
    projects = Project.query.filter_by(owner_id=current_user.id).all()
    return render_template('dashboard.html', projects=projects)

def blob_image(file):
    if file:
        return file.read()  # Read binary content

@main.route('/project/new', methods=['GET', 'POST'])
@login_required
def new_project():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(name=form.name.data, image = blob_image(form.image.data), priority = form.priority.data , deadline = form.deadline.data, project_manager_id=form.project_manager.data, description=form.description.data, owner_id=current_user.id)
        db.session.add(project)
        db.session.commit()
        print(blob_image(form.image.data))
        return redirect(url_for('main.dashboard'))
    return render_template('project_form.html', form=form)

@main.route('/project/<int:project_id>', methods=['GET', 'POST'])
@login_required
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    tasks = Task.query.filter_by(project_id=project.id).all()
    return render_template('project_detail.html', project=project, tasks=tasks)

@main.route('/project/<int:project_id>/task/new', methods=['GET', 'POST'])
@login_required
def new_task(project_id):
    form = TaskForm()
    print(form.validate_on_submit)
    if form.validate_on_submit():
        task = Task(
            name=form.name.data,
            description=form.description.data,
            assignee_id=int(form.assignee_id.data),
            due_date=form.due_date.data,
            image = blob_image(form.image.data),
            status=form.status.data,
            project_id=project_id  # use directly
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('main.project_detail', project_id=project_id))
    if request.method == 'POST':
        print("Form errors:", form.errors)

    return render_template('task_form.html', form=form)


