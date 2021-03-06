from routes.root import app
from controller import order_line

app.register_blueprint(order_line.get_order_line_blueprint)
app.register_blueprint(order_line.get_all_order_line_blueprint)
app.register_blueprint(order_line.create_order_line_blueprint)
app.register_blueprint(order_line.delete_order_line_blueprint)
app.register_blueprint(order_line.update_order_line_blueprint)