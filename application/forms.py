from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional


class ContactForm(FlaskForm):
    """User Sign-up Form."""
    name = StringField(
        'Name',
        validators=[DataRequired()]
    )

    mobile = StringField(
        'Mobile No.',
        validators=[DataRequired()]
    )
    subject = StringField(
        'Subject',
        validators=[DataRequired()]
    )

    email = StringField(
        'Email',
        validators=[
            Length(min=6),
            Email(message='Enter a valid email.'),
            DataRequired()
        ]
    )

    message = TextAreaField(
        'Message',
        validators=[DataRequired()]
    )

    submit = SubmitField('Send Message')
