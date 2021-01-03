from flask import Blueprint, url_for, redirect, session, flash

# logout blueprint definition
logout = Blueprint('logout', __name__, static_folder='static', static_url_path='/logout', template_folder='templates')


# Routes
@logout.route('/logout')
def index():
    if session.get('logged_in'):
        session.clear()
        flash('You are logged out.')
    return redirect(url_for('homepage.index'))
