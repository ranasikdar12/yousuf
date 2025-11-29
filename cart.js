function loadCart() {
    let cart = JSON.parse(localStorage.getItem("cart") || "[]");

    let html = "";
    cart.forEach(id => {
        html += `<div>Product ID: ${id}</div>`;
    });

    document.getElementById("cart-items").innerHTML = html;
}

function checkout() {
    alert("Checkout complete!");
    localStorage.removeItem("cart");
}

if (document.getElementById("cart-items")) {
    loadCart();
}
