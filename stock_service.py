from flask import Flask, jsonify, abort
import requests # Potrzebne do wykonania zapytania HTTP do innego serwisu

app = Flask(__name__)
PORT = 8002
PRODUCTS_SERVICE_URL = "http://localhost:8001/products"

# Dane magazynowe przechowywane "na sztywno"
STOCK = {
    123: {"productId": 123, "quantity": 15},
    456: {"productId": 456, "quantity": 50},
}

@app.route('/stock/<int:product_id>', methods=['GET'])
def get_stock(product_id):
    print(f"Stock Service: Otrzymano zapytanie o stan magazynowy ID: {product_id}")
    
    # 1. Kluczowe zadanie: Sprawdzenie, czy produkt istnieje w Serwisie Produktów
    product_check_url = f"{PRODUCTS_SERVICE_URL}/{product_id}"
    print(f"Stock Service: Komunikuję się z Serwisem Produktów: {product_check_url}")
    
    try:
        response = requests.get(product_check_url)
    except requests.exceptions.ConnectionError:
        print("Stock Service: Błąd połączenia z Serwisem Produktów.")
        return jsonify({"error": "Błąd komunikacji z serwisem produktów"}), 503

    # Obsługa ścieżki błędu (produkt nie istnieje)
    if response.status_code == 404:
        print(f"Stock Service: Serwis Produktów zwrócił 404. Przekazuję błąd 404.")
        # Serwis Magazynowy również powinien zwrócić błąd 404
        return jsonify({"error": f"Produkt ID {product_id} nie istnieje"}), 404
    
    # Obsługa ścieżki sukcesu (produkt istnieje)
    elif response.status_code == 200:
        stock_data = STOCK.get(product_id)
        
        if stock_data:
            print(f"Stock Service: Otrzymano dane produktu. Zwracam stan magazynowy: {stock_data['quantity']}")
            return jsonify(stock_data), 200
        else:
             # Przypadek gdy produkt jest w PRODUCTS, ale brak go w STOCK (opcjonalnie, ale dobry do obsługi)
             print(f"Stock Service: Produkt istnieje, ale brak danych magazynowych. Zwracam 404.")
             return jsonify({"error": f"Brak danych magazynowych dla produktu ID {product_id}"}), 404
    else:
        # Obsługa innych nieoczekiwanych błędów
        print(f"Stock Service: Serwis Produktów zwrócił nieoczekiwany kod: {response.status_code}")
        return jsonify({"error": "Nieoczekiwany błąd serwisu produktów"}), response.status_code

if __name__ == '__main__':
    print(f"*** Uruchamiam Serwis Magazynowy na http://localhost:{PORT} ***")
    app.run(port=PORT, debug=False)