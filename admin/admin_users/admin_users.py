from flask import Blueprint, render_template, redirect, flash, url_for, request, session
from utilities import AdminUsers

# about blueprint definition
admin_users = Blueprint('admin_users', __name__, static_folder='static', static_url_path='/admin_users', template_folder='templates')
users_add = Blueprint('users_add', __name__, static_folder='static', static_url_path='/users_add', template_folder='templates')
users_edit = Blueprint('users_edit', __name__, static_folder='static', static_url_path='/users_edit', template_folder='templates')
users_delete = Blueprint('users_delete', __name__, static_folder='static', static_url_path='/users_delete', template_folder='templates')


# Routes
@admin_users.route('/admin_users')
def index():
    if 'logged_in' in session:
        users_data = AdminUsers().get_data()
        if users_data:
            return render_template('admin_users.html', users=users_data)
        else:
            flash('Action has failed.')
            return redirect(url_for('admin_page.index'))
    else:
        flash('Your session is over Please login again.')
        return redirect(url_for('dashboard_log_in.index'))




@users_add.route('/users_add', methods=['GET', 'POST'])
def index():
    if 'logged_in' in session:
        if request.method == 'GET':
            return render_template('users_add.html')
        else:
            email_address = request.form.get('email-address')
            password = request.form.get('password')
            user_name = request.form.get('user-name')
            first_name = request.form.get('first-name')
            last_name = request.form.get('last-name')
            country = request.form.get('country')
            city = request.form.get('city')
            street = request.form.get('street')
            number = request.form.get('number')
            zip_code = request.form.get('zip-code')
            phone_number = request.form.get('phone-number')
            role = request.form.get('role')
            success = AdminUsers().insert_data(email_address, password, user_name, first_name, last_name, country, city, street, number, zip_code, phone_number, role)
            if success > 0:
                flash('A new user was successfully added')
                return redirect(url_for('admin_users.index'))
            else:
                flash('Please enter the details again..')
                return redirect(url_for('users_add.index'))
    else:
        flash('Your session is over Please login again.')
        return redirect(url_for('dashboard_log_in.index'))


@users_edit.route('/users_edit', methods=['GET', 'POST'])
def index():
    if 'logged_in' in session:
        if request.method == 'GET':
            if 'id' in request.args:
                email_address = request.args['id']
                customers_data = AdminUsers().get_data_edit(email_address)
                if customers_data:
                    return render_template('users_edit.html', user=customers_data[0])
                else:
                    flash('User does not exist.')
                    return render_template('page_not_found.html')
            else:
                flash('Please try again.')
                return render_template('admin_users.html')
        else:
            #print(request.form)
            email_address = request.form.get('email-address')
            password = request.form.get('password')
            user_name = request.form.get('user-name')
            first_name = request.form.get('first-name')
            last_name = request.form.get('last-name')
            country = request.form.get('country')
            city = request.form.get('city')
            street = request.form.get('street')
            number = request.form.get('number')
            zip_code = request.form.get('zip-code')
            phone_number = request.form.get('phone-number')
            role = request.form.get('role')
            success = AdminUsers().update_users_data(email_address, password, user_name, first_name, last_name, country, city, street, number, zip_code, phone_number, role)
            if success > 0:
                flash('Your changes have been saved.')
                return redirect(url_for('admin_users.index'))
            else:
                flash('Please try to update again.')
            return redirect(url_for('users_edit.index'))
    else:
        flash('Your session is over Please login again.')
        return redirect(url_for('dashboard_log_in.index'))


@users_delete.route('/users_delete', methods=['GET', 'POST'])
def index():
    if 'logged_in' in session:
        if request.method == 'POST':
            if 'email-address' in request.form:
                email_address = request.form['email-address']
                if AdminUsers().delete_data(email_address) > 0:
                    flash('The user was deleted.')
                    return redirect(url_for('admin_users.index'))
                else:
                    flash('Action delete user has failed')
                    return redirect(url_for('users_delete.html'))
            else:
                flash('Action delete user has failed')
                return redirect(url_for('users_delete.html'))
        else:
            email_address = request.args['id']
            #print(request.args)
            return render_template('users_delete.html', email_address=email_address)

    else:
        flash('Your session is over Please login again.')
        return redirect(url_for('dashboard_log_in.index'))