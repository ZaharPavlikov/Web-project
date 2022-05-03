from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class ManClother(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    language = SelectField('Programming Language', choices=['T-short', 'socks'])
    content = TextAreaField("Содержание")
    is_private = BooleanField("Личное")
    submit = SubmitField('Применить')
