const API_URL = "http://127.0.0.1:5000";

// Get product ID from URL
function getProductId() {
    const params = new URLSearchParams(window.location.search);
    return params.get("id");
}

// Load product details
async function loadProductDetail() {
    const id = getProductId();

    const response = await fetch(`${API_URL}/products/${id}`);
    const product = await response.json();

    document.getElementById("product-name").innerText = product.name;
    document.getElementById("product-price").innerText = "$" + product.price;
    document.getElementById("product-image").src = product.image;

    document.getElementById("product-color").innerText = product.color;
    document.getElementById("product-description").innerText = product.description;
}

// Buy button
function buyNow() {
    alert("Product added to cart!");
}

loadProductDetail();
