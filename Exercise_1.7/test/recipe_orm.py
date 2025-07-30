from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Setup database connection (using SQLite here for simplicity)
engine = create_engine('sqlite:///recipes.db', echo=True)  # echo=True for SQL logs

# 2. Create base class for models
Base = declarative_base()

# 3. Define Recipe model class
class Recipe(Base):
    __tablename__ = 'recipes'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return f"<Recipe(name='{self.name}', difficulty='{self.difficulty}')>"

# 4. Create the recipes table in the database
Base.metadata.create_all(engine)

# 5. Create a session
Session = sessionmaker(bind=engine)
session = Session()

# 6. Add new recipes
recipe1 = Recipe(name="Tea", ingredients="Water, Tea Leaves, Sugar", cooking_time=5, difficulty="Easy")
recipe2 = Recipe(name="Coffee", ingredients="Water, Coffee Powder, Sugar", cooking_time=5, difficulty="Easy")

session.add(recipe1)
session.add(recipe2)
session.commit()

# 7. Query and display recipes
recipes = session.query(Recipe).all()
for r in recipes:
    print(r)

# 8. Update a recipe
tea = session.query(Recipe).filter_by(name="Tea").first()
tea.cooking_time = 7
tea.difficulty = "Medium"
session.commit()

# 9. Delete a recipe
coffee = session.query(Recipe).filter_by(name="Coffee").first()
session.delete(coffee)
session.commit()

# 10. Display recipes after update/delete
print("\nAfter update/delete:")
recipes = session.query(Recipe).all()
for r in recipes:
    print(r)

# Close session
session.close()
