from routes.root import app
from controller import order

app.register_blueprint(order.get_order_blueprint)
app.register_blueprint(order.get_all_order_blueprint)
app.register_blueprint(order.create_order_blueprint)
app.register_blueprint(order.delete_order_blueprint)
app.register_blueprint(order.update_order_blueprint)