from flask import Blueprint, render_template, request, flash
from utilities import Catalog

# catalog blueprint definition
catalog = Blueprint('catalog', __name__, static_folder='static', static_url_path='/catalog', template_folder='templates')


# Routes
@catalog.route('/catalog')
def index():
    if 'id' in request.args:
        catalog_id = request.args['id']
        catalog_data = Catalog().get_data(catalog_id)
        if catalog_data:
            return render_template('catalog.html', products=catalog_data)
        else:
            flash('Category doesn\'t exist.')
            return render_template('page_not_found.html')
