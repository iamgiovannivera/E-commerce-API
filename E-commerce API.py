# 1. Setup Flask and Flask-SQLAlchemy



# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/ecommerce_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


# 2. Define Models



# class Customer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     phone = db.Column(db.String(20), nullable=False)

# class CustomerAccount(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password_hash = db.Column(db.String(128), nullable=False)
#     customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
#     customer = db.relationship('Customer', backref=db.backref('accounts', lazy=True))

#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)

# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     price = db.Column(db.Float, nullable=False)
#     stock = db.Column(db.Integer, nullable=False)

# class Order(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     order_date = db.Column(db.DateTime, nullable=False)
#     customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
#     customer = db.relationship('Customer', backref=db.backref('orders', lazy=True))


# 3. Create CRUD Endpoints



# @app.route('/customers', methods=['POST'])
# def create_customer():
#     data = request.json
#     new_customer = Customer(name=data['name'], email=data['email'], phone=data['phone'])
#     db.session.add(new_customer)
#     db.session.commit()
#     return jsonify({"message": "Customer created successfully"}), 201

# @app.route('/customers/<int:id>', methods=['GET'])
# def get_customer(id):
#     customer = Customer.query.get_or_404(id)
#     return jsonify({"id": customer.id, "name": customer.name, "email": customer.email, "phone": customer.phone})

# @app.route('/customers/<int:id>', methods=['PUT'])
# def update_customer(id):
#     data = request.json
#     customer = Customer.query.get_or_404(id)
#     customer.name = data['name']
#     customer.email = data['email']
#     customer.phone = data['phone']
#     db.session.commit()
#     return jsonify({"message": "Customer updated successfully"})

# @app.route('/customers/<int:id>', methods=['DELETE'])
# def delete_customer(id):
#     customer = Customer.query.get_or_404(id)
#     db.session.delete(customer)
#     db.session.commit()
#     return jsonify({"message": "Customer deleted successfully"})




# @app.route('/customer_accounts', methods=['POST'])
# def create_customer_account():
#     data = request.json
#     customer_id = data['customer_id']
#     customer = Customer.query.get_or_404(customer_id)
#     new_account = CustomerAccount(username=data['username'], customer=customer)
#     new_account.set_password(data['password'])
#     db.session.add(new_account)
#     db.session.commit()
#     return jsonify({"message": "Customer account created successfully"}), 201

# @app.route('/customer_accounts/<int:id>', methods=['GET'])
# def get_customer_account(id):
#     account = CustomerAccount.query.get_or_404(id)
#     return jsonify({"id": account.id, "username": account.username, "customer_id": account.customer_id})

# @app.route('/customer_accounts/<int:id>', methods=['PUT'])
# def update_customer_account(id):
#     data = request.json
#     account = CustomerAccount.query.get_or_404(id)
#     account.username = data['username']
#     account.set_password(data['password'])
#     db.session.commit()
#     return jsonify({"message": "Customer account updated successfully"})

# @app.route('/customer_accounts/<int:id>', methods=['DELETE'])
# def delete_customer_account(id):
#     account = CustomerAccount.query.get_or_404(id)
#     db.session.delete(account)
#     db.session.commit()
#     return jsonify({"message": "Customer account deleted successfully"})



# Product Management Endpoints:

    


# @app.route('/products', methods=['POST'])
# def create_product():
#     data = request.json
#     new_product = Product(name=data['name'], price=data['price'], stock=data['stock'])
#     db.session.add(new_product)
#     db.session.commit()
#     return jsonify({"message": "Product created successfully"}), 201

# @app.route('/products/<int:id>', methods=['GET'])
# def get_product(id):
#     product = Product.query.get_or_404(id)
#     return jsonify({"id": product.id, "name": product.name, "price": product.price, "stock": product.stock})

# @app.route('/products/<int:id>', methods=['PUT'])
# def update_product(id):
#     data = request.json
#     product = Product.query.get_or_404(id)
#     product.name = data['name']
#     product.price = data['price']
#     product.stock = data['stock']
#     db.session.commit()
#     return jsonify({"message": "Product updated successfully"})

# @app.route('/products/<int:id>', methods=['DELETE'])
# def delete_product(id):
#     product = Product.query.get_or_404(id)
#     db.session.delete(product)
#     db.session.commit()
#     return jsonify({"message": "Product deleted successfully"})

# @app.route('/products', methods=['GET'])
# def list_products():
#     products = Product.query.all()
#     result = [{"id": p.id, "name": p.name, "price": p.price, "stock": p.stock} for p in products]
#     return jsonify(result)



# 4. Order Management Endpoints:

    


# @app.route('/orders', methods=['POST'])
# def place_order():
#     data = request.json
#     customer = Customer.query.get_or_404(data['customer_id'])
#     new_order = Order(order_date=data['order_date'], customer=customer)
#     db.session.add(new_order)
#     db.session.commit()
#     return jsonify({"message": "Order placed successfully"}), 201

# @app.route('/orders/<int:id>', methods=['GET'])
# def retrieve_order(id):
#     order = Order.query.get_or_404(id)
#     return jsonify({"id": order.id, "order_date": order.order_date, "customer_id": order.customer_id})

# @app.route('/orders', methods=['GET'])
# def list_orders():
#     orders = Order.query.all()
#     result = [{"id": o.id, "order_date": o.order_date, "customer_id": o.customer_id} for o in orders]
#     return jsonify(result)



# 5. Run the Application



# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)