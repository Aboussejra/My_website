from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('your lifting name bruh', validators=[DataRequired()])
    password = PasswordField('ur password bruh', validators=[DataRequired()])
    remember_me = BooleanField('pls remember me i d''ont have friends')
    submit = SubmitField('Log In')

class SignupForm(FlaskForm):
    username = StringField('your lifting name bruh', validators=[DataRequired()])
    password = PasswordField('ur usual password so i can hack your google acount', validators=[DataRequired()])
    remember_me = BooleanField('pls remember me i d''ont have friends')
    submit = SubmitField('Sign Up (30 euros/month)')

class HHSULForm(FlaskForm):
    age = FloatField('How old are you?', validators=[DataRequired()])
    time_training = FloatField('How long have you been training? (enter 1.5 for a year and a half)', validators=[DataRequired()])
    wheight = FloatField('How much do you wheight? (enter kgs)', validators=[DataRequired()])
    height = FloatField('How tall are you? (enter meters)', validators=[DataRequired()])
    body_fat = FloatField('What is your Body fat%? (try to guess)', validators=[DataRequired()])
    natty = FloatField('Are you natural? (roids or not, 1 for Natural, 0 for Roids)', validators=[DataRequired()])
    bulking_shredding = FloatField('Are you Bulking or shredding? (0 = Shredding, 1 = Nothing, 2 = Bulking)', validators=[DataRequired()])
    submit = SubmitField('Tell me how much i should lift')


