const API = "http://127.0.0.1:5000";
const params = new URLSearchParams(window.location.search);
const id = params.get("id");

async function loadProduct() {
    let res = await fetch(`${API}/products/${id}`);
    let p = await res.json();

    document.getElementById("product-container").innerHTML = `
        <h1>${p.name}</h1>
        <p>Price: $${p.price}</p>
        <button onclick="addToCart(${p.id})">Add to Cart</button>
    `;
}

loadProduct();

function addToCart(id) {
    let cart = JSON.parse(localStorage.getItem("cart") || "[]");
    cart.push(id);
    localStorage.setItem("cart", JSON.stringify(cart));
    alert("Added to cart");
}
