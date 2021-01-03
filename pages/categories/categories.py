from flask import Blueprint, render_template, redirect, flash, url_for
from utilities import Categories
from db.db_manager import dbManager

# categories blueprint definition
categories = Blueprint('categories', __name__, static_folder='static', static_url_path='/categories', template_folder='templates')


# Routes
@categories.route('/categories')
def index():
    categories_data = Categories().get_data()
    if categories_data:
        return render_template('categories.html', categories=categories_data)
    else:
        flash('Action has failed.')
        return redirect(url_for('homepage.index'))

