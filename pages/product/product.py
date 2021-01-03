from flask import Blueprint, render_template, request, session, url_for, redirect, flash
from utilities import Product, Reviews

# product blueprint definition
product = Blueprint('product', __name__, static_folder='static', static_url_path='/product', template_folder='templates')


# Routes
@product.route('/product', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if 'id' in request.args:
            product_id = request.args['id']
            product_data = Product().get_data(product_id)
            reviews_data = Reviews().get_data(product_id)
        if len(product_data) > 0:
            if reviews_data == False:
                flash('Cannot load reviews. Please Refresh the page')
                return render_template('product.html', product=product_data[0], reviews=[])
            else:
                return render_template('product.html', product=product_data[0], reviews=reviews_data)
        return redirect(url_for('page_not_found.index'))
    else:
        if 'logged_in' in session:
            product_id = request.args['id']
            rank = request.form.get('rank')
            review = request.form.get('review')
            success = Reviews().upload_data(rank, review, session['user']['user_name'],
                                            product_id, session['user']['email_address'])
            if success[0] and success[1] > 0:
                flash('Your review is publish')
                return redirect(url_for('product.index', id=product_id))

            else:
                if success[0]:
                    flash('Error occurred, please submit your review again')
                    return redirect(url_for('product.index', id=product_id))
                flash(success[1]),
                return redirect(url_for('product.index', id=product_id))
        else:
            flash('You need to log in before you submit your review.')
            return redirect(url_for('sign_in_registration.index'))

