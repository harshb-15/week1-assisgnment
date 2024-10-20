# inventory_system.py

from copy import copy, deepcopy


def create_inventory():
    """
    Create and return an inventory using different dictionary creation methods,
    including dictionary comprehensions and dict() constructor.
    """
    categories = ["Electronics", "Groceries"]
    electronics_items = [{'name': 'Laptop', 'price': 1100, 'quantity': 5}, {'name': 'Tablet', 'price': 500, 'quantity': 15}]
    inventory = {k: dict() for k in categories} 
    for item in electronics_items:
        inventory["Electronics"][item['name']] = item
    return inventory

def update_inventory(inventory, category, item_name, update_info):
    """
    Update item information (e.g., increasing stock, updating price) in the inventory.
    """
    prev_item_details = inventory[category][item_name]
    inventory[category][item_name] = {**prev_item_details, **update_info}
    pass

def merge_inventories(inv1, inv2):
    """
    Merge two inventory systems without losing any data.
    """
    inv1 = deepcopy(inv1)
    inv2 = deepcopy(inv2)

    for cat,val in inv2.items():
        if(cat in inv1.keys()):
            for key, item in val.items():
                if(key in inv1[cat]):
                    inv1[cat][key]['quantity'] += item['quantity']
                else:
                    inv1[cat][key] = item
        else:
            inv1[cat] = val
    return inv1

def get_items_in_category(inventory, category):
    """
    Retrieve all items in a specified category.
    """
    return inventory[category]
    pass

def find_most_expensive_item(inventory):
    """
    Find and return the most expensive item in the inventory.
    """
    expensive_item = {'price':-1}
    for cat,value in inventory.items():
        for item in value.values():
            if(item['price']>=expensive_item['price']):
                expensive_item = item
    return expensive_item

def check_item_in_stock(inventory, item_name):
    """
    Check if an item is in stock and return its details if available.
    """
    for cat, value in inventory.items():
        if item_name in value:
            return value[item_name]
    pass

def view_categories(inventory):
    """
    View available categories (keys of the outer dictionary).
    """
    return inventory.keys()
    pass

def view_all_items(inventory):
    """
    View all items (values of the inventory).
    """
    values = [item for val in inventory.values() for item in val.values() ]
    return values

def view_category_item_pairs(inventory):
    """
    View category-item pairs (items view of the inventory).
    """
    cat_item_pairs = [(cat, item) for cat, val in inventory.items() for item in val.values()]
    return cat_item_pairs

def copy_inventory(inventory, deep=True):
    """
    Copy the entire inventory structure. Use deep copy if deep=True, else use shallow copy.
    """
    if(deep):
        return deepcopy(inventory)
    return copy(inventory)