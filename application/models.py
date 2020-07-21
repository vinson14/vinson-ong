"""Data models."""
from . import db
from flask_sqlalchemy import SQLAlchemy

class Contact(db.Model):
    """Data model for contact form."""

    __tablename__ = 'contact-form'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=False
    )

    mobile = db.Column(
        db.String(24),
        index=False,
        unique=False,
        nullable=False
    )

    email = db.Column(
        db.String(100),
        index=False,
        unique=False,
        nullable=False
    )

    subject = db.Column(
        db.String(),
        index=False,
        unique=False,
        nullable=False
    )


    message = db.Column(
        db.Text(),
        index=False,
        unique=False,
        nullable=False
    )
