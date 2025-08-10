# Task-2.7: Recipe Search & Data Visualization

## Search Criteria
- Search recipes by **recipe name** with partial matching (case insensitive).
- (Optional) Future filters: by ingredients, cooking time, or category.

## Output Format
- Search results shown as a table.
- Each recipe name is clickable and links to the recipe detail page.
- If no results, display "No recipes found".

## Data Analysis
### Planned Visualizations
1. **Bar Chart**  
   - X-axis: Cooking time ranges (e.g., <15, 15-30, 30-60 mins)  
   - Y-axis: Number of recipes in each range

2. **Pie Chart**  
   - Distribution of recipes by cooking time categories.

3. **Line Chart**  
   - Recipes created over time (by creation date).

### Chart Display Logic
- User selects chart type on search form.
- Charts update dynamically based on user input.
- Show chart below the search results table.

## Execution Flow (Summary)
1. User visits search page.
2. User inputs search criteria and chooses chart type.
3. Search results and chart are displayed.
4. User clicks on recipe to view details.
5. User navigates back or logs out.
