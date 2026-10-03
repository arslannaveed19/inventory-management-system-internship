
# PRODUCT CLASS 

class Product:

    def __init__(self, name, product_id, price, quantity):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.quantity = quantity

    def display(self):
        print("Product Name:", self.name)
        print("Product ID:", self.product_id)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("------------------------")


#ADD PRODUCT 
def add_product(products):

    print("~~ Add Product ~~")

    name = input("Enter Product Name: ")
    product_id = input("Enter Product ID: ")

    # Check duplicate ID
    for product in products:
        if product["product_id"] == product_id:
            print("Product ID already exists!")
            return

    price = float(input("Enter Price: "))

    if price < 0:
        print("Price cannot be negative!")
        return

    quantity = int(input("Enter Quantity: "))

    if quantity < 0:
        print("Quantity cannot be negative!")
        return

    product = Product(
        name,
        product_id,
        price,
        quantity
    )

    # Dictionary
    product_data = {
        "product_id": product.product_id,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity
    }

    products.append(product_data)

    print("Product added successfully!")


# VIEW PRODUCTS

def view_products(products):

    print(" All Products ")

    if len(products) == 0:
        print("No products available.")
        return

    for product in products:

        print("Product Name:", product["name"])
        print("Product ID:", product["product_id"])
        print("Price:", product["price"])
        print("Quantity:", product["quantity"])
        print("------------------------")


# SEARCH PRODUCT 

def search_product(products):

    print("===== Search Product =====")

    product_id = input("Enter Product ID: ")

    for product in products:

        if product["product_id"] == product_id:

            print("Product Found!")
            print("Name:", product["name"])
            print("ID:", product["product_id"])
            print("Price:", product["price"])
            print("Quantity:", product["quantity"])

            return

    print("Product not found!")


#  UPDATE PRODUCT 

def update_product(products):

    print("===== Update Product =====")

    product_id = input("Enter Product ID: ")

    for product in products:

        if product["product_id"] == product_id:

            new_name = input("Enter New Name: ")
            new_price = float(input("Enter New Price: "))
            new_quantity = int(input("Enter New Quantity: "))

            if new_price < 0:
                print("Price cannot be negative!")
                return

            if new_quantity < 0:
                print("Quantity cannot be negative!")
                return

            product["name"] = new_name
            product["price"] = new_price
            product["quantity"] = new_quantity

            print("Product updated successfully!")

            return

    print("Product not found!")


#  DELETE PRODUCT 

def delete_product(products):

    print("===== Delete Product =====")

    product_id = input("Enter Product ID: ")

    for product in products:

        if product["product_id"] == product_id:

            products.remove(product)

            print("Product deleted successfully!")

            return

    print("Product not found!")


#CHECK STOCK 

def check_stock(products):

    print("===== Check Stock =====")

    if len(products) == 0:
        print("No products available.")
        return

    for product in products:

        if product["quantity"] == 0:

            print(
                product["name"],
                "-> OUT OF STOCK"
            )

        elif product["quantity"] <= 5:

            print(
                product["name"],
                "-> LOW STOCK",
                product["quantity"]
            )

        else:

            print(
                product["name"],
                "-> In Stock",
                product["quantity"]
            )


#  SEARCH BY NAME 

def search_by_name(products):

    print("===== Search By Name =====")

    name = input("Enter Product Name: ").lower()

    found = False

    for product in products:

        if name in product["name"].lower():

            print("Product Found!")
            print("Name:", product["name"])
            print("ID:", product["product_id"])
            print("Price:", product["price"])
            print("Quantity:", product["quantity"])

            found = True

    if found == False:
        print("Product not found!")


#  TOTAL INVENTORY VALUE 

def total_inventory_value(products):

    total = 0

    for product in products:

        total = total + (
            product["price"] * product["quantity"]
        )

    print("\nTotal Inventory Value:", total)


#  MAIN PROGRAM 

products = []


while True:

    print("~~ Inventory Management System ~~")

    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Check Stock")
    print("7. Search Product By Name")
    print("8. Total Inventory Value")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_product(products)

    elif choice == "2":

        view_products(products)

    elif choice == "3":

        search_product(products)

    elif choice == "4":

        update_product(products)

    elif choice == "5":

        delete_product(products)

    elif choice == "6":

        check_stock(products)

    elif choice == "7":

        search_by_name(products)

    elif choice == "8":

        total_inventory_value(products)

    elif choice == "9":

        print("Thank you for using Inventory Management System!")
        break

    else:

        print("Invalid choice!")