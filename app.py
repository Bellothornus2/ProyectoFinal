import sys
from flask import Flask
from flask_cors import CORS 
from controller import (
    get_item,
    create_alcohol,
    get_all,
    delete_item,
    initialize_db,
    update_item,
    update_daily,
)


app = Flask(__name__)
app.register_blueprint(get_item.get_item_blueprint)
app.register_blueprint(get_all.get_all_blue)
app.register_blueprint(create_alcohol.create_alcohol_blueprint)
app.register_blueprint(delete_item.delete_item_blueprint)
app.register_blueprint(initialize_db.initialize_items_blue)
app.register_blueprint(update_item.update_item_blueprint)
app.register_blueprint(update_daily.update_daily_blue)
CORS(app)
try:
    if __name__ == "__main__" and sys.argv[1] == "production":
        app.run(debug=True, use_debugger=False, use_reloader=False, host="0.0.0.0")
except IndexError:
    app.run(debug=True, use_debugger=False, use_reloader=False)
