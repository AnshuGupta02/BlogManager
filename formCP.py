from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import data_required
from wtforms.widgets import TextArea

class AddText(FlaskForm):
    title=StringField('Title', validators=[data_required()], render_kw={"placeholder": "Title"})#we can use mutiple validators wth of list
    blog=StringField('blog', validators=[data_required()], widget=TextArea(), render_kw={'placeholder': 'Write Blog Here', 'wrap': 'hard'})
    submit=SubmitField(label='Create') #sirf 'submit' bhi likh skte hai.. label= ki jrurt ni

class DeleteText(FlaskForm):
    delete=SubmitField(label='Delete')

