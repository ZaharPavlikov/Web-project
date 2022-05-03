from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, FileField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    language = SelectField('Категория одежды', choices=['Футболки', 'штаны', 'кофты', 'шорты'])
    pol = SelectField('Категория одежды', choices=['man', 'woman'])
    content = TextAreaField("Содержание")
    image = FileField('Image File')
    is_private = BooleanField("Личное")
    submit = SubmitField('Применить')
