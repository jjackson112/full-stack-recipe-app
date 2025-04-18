import time
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# create a database and recipe table - will hold all recipe data
# configure location to store database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///recipes.db"
# create db object to import with
db = SQLAlchemy(app)

# how to organize db data - db model
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(500), nullable=False)
    description = db.Column(db.Text, nullable=True, default="Absolutely delicious! You should try it!")
    instructions = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(500), nullable=True, default="https://images.pexels.com/photos/9986228/pexels-photo-9986228.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
    servings = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"Recipe(id={self.id}, title='{self.title}', description='{self.description}', servings={self.serviings})"

# connect sql to web app
#    with app.app_context():
#        db.create_all()
#        db.session.commit()

# create app routes
@app.route("/api/recipes", methods=["GET"])

# build API directory with endpoints
def get_all_recipes():
    recipes = Recipe.query.all()
    recipe_list = []
    for recipe in recipes:
        recipe_list.append({
            'id': recipe.id,
            'title': recipe.title,
            'ingredients': recipe.ingredients,
            'instructions': recipe.instructions,
            'description': recipe.description,
            'image_url': recipe.image_url,
            'servings': recipe.servings
        })
    return jsonify(recipe_list)

if __name__ == '__main__':
    app.run(debug=True)
