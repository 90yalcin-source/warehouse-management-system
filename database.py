import sqlite3

class WarehouseManager:
    """Manages all database operations for the warehouse system."""
    
    def __init__(self, db_name="warehouse.db"):
        self.db_name = db_name
        self.create_tables()

    def get_connection(self):
        """Helper function that simplifies connecting to the database."""
        return sqlite3.connect(self.db_name)

    def create_tables(self):
        """Creates products, sales, and returns tables if they do not exist."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT,
                product TEXT,
                quantity INTEGER
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT,
                product TEXT,
                quantity INTEGER,
                date TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS returns (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT,
                product TEXT,
                quantity INTEGER,
                date TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.commit()
        conn.close()

    def receive_stock(self, category, product_name, qty):
        """Adds new stock or updates existing product quantity."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, quantity FROM products WHERE product = ?", (product_name,))
        existing_product = cursor.fetchone()
        
        if existing_product:
            cursor.execute("UPDATE products SET quantity = quantity + ? WHERE product = ?", (qty, product_name))
        else:
            cursor.execute("INSERT INTO products (category, product, quantity) VALUES (?, ?, ?)", (category, product_name, qty))
            
        conn.commit()
        conn.close()
        print(f"📥 Successfully received {qty} units of '{product_name}'.")

    def sell_product(self, product_name, qty):
        """Deducts quantity from products and logs the sale if stock is available."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, quantity, category FROM products WHERE product = ?", (product_name,))
        product = cursor.fetchone()
        
        if product is None:
            print(f"❌ Error: '{product_name}' is not found in the warehouse!")
            conn.close()
            return False
            
        current_stock = product[1]
        category = product[2]
        
        if current_stock < qty:
            print(f"❌ Error: Insufficient stock! Available: {current_stock}, Requested: {qty}")
            conn.close()
            return False
            
        cursor.execute("INSERT INTO sales (category, product, quantity) VALUES (?, ?, ?)", (category, product_name, qty))
        cursor.execute("UPDATE products SET quantity = quantity - ? WHERE product = ?", (qty, product_name))
        
        conn.commit()
        conn.close()
        print(f"💰 Successfully sold {qty} units of '{product_name}'.")
        return True

    def return_product(self, product_name, qty):
        """Logs the return and adds the quantity back to the products table."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT category FROM products WHERE product = ?", (product_name,))
        product = cursor.fetchone()
        
        category = product[0] if product else "Unknown"
        
        cursor.execute("INSERT INTO returns (category, product, quantity) VALUES (?, ?, ?)", (category, product_name, qty))
        
        if product:
            cursor.execute("UPDATE products SET quantity = quantity + ? WHERE product = ?", (qty, product_name))
        else:
            cursor.execute("INSERT INTO products (category, product, quantity) VALUES (?, ?, ?)", (category, product_name, qty))
            
        conn.commit()
        conn.close()
        print(f"🔄 Successfully returned {qty} units of '{product_name}'.")

    def get_top_selling_products(self):
        """Fetches the top 5 best-selling products."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT product, SUM(quantity) as total_sales 
            FROM sales 
            GROUP BY product 
            ORDER BY total_sales DESC 
            LIMIT 5
        """)
        report = cursor.fetchall()
        conn.close()
        return report
    