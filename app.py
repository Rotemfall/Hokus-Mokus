from flask import Flask


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
# Homepage
#TODO: we need to change homepage to homepage page
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

# About
from pages.about.about import about
app.register_blueprint(about)

# Catalog
from pages.catalog.catalog import catalog
app.register_blueprint(catalog)

# Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)

# Categories
from pages.categories.categories import categories
app.register_blueprint(categories)

# Sign_in_registration
from pages.sign_in_registration.sign_in_registration import sign_in_registration
app.register_blueprint(sign_in_registration)

# Logout
from pages.logout.logout import logout
app.register_blueprint(logout)

# Product
from pages.product.product import product
app.register_blueprint(product)

# Contact_us
from pages.contact_us.contact_us import contact_us
app.register_blueprint(contact_us)

# Profile
from pages.profile.profile import profile
app.register_blueprint(profile)

## Admin
# Dashboard main
from admin.dashboard_main.dashboard_main import dashboard_main
app.register_blueprint(dashboard_main)

# Dashboard log in
from admin.dashboard_log_in.dashboard_log_in import dashboard_log_in
app.register_blueprint(dashboard_log_in)

# Dashboard log out
from admin.dashboard_logout.dashboard_logout import dashboard_logout
app.register_blueprint(dashboard_logout)

# Admin product
from admin.admin_product.admin_product import admin_product
app.register_blueprint(admin_product)

# Admin edit product
from admin.admin_product.admin_product import product_edit
app.register_blueprint(product_edit)

# Admin add product
from admin.admin_product.admin_product import product_add
app.register_blueprint(product_add)

# Admin delete product
from admin.admin_product.admin_product import product_delete
app.register_blueprint(product_delete)

# Admin categories
from admin.admin_categories.admin_categories import admin_categories
app.register_blueprint(admin_categories)

# Admin edit categories
from admin.admin_categories.admin_categories import categories_edit
app.register_blueprint(categories_edit)

# Admin add categories
from admin.admin_categories.admin_categories import categories_add
app.register_blueprint(categories_add)

# Admin delete categories
from admin.admin_categories.admin_categories import categories_delete
app.register_blueprint(categories_delete)

# Admin users
from admin.admin_users.admin_users import admin_users
app.register_blueprint(admin_users)

# Admin edit users
from admin.admin_users.admin_users import users_edit
app.register_blueprint(users_edit)

# Admin add users
from admin.admin_users.admin_users import users_add
app.register_blueprint(users_add)

# Admin delete users
from admin.admin_users.admin_users import users_delete
app.register_blueprint(users_delete)

###### Components
# Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)