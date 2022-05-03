from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, FileField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class BuysForm(FlaskForm):
    title = StringField('ф.И.О', validators=[DataRequired()])
    language = SelectField('Размер', choices=['xs', 's', 'm', 'l', 'xl', 'xxl', 'xxxl'])
    content = TextAreaField("Адрес доставки")
    submit = SubmitField('Применить')
