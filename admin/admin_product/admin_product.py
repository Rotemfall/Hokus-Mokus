from flask import Blueprint, render_template, redirect, flash, url_for, request, session
from utilities import AdminProducts

# about blueprint definition
admin_product = Blueprint('admin_product', __name__, static_folder='static', static_url_path='/admin_product', template_folder='templates')
product_add = Blueprint('product_add', __name__, static_folder='static', static_url_path='/product_add', template_folder='templates')
product_edit = Blueprint('product_edit', __name__, static_folder='static', static_url_path='/product_edit', template_folder='templates')
product_delete = Blueprint('product_delete', __name__, static_folder='static', static_url_path='/product_delete', template_folder='templates')


# Routes
@admin_product.route('/admin_product')
def index():
    if 'logged_in' in session:
        products_data = AdminProducts().get_data()
        if products_data:
            return render_template('admin_product.html', products=products_data)
        else:
            flash('Action has failed.')
            return redirect(url_for('admin_page.index'))
    else:
        flash('Your session is over Please login again.')
        return redirect(url_for('dashboard_log_in.index'))


@product_add.route('/product_add', methods=['GET', 'POST'])
def index():
    if 'logged_in' in session:
        if request.method == 'GET':
            return render_template('product_add.html')
        else:
            sku = request.form.get('sku')
            product_name = request.form.get('name')
            price = request.form.get('price')
            description = request.form.get('description')
            category_code = request.form.get('category-code')
            img = request.form.get('img')
            success = AdminProducts().insert_data(sku, product_name, price, description, category_code, img)
            if success > 0:
                flash('A new product was successfully added')
                return redirect(url_for('admin_product.index'))
            else:
                flash('Please enter your details again..')
                return redirect(url_for('product_add.index'))
    else:
        flash('Your session is over Please login again.')
        return redirect(url_for('dashboard_log_in.index'))


@product_edit.route('/product_edit', methods=['GET', 'POST'])
def index():
    if 'logged_in' in session:
        if request.method == 'GET':
            if 'id' in request.args:
                sku = request.args['id']
                product_data = AdminProducts().get_data_edit(sku)
                if product_data:
                    return render_template('product_edit.html', product=product_data[0])
                else:
                    flash('Product does not exist.')
                    return render_template('page_not_found.html')
            else:
                flash('Please try again.')
                return render_template('admin_product.html')
        else:
            #print(request.form)
            sku = request.form.get('sku')
            name = request.form.get('name')
            price = request.form.get('price')
            description = request.form.get('description')
            category_code = request.form.get('category-code')
            img = request.form.get('img')
            success = AdminProducts().update_product_data(sku, name, price, description, category_code, img)
            if success > 0:
                flash('Your changes have been saved.')
                return redirect(url_for('admin_product.index'))
            else:
                flash('Please try to update again.')
                return redirect(url_for('product_edit.index'))
    else:
        flash('Your session is over Please login again.')
        return redirect(url_for('dashboard_log_in.index'))


@product_delete.route('/product_delete', methods=['GET', 'POST'])
def index():
    if 'logged_in' in session:
        if request.method == 'POST':
            if 'sku' in request.form:
                product_sku = request.form['sku']
                if AdminProducts().delete_data(product_sku) > 0:
                    flash('The product was deleted.')
                    return redirect(url_for('admin_product.index'))
                else:
                    flash('Action delete product has failed')
                    return redirect(url_for('product_delete.html'))
            else:
                flash('Action delete product has failed')
                return redirect(url_for('product_delete.html'))
        else:
            product_sku = request.args['id']
            #print(request.args)
            return render_template('product_delete.html', sku=product_sku)
    else:
        flash('Your session is over Please login again.')
        return redirect(url_for('dashboard_log_in.index'))
