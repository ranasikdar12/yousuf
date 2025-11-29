from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

def read_json(file):
    with open(file) as f:
        return json.load(f)

def write_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)


# --------------------------
# API ROUTES
# --------------------------

@app.get("/products")
def products():
    return jsonify(read_json("data/products.json"))

@app.get("/products/<int:id>")
def product(id):
    data = read_json("data/products.json")
    for p in data:
        if p["id"] == id:
            return jsonify(p)
    return jsonify({"error": "Not found"}), 404

@app.post("/admin/products")
def add_product():
    data = read_json("data/products.json")
    new_product = request.json
    new_product["id"] = len(data) + 1
    data.append(new_product)
    write_json("data/products.json", data)
    return jsonify({"message": "Product added"})


# --------------------------
# FIX FOR RENDER HOST + PORT
# --------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


