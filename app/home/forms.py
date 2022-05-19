from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from flask_wtf.file import FileField, FileAllowed

class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[DataRequired(), Length(min=1, max=200)])
    submit =SubmitField('Submit')
    
class CommentForm(FlaskForm):
    commentbody = TextAreaField("Comment", validators=[DataRequired()])
    postbtn = SubmitField("Post")
    
class UpdateProfile(FlaskForm):
    username= StringField('New Username')
    bio = TextAreaField("Bio")
    photo = FileField("photo")
    submit = SubmitField("Update Profile")
    