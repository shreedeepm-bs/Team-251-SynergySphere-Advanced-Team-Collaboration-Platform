from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, DateField, SelectField,SelectMultipleField,RadioField, FileField

from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf.file import FileAllowed
class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password')])
    submit = SubmitField('Create Account')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ProjectForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    tags = SelectMultipleField('Tags', choices=[('tag1', 'Feedback'), ('tag2', 'Optimise Performance'), ('tag3', 'Bug')])
    project_manager = StringField('Project Manager ID', validators=[DataRequired()])
    deadline = DateField('Deadline', format='%Y-%m-%d', validators=[DataRequired()])
    priority = RadioField('Priority', choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium')
    image = FileField('Image .jpg only', validators=[FileAllowed(['jpg'], 'Images only!')])
    description = TextAreaField('Description')
    submit = SubmitField('Create')

class TaskForm(FlaskForm):
    name = StringField('Task Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    assignee_id = TextAreaField('Assign To User Id', validators=[DataRequired()])
    tags = SelectField('Tags', choices=[('tag1', 'Feedback'), ('tag2', 'Optimise Performance'), ('tag3', 'Bug')])
    due_date = DateField('Due Date', format='%Y-%m-%d')
    image = FileField('Upload Image', validators=[FileAllowed(['jpg'], 'jpg Images only!')])
    status = SelectField('Status', choices=[('To-Do', 'To-Do'), ('In Progress', 'In Progress'), ('Done', 'Done')])
    submit = SubmitField('Save Task') #fixed