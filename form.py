from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from app import User

#username and password checker defined outside the class
def invalid_credentials(form,field):

    username_entered = form.username.data
    password_entered = field.data
    #check username is valValidationError
    user_object = User.query.filter_by(username=username_entered).first()
    if user_object is None:
        raise ValidationError("Username or password is incorrect")
    elif password_entered != user_object.password:
        raise ValValidationError("Username or password is incorrect")

class RegistrationForm(FlaskForm):

    username = StringField('username_label',validators=[InputRequired(message="Username required"),Length(min=4,max=25,message='Username must be between 4 and 25 characters')])
    password = PasswordField('password_label',validators=[InputRequired(message="Password required"),Length(min=4,max=25,message='Password must be between 4 and 25 characters')])
    password_confirm = PasswordField('password_confirm_label',validators=[InputRequired(message="Password required"),EqualTo('password',message='Password must match')])
    submit = SubmitField('Create')
#duplicate username checker defined inside the class
    def validate_username(self,username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Username already exist")

class LoginForm(FlaskForm):

    username = StringField('username_label',validators=[InputRequired(message="Username required")])
    password = PasswordField('password_label',validators=[InputRequired(message="Password required"),invalid_credentials])
    submit = SubmitField('Login')
