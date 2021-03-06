from routes.root import app
from controller import address

app.register_blueprint(address.get_address_blueprint)
app.register_blueprint(address.get_all_address_blueprint)
app.register_blueprint(address.create_address_blueprint)
app.register_blueprint(address.delete_address_blueprint)
app.register_blueprint(address.update_address_blueprint)