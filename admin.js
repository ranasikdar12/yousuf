const API = "http://127.0.0.1:5000";

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
