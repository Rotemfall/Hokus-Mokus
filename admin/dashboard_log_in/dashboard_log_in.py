from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from utilities import DashboardLogIn

# about blueprint definition
dashboard_log_in = Blueprint('dashboard_log_in', __name__, static_folder='static', static_url_path='/dashboard_log_in', template_folder='templates')


# Routes
@dashboard_log_in.route('/dashboard_log_in', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('dashboard_log_in.html')
    else:
        user_name = request.form['user-name']
        password = request.form['password']
        user = DashboardLogIn().get_user_data(user_name, password)
        if len(user):
            session['logged_in'] = True
            session['user'] = {
                'user_name': user[0].user_name,
                'first_name': user[0].first_name,
                'role': user[0].role,
            }
            if session['logged_in']:
                if session['user']['role'] != "customer":
                    flash('You are logged in.')
                    return redirect(url_for('dashboard_main.index'))
                else:
                    # customer is trying to sing in(not really possible)
                    flash('You do not have access to this website')
            else:
                flash('Please enter your details again.')
                return redirect(url_for('dashboard_log_in.index'))
        else:
            flash('Please verify your details and try again.')
            return redirect(url_for('dashboard_log_in.index'))