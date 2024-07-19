from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

"""Создаем базовый класс моделей"""
Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipes'
    """Идентификатор рецепта"""
    id = Column(Integer, primary_key=True, index=True)
    """Название рецепта"""
    title = Column(String)
    """Время приготовления"""
    time_to_cook = Column(Integer)
    """Количество просмотров"""
    views = Column(Integer)
    """Связь с ингредиентами"""
    ingredients = relationship("Ingredient", back_populates="recipe")

class Ingredient(Base):
    __tablename__ = 'ingredients'
    """Идентификатор ингредиента"""
    id = Column(Integer, primary_key=True, index=True)
    """Название ингредиента"""
    name = Column(String)
    """Внешний ключ на рецепт"""
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    """Связь с рецептом"""
    recipe = relationship("Recipe", back_populates="ingredients")