from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired, Length
class GetArticleContent(FlaskForm):
#    def __init__(self, nicks=None, *args, **kwargs):
#        super(GetArticleContent, self).__init__(*args, **kwargs)
#        self.nicks = nicks

    title = StringField('Заголовок статьи:', validators=[DataRequired(), Length(min=3, max=128)])
    motto = StringField('Девиз статьи:', validators=[DataRequired(), Length(min=3, max=128)])
    ilink = StringField('Внутренняя ссылка:', validators=[DataRequired(), Length(min=1, max=16)])
    olink = StringField('Внешняя ссылка:', validators=[DataRequired(), Length(min=8, max=128)])
    content = TextAreaField('Содержание статьи:', validators=[DataRequired(), Length(min=16)])
    date_posted = DateField('Дата регистрации статьи:', validators=[DataRequired()])
    date_pub = DateField('Дата оригинальной статьи:', validators=[DataRequired()])
    publisher_id = StringField('ID издателя:', validators=[DataRequired()])
    submit = SubmitField('Запись')
