from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequest, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from puppycompanyblog.models import User

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Email',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('password_confirm')])
    password_confirm = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('YOur email has been registered already!')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('YOur username has been registered already!')

class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Email', validators=[DataRequired()])
    picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update Profile')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('YOur email has been registered already!')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('YOur username has been registered already!')
