from flask_wtf import FlaskForm
from wtforms import StringFiled, SubmitFiel, TextAreaField
from wtforms.validators import DataRequired

class BlogPostForm(FlaskForm):
    tilte =  StringFiled('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitFiel('Post')
