const API_URL = "https://yousuf-yf0y.onrender.com";


async function addProduct() {
  let name = document.getElementById("pname").value;
  let price = document.getElementById("pprice").value;

  await fetch(`${API}/admin/products`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, price })
  });

  alert("Product added!");
}

