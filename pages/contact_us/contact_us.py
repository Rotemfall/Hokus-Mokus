from flask import Blueprint, render_template, request, redirect, flash, url_for
from utilities import ContactUs

# contact_us blueprint definition
contact_us = Blueprint('contact_us', __name__, static_folder='static', static_url_path='/contact_us', template_folder='templates')


# Routes
@contact_us.route('/contact_us', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('contact_us.html')
    else:
        email = request.form.get('email')
        subject = request.form.get('subject')
        content = request.form.get('message')
        if ContactUs().update_data(email, subject, content) > 0:
            flash('Your message sent')
        else:
            flash('Error! Please send again.')
        return render_template('contact_us.html')
