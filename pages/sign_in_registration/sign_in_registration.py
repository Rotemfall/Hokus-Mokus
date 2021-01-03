from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from utilities import SignIn
from utilities import Registration

# sign_in_registration blueprint definition
sign_in_registration = Blueprint('sign_in_registration', __name__, static_folder='static', static_url_path='/sign_in_registration', template_folder='templates')


@sign_in_registration.route('/sign_in_registration', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('sign_in_registration.html')
    else:
        if "sign-in-form" in request.form:
            email_address = request.form['email-address']
            password = request.form['password']
            user = SignIn().get_user_data(email_address, password)
            if len(user):
                session['logged_in'] = True
                session['user'] = {
                    'first_name': user[0].first_name,
                    'last_name': user[0].last_name,
                    'email_address': user[0].email_address,
                    'user_name': user[0].user_name,
                    'role': user[0].role,
                }
                if session['logged_in']:
                    flash('You are logged in.')
                return redirect(url_for('homepage.index'))
            else:
                flash('Please enter your details again.')
                return redirect(url_for('sign_in_registration.index'))
        else:
            user_name = request.form.get('user-name')
            email_address = request.form.get('email')
            password = request.form.get('password')
            first_name = request.form.get('first-name')
            last_name = request.form.get('last-name')
            country = request.form.get('country')
            city = request.form.get('city')
            street = request.form.get('street')
            number = request.form.get('number')
            zip_code = request.form.get('zip-code')
            phone_number = request.form.get('phone-number')
            success = Registration().insert_data(email_address, password, user_name, first_name, last_name, country, city, street, number, zip_code, phone_number)
            if success > 0:
                user = SignIn().get_user_data(email_address, password)
                if len(user):
                    session['logged_in'] = True
                    session['user'] = {
                        'first_name': user[0].first_name,
                        'last_name': user[0].last_name,
                        'email_address': user[0].email_address,
                        'user_name': user[0].user_name,
                        'role': user[0].role,
                    }
                flash('Your registration has been successfully done, welcome to Hokus Mokus!')
                return redirect(url_for('homepage.index'))
            else:
                flash('Please enter your details again. If you already have an account use the login form')
                return redirect(url_for('sign_in_registration.index'))
