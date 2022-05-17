from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import StringField,PasswordField,SubmitField, BooleanField,SelectField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User
from wtforms import ValidationError



class RegistrationForm(FlaskForm):
    firstname = StringField('First Name',validators=[DataRequired()])
    lastname = StringField('Last Name',validators=[DataRequired()])
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    username = StringField('Enter your username',validators = [DataRequired()])
    location = SelectField('Location', coerce=int,choices=[(0, 'Please Select...'), (1, 'Ruaka'), (2, 'Muthaiga'), (3, 'Waiyaki Way'),(4, 'Ngong Road'), (5, 'Buruburu')],validators=[DataRequired()])
    password = PasswordField('Password',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Password',validators = [DataRequired()])
    terms = BooleanField('I have read and agreed with the terms of service and <br> our privacy policy.')
    submit = SubmitField('SIGN UP')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')


=======
from wtforms import (StringField, PasswordField, SubmitField, ValidationError, BooleanField)
from wtforms.validators import InputRequired, Email, Length
from ..models import User


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Email(), Length(1, 64)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=6, max=72)])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
    
>>>>>>> cbdd7d94a3e6113c55013b9e886dd7e6a60d59fc
