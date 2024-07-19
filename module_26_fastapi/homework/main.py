from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Recipe, Ingredient

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Подключение к базе данных SQLite
sqlalchemy_database_url = "sqlite:///./recipes.db"
engine = create_engine(sqlalchemy_database_url)
SessionLocal = sessionmaker(bind=engine)

# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)

# Маршрут для получения списка всех рецептов
@app.get("/recipes", response_model=list[Recipe])
def read_recipes(skip: int = 0, limit: int = 10):
    db = SessionLocal()
    recipes = db.query(Recipe).offset(skip).limit(limit).all()
    return recipes

# Маршрут для получения информации о конкретном рецепте
@app.get("/recipes/{recipe_id}", response_model=Recipe)
def read_recipe(recipe_id: int):
    db = SessionLocal()
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

# Маршрут для создания нового рецепта
@app.post("/recipes", response_model=Recipe)
def create_recipe(new_recipe: Recipe):
    db = SessionLocal()
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe