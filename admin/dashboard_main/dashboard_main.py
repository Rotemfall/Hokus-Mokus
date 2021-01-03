from flask import Blueprint, render_template, flash, session, redirect, url_for

# about blueprint definition
dashboard_main = Blueprint('dashboard_main', __name__, static_folder='static', static_url_path='/dashboard_main', template_folder='templates')


# Routes
@dashboard_main.route('/dashboard_main')
def index():
    if 'logged_in' in session:
        return render_template('dashboard_main.html')
    else:
        flash('Your session is over Please login again.')
        return redirect(url_for('dashboard_log_in.index'))
