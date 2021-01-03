from flask import Blueprint, render_template, redirect, flash, url_for, request, session
from utilities import AdminCategories


# about blueprint  definition
admin_categories = Blueprint('admin_categories', __name__, static_folder='static',
                             static_url_path='/admin_categories', template_folder='templates')
categories_add = Blueprint('categories_add', __name__, static_folder='static',
                           static_url_path='/categories_add', template_folder='templates')
categories_edit = Blueprint('categories_edit', __name__, static_folder='static',
                            static_url_path='/categories_edit', template_folder='templates')
categories_delete = Blueprint('categories_delete', __name__, static_folder='static',
                              static_url_path='/categories_delete', template_folder='templates')


# Routes
@admin_categories.route('/admin_categories')
def index():
    if 'logged_in' in session:
        categories_data = AdminCategories().get_data()
        if categories_data:
            return render_template('admin_categories.html', categories=categories_data)
        else:
            flash('Action has failed.')
            return redirect(url_for('admin_page.index'))
    else:
        flash('Your session is over Please login again.')
        return redirect(url_for('dashboard_log_in.index'))



@categories_add.route('/categories_add', methods=['GET', 'POST'])
def index():
    if 'logged_in' in session:
        if request.method == 'GET':
            return render_template('categories_add.html')
        else:
            category_code = request.form.get('category-code')
            category_name = request.form.get('category-name')
            img = request.form.get('img')
            success = AdminCategories().insert_data(category_code, category_name, img)
            if success > 0:
                flash('A new category was successfully added')
                return redirect(url_for('admin_categories.index'))
            else:
                flash('Please enter your details again..')
                return redirect(url_for('categories_add.index'))
    else:
        flash('Your session is over Please login again.')
        return redirect(url_for('dashboard_log_in.index'))


@categories_edit.route('/categories_edit', methods=['GET', 'POST'])
def index():
    if 'logged_in' in session:
        if request.method == 'GET':
            if 'id' in request.args:
                category_code = request.args['id']
                category_data = AdminCategories().get_data_edit(category_code)
                if category_data:
                    return render_template('categories_edit.html', category=category_data[0])
                else:
                    flash('Category does not exist.')
                    return render_template('page_not_found.html')
            else:
                flash('Please try again.')
                return render_template('admin_categories.html')
        else:
            #print(request.form)
            category_code = request.form.get('category-code')
            category_name = request.form.get('category-name')
            img = request.form.get('img')
            success = AdminCategories().update_category_data(category_code, category_name, img)
            if success > 0:
                flash('Your changes have been saved.')
                return redirect(url_for('admin_categories.index'))
            else:
                flash('Please try to update again.')
                return redirect(url_for('categories_edit.index'))
    else:
        flash('Your session is over Please login again.')
        return redirect(url_for('dashboard_log_in.index'))



@categories_delete.route('/categories_delete', methods=['GET', 'POST'])
def index():
    if 'logged_in' in session:
        if request.method == 'POST':
            if 'category-code' in request.form:
                category_code = request.form['category-code']
                if AdminCategories().delete_data(category_code) > 0:
                    flash('The category was deleted.')
                    return redirect(url_for('admin_categories.index'))
                else:
                    flash('Action delete category has failed')
                    return redirect(url_for('categories_delete.html'))
            else:
                flash('Action delete category has failed')
                return redirect(url_for('categories_delete.html'))
        else:
            category_code = request.args['id']
            #print(request.args)
            return render_template('categories_delete.html', category_code=category_code)
    else:
        flash('Your session is over Please login again.')
        return redirect(url_for('dashboard_log_in.index'))