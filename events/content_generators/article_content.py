from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
class GetArticleContent(FlaskForm):
    title = StringField('Текст заголовка статьи:', validators=[DataRequired(), Length(min=3, max=128)])
    content = TextAreaField('Текст содержания статьи:', validators=[DataRequired(), Length(min=16)])
    
    submit = SubmitField('Запись')
