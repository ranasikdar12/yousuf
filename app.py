from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Correct absolute path for Render
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Note: Ensure the 'data' directory and 'products.json' exist in your repository
PRODUCTS_FILE = os.path.join(BASE_DIR, "data", "products.json")

def read_json(file):
    """Reads data from the specified JSON file."""
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # Handle case where file might be missing during initial deployment/testing
        print(f"Error: Data file not found at {file}")
        return []

def write_json(file, data):
    """Writes data to the specified JSON file."""
    # Note: In a production environment like Render, persistent storage for changes
    # requires a database (like PostgreSQL, which Render offers) or a cloud storage
    # service, as changes to local files like this are lost on deployment or restart.
    try:
        with open(file, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error writing to file: {e}")


# --------------------------
# API ROUTES
# --------------------------

@app.get("/")
def home():
    """
    Root route for health checks and status display.
    This resolves the 404 error when hitting the base URL.
    """
    return jsonify({
        "status": "API is operational",
        "message": "Welcome to the YousufJoy API.",
        "endpoints": {
            "products_get_all": "/products",
            "products_get_by_id": "/products/<id>",
            "products_add_new": "/admin/products (POST)"
        }
    })

@app.get("/products")
def products():
    """Returns all products."""
    return jsonify(read_json(PRODUCTS_FILE))

@app.get("/products/<int:id>")
def product(id):
    """Returns a single product by ID."""
    data = read_json(PRODUCTS_FILE)
    for p in data:
        if p["id"] == id:
            return jsonify(p)
    return jsonify({"error": "Product not found"}), 404

@app.post("/admin/products")
def add_product():
    """Adds a new product (Note: changes are temporary on Render unless using a DB)."""
    data = read_json(PRODUCTS_FILE)
    
    # Ensure request data is valid JSON
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400
        
    new_product = request.json
    
    # Basic validation
    if not all(key in new_product for key in ['name', 'price']): # Example validation
        return jsonify({"error": "Missing name or price field"}), 400

    # Assign a new ID
    new_product["id"] = (data[-1]["id"] + 1) if data else 1
    data.append(new_product)
    
    write_json(PRODUCTS_FILE, data)
    
    return jsonify({"message": "Product added successfully", "product": new_product}), 201


# --------------------------
# WSGI ENTRY POINT (NO app.run())
# --------------------------
# This file is now configured to be run by Gunicorn via the Procfile.
# The previous development server code has been correctly removed.
