from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Создаем базовый класс моделей
Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)  # Идентификатор рецепта
    title = Column(String)  # Название рецепта
    time_to_cook = Column(Integer)  # Время приготовления
    views = Column(Integer)  # Количество просмотров
    ingredients = relationship("Ingredient", back_populates="recipe")  # Связь с ингредиентами

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True, index=True)  # Идентификатор ингредиента
    name = Column(String)  # Название ингредиента
    recipe_id = Column(Integer, ForeignKey('recipes.id'))  # Внешний ключ на рецепт
    recipe = relationship("Recipe", back_populates="ingredients")  # Связь с рецептом