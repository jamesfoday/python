# Task-2.5: Model Updates and Reflections

## Models from Exercise 2.3

- **Recipe**  
  Initial fields:  
  - `name` (CharField)  
  - `cooking_time` (PositiveIntegerField)  
  - `description` (TextField)  

- **Ingredient**  
  Initial fields:  
  - `name` (CharField)  
  - `quantity` (CharField)  

---

## Updates Made

### Recipe Model

- Added `pic` field (`ImageField`) to allow uploading cover images for recipes.  
  *Reason:* To enable visually rich recipe listings and detail pages.

- Added `difficulty` field (`CharField` or similar) to represent the difficulty level of the recipe.  
  *Reason:* To provide users with quick insight about recipe complexity.

### Ingredient Model

- Added `image` field (`ImageField`) to allow uploading photos for ingredients.  
  *Reason:* To display ingredient thumbnails on recipe pages, enhancing UX.

### RecipeIngredient Model

- Created a new model to link `Recipe` and `Ingredient` with a `quantity` attribute.  
  *Reason:* To handle many-to-many relationship between recipes and ingredients, including specific quantities per recipe.

---

## Reasoning

- These updates enable more detailed and user-friendly presentation of recipes and ingredients.
- The new relationships between models better represent real-world data.
- Adding images enhances UI and makes the app visually appealing.
- Updating models early avoids costly changes once data and templates are established.

---

## Next Steps

- Populate the database with sample data using Django admin.  
- Build frontend templates to display recipes and ingredients with images.  
- Implement modals/lightboxes for ingredient images on recipe detail pages.  
- Write tests to validate views and data integrity.
