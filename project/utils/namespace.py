from flask_restx import Namespace

establishment_ns = Namespace(
    name="Establishment",
    description="Gerenciar estabelecimento",
    path="/establishments",
)
user_ns = Namespace(name="User", description="Gerenciar usuário", path="/users")
product_ns = Namespace(
    name="Product", description="Gerenciar produto", path="/products"
)
client_ns = Namespace(name="Client", description="Gerenciar cliente", path="/clients")
order_ns = Namespace(name="Order", description="Gerenciar pedido", path="/orders")
payment_ns = Namespace(
    name="Payment", description="Gerenciar pagamento", path="/payments"
)
lead_ns = Namespace(name="Lead", description="Gerenciar lead", path="/leads")
notification_ns = Namespace(
    name="Notification", description="Gerenciar Notificações", path="/notify"
)
