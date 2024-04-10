from wtforms import StringField, TextAreaField, validators
from flask_wtf import FlaskForm
from wtforms.validators import Email 

class ContactForm(FlaskForm):
    """Form to accept name, email, and message."""

    name = StringField("Name", [validators.DataRequired()])
    email = StringField("Email", [Email(message="Not a valid email address."), validators.DataRequired()])
    message = TextAreaField("Message", [validators.DataRequired(), validators.Length(max=5000)])
