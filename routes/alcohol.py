from routes.root import app
from controller import alcohol

app.register_blueprint(alcohol.get_alcohol_blueprint)
app.register_blueprint(alcohol.get_all_alcohol_blueprint)
app.register_blueprint(alcohol.create_alcohol_blueprint)
app.register_blueprint(alcohol.delete_alcohol_blueprint)
app.register_blueprint(alcohol.update_alcohol_blueprint)
app.register_blueprint(alcohol.get_alcohol_by_type_alcohol_blueprint)
app.register_blueprint(alcohol.get_alcohol_by_subtype_alcohol_blueprint)