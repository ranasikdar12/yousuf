const API = "http://127.0.0.1:5000";

async function loadProducts() {
    let res = await fetch(`${API}/products`);
    let products = await res.json();

    let html = "";
    products.forEach(p => {
        html += `
        <div class="product-card">
            <h3>${p.name}</h3>
            <p>$${p.price}</p>
            <a href="product-detail.html?id=${p.id}">View</a>
        </div>`;
    });

    document.getElementById("product-list").innerHTML = html;
}

if (document.getElementById("product-list")) {
    loadProducts();
}
