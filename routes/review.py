from routes.root import app
from controller import review

app.register_blueprint(review.get_review_blueprint)
app.register_blueprint(review.get_all_review_blueprint)
app.register_blueprint(review.create_review_blueprint)
app.register_blueprint(review.delete_review_blueprint)
app.register_blueprint(review.update_review_blueprint)