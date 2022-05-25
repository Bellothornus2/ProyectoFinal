import sys
from flask_cors import CORS 
from controller import initialize_db
from routes.root import app
from routes import alcohol,ingredient,initialize_db,type_alcohol,subtype_alcohol,ingredient_alcohol,user,address,credit_card,order,order_line,review

CORS(app)
try:
	if __name__ == "__main__" and sys.argv[1] == "production":
		app.run(debug=True, use_debugger=False, use_reloader=False, host="0.0.0.0")
except IndexError:
	app.run(debug=True, use_debugger=False, use_reloader=False)
