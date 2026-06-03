// --- 1. VARSAYILAN ÜRÜN LİSTESİ ---
const defaultProducts = [
    { category: "White Goods", product: "Washing Machine", quantity: 50 },
    { category: "White Goods", product: "Refrigerator", quantity: 30 },
    { category: "White Goods", product: "Microwave", quantity: 40 },
    { category: "White Goods", product: "Dishwasher", quantity: 50 },
    { category: "White Goods", product: "Freezer", quantity: 50 },
    { category: "White Goods", product: "Tumble dryer", quantity: 50 },
    { category: "White Goods", product: "Oven", quantity: 15 },
    { category: "TV & Audio", product: "LED TV", quantity: 30 },
    { category: "TV & Audio", product: "OLED TV", quantity: 30 },
    { category: "TV & Audio", product: "Soundbar", quantity: 50 },
    { category: "TV & Audio", product: "MP3 player", quantity: 50 },
    { category: "TV & Audio", product: "Bluetooth Speaker", quantity: 80 },
    { category: "Small Appliances", product: "Kettle", quantity: 100 },
    { category: "Small Appliances", product: "Coffee Machine", quantity: 50 },
    { category: "Small Appliances", product: "Toaster", quantity: 75 },
    { category: "Small Appliances", product: "Air Fryer", quantity: 90 },
    { category: "Computers & Tablets", product: "Laptop", quantity: 100 },
    { category: "Computers & Tablets", product: "Desktop PC", quantity: 60 },
    { category: "Computers & Tablets", product: "Tablet", quantity: 50 },
    { category: "Computers & Tablets", product: "Monitor", quantity: 40 },
    { category: "Computers & Tablets", product: "Keyboard", quantity: 100 },
    { category: "Computers & Tablets", product: "Mouse", quantity: 100 },
    { category: "Computers & Tablets", product: "Printer", quantity: 50 },
    { category: "Computers & Tablets", product: "Accessories", quantity: 150 },
    { category: "Smartphones", product: "iPhone", quantity: 40 },
    { category: "Smartphones", product: "Samsung", quantity: 40 },
    { category: "Smartphones", product: "One Plus", quantity: 50 },
    { category: "Smartphones", product: "Galaxy", quantity: 35 },
    { category: "Smartphones", product: "Redmi", quantity: 100 },
    { category: "Smartphones", product: "Accessories", quantity: 600 }
];

let products = JSON.parse(localStorage.getItem('products')) || defaultProducts;
let sales = JSON.parse(localStorage.getItem('sales')) || [];

// --- 2. STOK GİRİŞİ ---
function receiveStock() {
    const category = document.getElementById('recCategory').value.trim();
    const product = document.getElementById('recProduct').value.trim();
    const qty = parseInt(document.getElementById('recQty').value);

    if (!category || !product || isNaN(qty) || qty <= 0) {
        alert("❌ Please enter valid details!");
        return;
    }

    let existing = products.find(item => item.product.toLowerCase() === product.toLowerCase());
    if (existing) { existing.quantity += qty; } 
    else { products.push({ category, product, quantity: qty }); }

    saveAndRefresh();
    document.getElementById('recCategory').value = '';
    document.getElementById('recProduct').value = '';
    document.getElementById('recQty').value = '';
}

// --- 3. SATIŞ YAPMA (ÇAKIŞMAYI ÖNLEMEK İÇİN ADINI "islemisun" YAPTIK) ---
function sellProduct() {
    const productInput = document.getElementById('sellProduct');
    const qtyInput = document.getElementById('sellQty');

    const product = productInput.value.trim();
    const qty = parseInt(qtyInput.value);

    if (!product || isNaN(qty) || qty <= 0) {
        alert("❌ Please enter a valid product name and quantity!");
        return;
    }

    let item = products.find(p => p.product.toLowerCase() === product.toLowerCase());
    
    if (!item) {
        alert(`❌ Error: '${product}' is not found!`);
        return;
    }

    if (item.quantity < qty) {
        alert(`❌ Error: Insufficient stock!`);
        return;
    }

    item.quantity -= qty;

    let saleRecord = sales.find(s => s.product.toLowerCase() === product.toLowerCase());
    if (saleRecord) { saleRecord.quantity += qty; } 
    else { sales.push({ product: item.product, quantity: qty }); }

    console.log("📊 CURRENT WAREHOUSE STATUS (Background):", products);

    saveAndRefresh();
    productInput.value = '';
    qtyInput.value = '';
    alert(`💰 Successfully processed order for ${qty} units of ${item.product}.`);
}

// 💥 KÖKTEN ÇÖZÜMÜ SAĞLAYAN SİHİRLİ DOKUNUŞ: 
// HTML'deki "sellProduct()" çağrısını zorla bu yeni temiz fonksiyona bağlıyoruz!
window.sellProduct = sellProduct;

// --- 4. İADE ALMAK ---
function returnProduct() {
    const product = document.getElementById('retProduct').value.trim();
    const qty = parseInt(document.getElementById('retQty').value);

    if (!product || isNaN(qty) || qty <= 0) {
        alert("❌ Please enter a valid product name and quantity!");
        return;
    }

    let item = products.find(p => p.product.toLowerCase() === product.toLowerCase());
    if (item) { item.quantity += qty; } 
    else { products.push({ category: "Returned", product, quantity: qty }); }

    saveAndRefresh();
    document.getElementById('retProduct').value = '';
    document.getElementById('retQty').value = '';
    alert(`🔄 Successfully processed return.`);
}

// --- 5. LİSTELEME ---


function saveAndRefresh() {
    localStorage.setItem('products', JSON.stringify(products));
    localStorage.setItem('sales', JSON.stringify(sales));
    
    console.log("📦 STOCK STATUS:", products);
    console.log("💰 SALES REPORT:", sales);
}




// Sayfa açılınca listeyi göster
saveAndRefresh();