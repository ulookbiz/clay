from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class GetPublisherContent(FlaskForm):
    pub_name = StringField('Название издателя:', validators=[DataRequired(), Length(min=6, max=64)])
    nick = StringField('Ник издателя:', validators=[DataRequired(), Length(min=2, max=6)])
    pub_status = IntegerField('Статус издателя:', validators=[DataRequired(), NumberRange(min=0,max=10)])

    submit = SubmitField('Запись')
