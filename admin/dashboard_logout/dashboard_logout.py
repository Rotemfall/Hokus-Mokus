from flask import Blueprint, url_for, redirect, session, flash

# logout blueprint definition
dashboard_logout = Blueprint('dashboard_logout', __name__, static_folder='static', static_url_path='/dashboard_logout', template_folder='templates')


# Routes
@dashboard_logout.route('/dashboard_logout')
def index():
    if session.get('logged_in'):
        session.clear()
        flash('You are logged out.')
    return redirect(url_for('dashboard_log_in.index'))
