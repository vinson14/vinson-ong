from flask import Blueprint, render_template
from flask import current_app as app
from ..forms import ContactForm


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
    return render_template('experience.html')

@home_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact"""
    form = ContactForm()
    return render_template('contact.html', form=form)
