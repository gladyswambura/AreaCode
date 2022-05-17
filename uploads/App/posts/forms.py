from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    content = TextAreaField('Write here ...', validators=[DataRequired()])
    picture = FileField('Upload image here', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Post')