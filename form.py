from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo

class RegistrationForm(FlaskForm):

    username = StringField('username_label',validators=[InputRequired(message="Username required"),Length(min=4,max=25,message='Username must be between 4 and 25 characters')])
    password = PasswordField('password_label',validators=[InputRequired(message="Password required"),Length(min=4,max=25,message='Password must be between 4 and 25 characters')])
    password_confirm = PasswordField('password_confirm_label',validators=[InputRequired(message="Password required"),EqualTo('password',message='Password must match')])
    submit = SubmitField('Create')