from flask import Blueprint, render_template
from flask import current_app as app
from ..forms import ContactForm
from ..models import db, Contact


# Blueprint Configuration
home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


# Adding routes
@home_bp.route('/', methods=['GET'])
def home():
    """Homepage."""
    return render_template('index.html')

@home_bp.route('/about', methods=['GET'])
def about():
    """About Me"""
    return render_template('about.html')

@home_bp.route('/experience', methods=['GET'])
def experience():
    """Experience"""

    photos = [
        'img/Portfolio/' + str(number) + "c.jpg"
        for number in range(1, 7)
    ]

    return render_template('experience.html', photos=photos)

@home_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact"""
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(
            name=form.name.data,
            mobile=form.mobile.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data
        )
        db.session.add(contact)
        db.session.commit()
        return render_template('submit-contact.html')
    return render_template('contact.html', form=form)
