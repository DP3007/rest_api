from flask import Flask, jsonify, abort

app = Flask(__name__)
PORT = 8001

# Dane przechowywane "na sztywno"
PRODUCTS = {
    123: {"id": 123, "name": "Laptop", "price": 4500.00},
    456: {"id": 456, "name": "Myszka", "price": 120.00},
}

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    print(f"Products Service: Otrzymano zapytanie o produkt ID: {product_id}")
    
    product = PRODUCTS.get(product_id)
    
    if product:
        print(f"Products Service: Zwracam dane dla ID {product_id}")
        return jsonify(product), 200
    else:
        print(f"Products Service: Produkt ID {product_id} nie znaleziony. Zwracam 404.")
        # Zwrócenie standardowego błędu HTTP 404 Not Found
        abort(404) 

if __name__ == '__main__':
    print(f"*** Uruchamiam Serwis Produktów na http://localhost:{PORT} ***")
    # debug=True ułatwia testowanie, ale wyłącz w produkcji
    app.run(port=PORT, debug=False)