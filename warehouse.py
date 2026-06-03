warehouse = {"White Goods":{"Washing Machine":50,"Refrigerator":30,"Microwave":40,"Dishwasher":50, "Freezer":50, "Tumble dryer" :50, "Oven":15},
             "TV & Audio":{ "LED TV":30,"OLED TV":30,"Soundbar":50, "MP3 player":50, "Bluetooth Speaker":80},
             "Small Appliances":{ "Kettle": 100, "Coffee Machine":50, "Toaster" :75, "Air Fryer":90},
             "Computers & Tablets":{ "Laptop":100, "Desktop PC":60, "Tablet":50, "Monitor":40, "Keyboard":100, "Mouse":100, "Printer":50,"Accessories":150},
             "Smartphones":{ "iPhone":40, "Samsung":40, "One Plus":50, "Galaxy":35, "Redmi":100,"Accessories":600},

}

categories = list(warehouse.keys())
enumerate_categories = list(enumerate(categories, start = 1))
print(categories)



def show_stock():
   for category, products in warehouse.items():  
       print(category)
       for product, quantity in products.items():
           print(product,quantity)

# show_stock()

for number, category in enumerate_categories:
    print(f"{number}. {category}")


while True:
    print("1 Sell Product")
    print("2 Receive Stock")
    print("3 Returns") 
    print("0 Exit")
    operation = int(input("Select operation: "))
    if operation == 4:
        print("Goodbye!!")
        break
    elif operation == 1:
        print("--- Sell Product ---")
        choice= int(input("Choice category: "))
        if choice < 1 or choice > 5: 
            print("Invalid choice!!")
        else:
            selected = categories[choice -1 ]
            products = warehouse[selected]
            for number, product in enumerate(products, start = 1):
                print(f"{number}. {product}")
            pick = int(input("Choice product: "))
            prodcuts_list = list(products.keys())
            selected_product = prodcuts_list[pick -1]
            quantity = int(input("How Many: "))
            currrent_stock = warehouse[selected][selected_product]
            if quantity > currrent_stock:
                print("Not enough stock!!")
      
            else:
             warehouse[selected][selected_product] -=quantity
             print(f"New stock of {selected_product}: {warehouse[selected][selected_product]}")
        
    elif operation == 2:
        print("--- Receive Stock ---")
        choice= int(input("Choice category: "))
        if choice < 1 or choice > 5:
            print("Invalid choice!!")
        else:
            selected = categories[choice -1 ]
            products = warehouse[selected]
            for number, product in enumerate(products, start = 1):
                print(f"{number}. {product}")
            pick = int(input("Choice product: "))
            prodcuts_list = list(products.keys())
            selected_product = prodcuts_list[pick -1]
            quantity = int(input("How Many: "))
            warehouse[selected][selected_product] +=quantity
            print(f"New stock of {selected_product}: {warehouse[selected][selected_product]}")

    elif operation == 3:   
        print("--- Returns ---")
        choice= int(input("Choice category: "))
        if choice < 1 or choice > 5:
            print("Invalid choice!!")
        else:
            selected = categories[choice -1 ]
            products = warehouse[selected]
            for number, product in enumerate(products, start = 1):
                print(f"{number}. {product}")
            pick = int(input("Choice product: "))
            prodcuts_list = list(products.keys())
            selected_product = prodcuts_list[pick -1]
            quantity = int(input("How Many: "))
            warehouse[selected][selected_product] +=quantity
            print(f"{selected_product} retuned. New Stock: {warehouse[selected][selected_product]}")

         
    
  
     
   
    