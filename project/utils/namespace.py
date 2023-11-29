from flask_restx import Namespace

restaurant_ns = Namespace(name='Restaurant',
                          description='Manage restaurant',
                          path='/')

user_ns = Namespace(name='User',
                    description='Manage user',
                    path='/')

product_ns = Namespace(name='Product',
                       description='Manage product',
                       path='/')

client_ns = Namespace(name='Client',
                       description='Manage client',
                       path='/')

order_ns = Namespace(name='Order',
                      description='Manage order',
                      path='/')
