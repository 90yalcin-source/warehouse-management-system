from database import WarehouseManager

def main():
    db = WarehouseManager()
    print("🚀 Warehouse Management System is ready!")

    while True:
        print("\n=====================================")
        print("    WAREHOUSE MANAGEMENT SYSTEM Menu ")
        print("=====================================")
        print("1. Receive Stock (Stok Girişi)")
        print("2. Sell Product (Ürün Satışı)")
        print("3. Return Product (Ürün İadesi)")
        print("4. View Top Selling Products (Raporlar)")
        print("5. Exit (Çıkış)")
        print("=====================================")
        
        try:
            choice = int(input("Please select an option (1-5): "))
            if choice not in [1, 2, 3, 4, 5]:
                print("❌ Invalid choice! Please enter a number between 1 and 5.")
                continue
        except ValueError:
            print("❌ Error: Invalid input! Please enter numbers only.")
            continue

        # --- Menu Logic ---
        if choice == 1:
            print("\n[Action: Receive Stock]")
            category = input("Enter category: ")
            product = input("Enter product name: ")
            try:
                qty = int(input("Enter quantity: "))
                db.receive_stock(category, product, qty)
            except ValueError:
                print("❌ Error: Quantity must be a number!")
                
        elif choice == 2:
            print("\n[Action: Sell Product]")
            product = input("Enter product name: ")
            try:
                qty = int(input("Enter quantity to sell: "))
                db.sell_product(product, qty)
            except ValueError:
                print("❌ Error: Quantity must be a number!")
                
        elif choice == 3:
            print("\n[Action: Return Product]")
            product = input("Enter product name: ")
            try:
                qty = int(input("Enter quantity to return: "))
                db.return_product(product, qty)
            except ValueError:
                print("❌ Error: Quantity must be a number!")
                
        elif choice == 4:
            print("\n[Action: Analytics Report]")
            report = db.get_top_selling_products()
            print("\n🔥 TOP 5 BEST-SELLING PRODUCTS 🔥")
            if not report:
                print("No sales data available yet.")
            else:
                for index, item in enumerate(report, 1):
                    print(f"{index}. {item[0]} - Total: {item[1]} units")
            print("-" * 30)
            
        elif choice == 5:
            print("\nShutting down the system securely... Goodbye!")
            break # Halka kırılır, döngü biter ve program kapanır.

if __name__ == "__main__":
    main()