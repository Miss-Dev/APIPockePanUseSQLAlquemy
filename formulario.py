from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import PasswordInput

csrf = CSRFProtect()

class form_ponto(FlaskForm):
    latitude = StringField('latitude', validators=[DataRequired()])
    longitude = StringField('longitude', validators=[DataRequired("Campo obrigatório!")])