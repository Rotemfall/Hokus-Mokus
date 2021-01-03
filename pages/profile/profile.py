from flask import Blueprint, render_template, request, session, url_for, redirect, flash
from utilities import Profile

# profile blueprint definition
profile = Blueprint('profile', __name__, static_folder='static', static_url_path='/profile', template_folder='templates')

# Routes
@profile.route('/profile', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if 'logged_in' in session:
            user_data = Profile().get_data(session['user']['email_address'])
            if user_data:
                return render_template('profile.html', user=user_data)
            else:
                flash('Error occurred. Please try again')
                return redirect(url_for('homepage.index'))
        else:
            flash('Your session is over Please login again.')
            return redirect(url_for('sign_in_registration.index'))
    else:
        if 'logged_in' in session:
            if "info-form" in request.form:
                phone = request.form.get('phone-number')
                success = Profile().update_phone_number(session['user']['email_address'], phone)
                if success > 0:
                    flash('Your changes have been saved.')
                    return redirect(url_for('profile.index'))
                else:
                    flash('Please try to update again.')
                return redirect(url_for('profile.index'))
            if "change-address" in request.form:
                country = request.form.get('country')
                city = request.form.get('city')
                street = request.form.get('street')
                street_num = request.form.get('number')
                zip_code = request.form.get('zip_code')
                success = Profile().update_address(session['user']['email_address'], country, city, street, street_num, zip_code)
                if success > 0:
                    flash('Your changes have been saved.')
                else:
                    flash('Please try to update again.')
                return redirect(url_for('profile.index'))
            elif "password-form" in request.form:
                old_password = request.form.get('old-password')
                new_password = request.form.get('new-password')
                success = Profile().update_password(session['user']['email_address'], old_password, new_password)
                if success > 0:
                    flash('Your changes have been saved.')
                else:
                    flash('Please try to update again.')
                return redirect(url_for('profile.index'))
            elif "card-form" in request.form:
                credit_card_number = request.form.get('credit')
                expiration_date = request.form.get('exp')
                cvv = request.form.get('cvv')
                # user_data = Profile().get_data(session['user']['email_address'])
                #  if user_data[0].expiration_date is None:
                # success = Profile().add_credit_card(session['user']['email_address'], credit_card_number,
                #                                         expiration_date, cvv)
                # else:
                success = Profile().update_credit_card(session['user']['email_address'], credit_card_number, expiration_date, cvv)
                if success > 0:
                    flash('Your changes have been saved.')
                else:
                    flash('Please try to update again.')
                return redirect(url_for('profile.index'))
            elif "delete-user" in request.form:
                if 'logged_in' in session:
                    if Profile().delete_data(session['user']['email_address']) > 0:
                        flash('You delete your profile')
                        return redirect(url_for('logout.index'))
                    else:
                        flash('Action delete account has failed')
                        return redirect(url_for('profile.index'))
                else:
                    flash('Your session is over Please login again.')
                    return redirect(url_for('sign_in_registration.index'))
        else:
            flash('Your session is over Please login again.')
            return redirect(url_for('sign_in_registration.index'))

