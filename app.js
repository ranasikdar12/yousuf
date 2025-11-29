const API_URL = "https://yousuf-yf0y.onrender.com";


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

