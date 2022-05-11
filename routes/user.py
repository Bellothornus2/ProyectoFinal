from routes.root import app
from controller import user

app.register_blueprint(user.get_user_blueprint)
app.register_blueprint(user.get_all_user_blueprint)
app.register_blueprint(user.create_user_blueprint)
app.register_blueprint(user.delete_user_blueprint)
app.register_blueprint(user.update_user_blueprint)