from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import base, recipe, ingredient

app = FastAPI()

sqlalchemy_database_url = "sqlite:///./recipes.db"
engine = create_engine(sqlalchemy_database_url)
SessionLocal = sessionmaker(bind=engine)
base.metadata.create_all(bind=engine)

# Route to get list of all recipes
@app.get("/recipes", response_model=list[recipe])
def read_recipes(skip: int = 0, limit: int = 10):
    db = SessionLocal()
    recipes = db.query(recipe).offset(skip).limit(limit).all()
    return recipes

# Route to get detailed information about a specific recipe
@app.get("/recipes/{recipe_id}", response_model=recipe)
def read_recipe(recipe_id: int):
    db = SessionLocal()
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

# Route to create a new recipe
@app.post("/recipes", response_model=recipe)
def create_recipe(new_recipe: recipe):
    db = SessionLocal()
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe