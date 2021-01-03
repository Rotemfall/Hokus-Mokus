from db.db_manager import dbManager
'''
get:
use dbManager.fetch(query=, id) for select queries
:return: result if it succeeded False in not
update:
use dbManager.commit(query=, args=) for delete insert and update queries
:return: True if it succeeded (or False in not)
'''


class Catalog:
    # TODO get products list of the right categories query
    def get_data(self, id=None):
        query = 'SELECT * FROM products ' \
                'WHERE products.category_code=%s'
        return dbManager.fetch(query, (id,))


class Profile:
    def get_data(self, id=None):
        query = 'SELECT user_data.*, group1.reviews.`rank`, group1.reviews.date, group1.reviews.content ' \
                'FROM ( SELECT user_orders.*, credit_cards.expiration_date ' \
                'FROM ( ' \
                'SELECT details.*, product_details.name as product_name, product_details.img,' \
                ' product_details.price, product_details.sku FROM (SELECT group1.customers.*, o.id as order_id,' \
                ' o.date_of_order FROM group1.customers ' \
                'LEFT JOIN group1.orders o ON customers.email_address = o.email_address ' \
                'WHERE customers.email_address = %s ORDER BY o.date_of_order DESC LIMIT 10) as details' \
                ' LEFT JOIN (SELECT group1.products.*, group1.include.order_id FROM group1.products ' \
                'JOIN group1.include ON products.sku = include.sku) as product_details ' \
                'ON details.order_id = product_details.order_id ORDER BY product_details.name) as user_orders ' \
                'LEFT JOIN group1.credit_cards ON user_orders.email_address = credit_cards.email_address) AS user_data ' \
                'LEFT JOIN group1.reviews ' \
                'ON (user_data.user_name = group1.reviews.user_name AND user_data.sku = group1.reviews.sku)'
        return dbManager.fetch(query, (id,))

    def update_phone_number(self, email_address, phone):
        query = 'UPDATE group1.customers SET phone_number=%s ' \
                'WHERE group1.customers.email_address = %s;'
        return dbManager.commit(query, (phone, email_address,))

    def update_address(self, email_address, country, city, street, street_num, zip_code):
        query = 'UPDATE group1.customers SET country=%s, city=%s, street=%s, number=%s, zip_code=%s ' \
                'WHERE group1.customers.email_address = %s;'
        return dbManager.commit(query, (country, city, street, street_num, zip_code, email_address))

    def update_credit_card(self, email_address, credit_card_number, expiration_date, cvv):
        query = 'UPDATE group1.credit_cards SET credit_card_number=%s, expiration_date=%s, cvv=%s ' \
                'WHERE group1.credit_cards.email_address = %s;'

        success = dbManager.commit(query, (credit_card_number, expiration_date, cvv, email_address))
        if success > 0:
            return success
        return Profile().add_credit_card(email_address, credit_card_number, expiration_date, cvv)

    def add_credit_card(self, email_address, credit_card_number, expiration_date, cvv):
        query = 'INSERT INTO group1.credit_cards (email_address, credit_card_number, expiration_date, cvv) ' \
                'VALUES(%s, %s, %s, %s)'
        return dbManager.commit(query, (email_address, credit_card_number, expiration_date, cvv))

    def update_password(self, email_address, old_password,new_password):
        query = 'SELECT password FROM group1.customers WHERE email_address = %s'
        real_old_password = dbManager.fetch(query, (email_address,))
        if real_old_password[0].password == old_password:
            query = 'UPDATE group1.customers SET password=%s ' \
                'WHERE group1.customers.email_address = %s;'
            return dbManager.commit(query, (new_password, email_address))
        return False

    def delete_data(self, email_address):
        query = 'DELETE FROM group1.customers WHERE email_address = %s'
        return dbManager.commit(query, (email_address,))


class Home:
    def get_data(self, id=None):
        # TODO get carousal products query
        pass


class Product:
    def get_data(self, id=None):
        query = 'SELECT * FROM group1.products WHERE group1.products.sku=%s'
        return dbManager.fetch(query, (id,))


class Reviews:
    def get_data(self, id=None):
        query = 'SELECT group1.customers.user_name as user_name,' \
                ' group1.reviews.rank, content, group1.reviews.date as date ' \
                'FROM group1.reviews JOIN group1.customers ' \
                'ON group1.reviews.user_name = group1.customers.user_name ' \
                'WHERE group1.reviews.sku=%s ' \
                'ORDER BY date DESC, user_name'
        return dbManager.fetch(query, (id,))

    def upload_data(self, rank, content, user_name, id, email_address):
        vertify_query = 'SELECT details.*, include.sku FROM (' \
        ' SELECT group1.customers.user_name, o.id as order_id, o.date_of_order ' \
        'FROM group1.customers JOIN group1.orders o ON customers.email_address = o.email_address ' \
        'WHERE customers.email_address = %s ) as details ' \
        'JOIN group1.include ON details.order_id = include.order_id '
        customer_buy_the_product = dbManager.fetch(vertify_query, (email_address,))
        if customer_buy_the_product == 0:
            return (False, 'You need to buy the product in order to post a review')
        product_reviews = Reviews().get_data(id)
        for review in product_reviews:
            if review.user_name == user_name:
                return (False, 'You already post review for this product')
        query = 'INSERT INTO group1.reviews (date, `rank`, content, user_name, sku) ' \
                'VALUES(date(NOW()), %s, %s, %s, %s)'
        return (True, dbManager.commit(query, (rank, content, user_name, id)))


