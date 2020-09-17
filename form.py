# flask wtf provides our flask application intergation with wtfforms

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationFrom(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=3, max=20)])

    email = StringField('Email', validators=[DataRequired()])

    password = StringField("Password", validators=[DataRequired()])

    confirm_password = StringField("Confirm Password", validators=[
                                   DataRequired(), EqualTo('password')])

    submit = SubmitField("Sign Up")


class LoginFrom(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
