from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class get_admin_content(FlaskForm):
    title = StringField('title', validators=[DataRequired(), Length(min=3, max=255)])
    content = StringField('content', validators=[DataRequired(), Length(min=16)])
    
    submit = SubmitField('Запись')
    
'''    
    email = StringField('Email',  validators=[DataRequired(), Email()])
    password = PasswordField('Password',  validators=[DataRequired()])
    confirmpassword = PasswordField('Password',  validators=[DataRequired(),EqualTo('password')])
    remember = BooleanField('Remember me')
'''    
