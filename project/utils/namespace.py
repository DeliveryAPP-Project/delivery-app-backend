from flask_restx import Namespace

restaurant_ns = Namespace(
    name="Restaurant", description="Gerenciar restaurante", path="/restaurants"
)
user_ns = Namespace(name="User", description="Gerenciar usuário", path="/users")
product_ns = Namespace(
    name="Product", description="Gerenciar produto", path="/products"
)
client_ns = Namespace(name="Client", description="Gerenciar cliente", path="/clients")
order_ns = Namespace(name="Order", description="Gerenciar pedido", path="/orders")

lead_ns = Namespace(name="Lead", description="Gerenciar lead", path="/leads")
