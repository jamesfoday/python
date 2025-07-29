class ShoppingList:
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)
        else:
            print(f"{item} is already in the list.")

    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)
        else:
            print(f"{item} is not in the list.")

    def view_list(self):
        print(f"{self.list_name} contains:")
        for item in self.shopping_list:
            print(f"- {item}")

# Main code to test the class
if __name__ == "__main__":
    pet_store_list = ShoppingList("Pet Store Shopping List")

    # Add items
    pet_store_list.add_item("dog food")
    pet_store_list.add_item("frisbee")
    pet_store_list.add_item("bowl")
    pet_store_list.add_item("collars")
    pet_store_list.add_item("flea collars")

    # Remove flea collars
    pet_store_list.remove_item("flea collars")

    # Try adding frisbee again
    pet_store_list.add_item("frisbee")

    # View the current list
    pet_store_list.view_list()