class ContactUs:
    def update_data(self, email_address, subject, content):
        query = 'INSERT INTO group1.contact_us(sent_date, subject, content, status, email_address) ' \
                'VALUES(date(NOW()), %s, %s, %s, %s)'
        return dbManager.commit(query, (subject, content, 'waiting', email_address))


class SignIn:
    def get_user_data(self, email_address=None, password=None):
        query = 'SELECT customers.first_name, customers.last_name, customers.email_address, customers.user_name, customers.role ' \
                'FROM group1.customers WHERE customers.email_address=%s AND customers.password=%s'
        return dbManager.fetch(query, (email_address, password,))


class Registration:
    def insert_data(self, email_address, password, user_name, first_name, last_name, country, city, street, number, zip_code, phone_number):
        query = 'INSERT INTO group1.customers (email_address, password, user_name, first_name, last_name, country, city, street, number, zip_code, phone_number) ' \
                'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        return dbManager.commit(query, (email_address, password, user_name, first_name, last_name, country, city, street, number, zip_code, phone_number))


class Categories:
    def get_data(self, id=None):
        query = 'SELECT category_code as code, category_name as name, img FROM group1.categories'
        return dbManager.fetch(query)

'''Admin classes'''
class AdminHome:
    def get_data(self, id=None):
        pass

class DashboardLogIn:
    def get_user_data(self, user_name=None, password=None):
        query = 'SELECT * FROM group1.customers ' \
                'WHERE customers.user_name=%s AND customers.password=%s ' \
                'AND (role="admin" or role="content manager" or role="dba");'
        return dbManager.fetch(query, (user_name, password,))

class AdminCategories:
    def get_data(self, id=None):
        query = 'SELECT * FROM group1.categories'
        return dbManager.fetch(query)

    def get_data_edit(self, id=None):
        query = 'SELECT * FROM group1.categories WHERE categories.category_code=%s'
        return dbManager.fetch(query, (id,))

    def insert_data(self, category_code, category_name, img):
        query = 'INSERT INTO group1.categories (category_code, category_name, img) ' \
                'VALUES(%s, %s, %s)'
        return dbManager.commit(query, (category_code, category_name, img))

    def delete_data(self, category_code):
        query = 'DELETE FROM group1.categories WHERE category_code = %s'
        return dbManager.commit(query, (category_code,))

    def update_category_data(self, category_code, category_name, img):
        query = 'UPDATE group1.categories SET category_name=%s, img=%s ' \
                'WHERE group1.categories.category_code=%s;'
        return dbManager.commit(query, (category_name, img, category_code))

class AdminProducts:
    #read the data
    def get_data(self, id=None):
        query = 'SELECT * FROM group1.products'
        return dbManager.fetch(query)

    def get_data_edit(self, id=None):
        query = 'SELECT * FROM group1.products WHERE products.sku=%s'
        return dbManager.fetch(query, (id,))
    #creat new data
    def insert_data(self, sku, name, price, description, category_code, img):
        query = 'INSERT INTO group1.products (sku, name, price, description, category_code, img) ' \
                'VALUES(%s, %s, %s, %s, %s, %s)'
        return dbManager.commit(query, (sku, name, price, description, category_code, img))
    #delete data
    def delete_data(self, sku):
        query = 'DELETE FROM group1.products WHERE sku = %s'
        return dbManager.commit(query, (sku,))
    #edit data
    def update_product_data(self, sku, name, price, description, category_code, img):
        query = 'UPDATE group1.products SET name=%s, price=%s, description=%s, category_code=%s, img=%s ' \
                'WHERE group1.products.sku=%s;'
        return dbManager.commit(query, (name, price, description, category_code, img, sku))


class AdminUsers:
    def get_data(self, id=None):
        query = 'SELECT * FROM group1.customers WHERE role="admin" or role="content manager" or role="dba"'
        return dbManager.fetch(query)

    def get_data_edit(self, id=None):
        query = 'SELECT * FROM group1.customers WHERE customers.email_address=%s'
        return dbManager.fetch(query, (id,))

    def insert_data(self, email_address, password, user_name, first_name, last_name, country, city, street, number, zip_code, phone_number, role):
        query = 'INSERT INTO group1.customers(email_address, password, user_name, first_name, last_name, country, city, street, number, zip_code, phone_number, role) ' \
                'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        return dbManager.commit(query, (email_address, password, user_name, first_name, last_name, country, city, street, number, zip_code, phone_number, role))

    def delete_data(self, email_address):
        query = 'DELETE FROM group1.customers WHERE email_address = %s'
        return dbManager.commit(query, (email_address,))

    def update_users_data(self, email_address, password, user_name, first_name, last_name, country, city, street, number, zip_code, phone_number, role):
        query = 'UPDATE group1.customers SET password=%s, user_name=%s, first_name=%s, last_name=%s, country=%s, city=%s, street=%s, number=%s, zip_code=%s, phone_number=%s, role=%s ' \
                'WHERE group1.customers.email_address=%s;'
        return dbManager.commit(query, (password, user_name, first_name, last_name, country, city, street, number, zip_code, phone_number, role, email_address))