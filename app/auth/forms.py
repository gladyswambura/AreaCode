from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, ValidationError, BooleanField)
from wtforms.validators import InputRequired, Email, Length
from ..models import User


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Email(), Length(1, 64)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=6, max=72)])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
    