# rest_api
Zadanie: Budowa systemu rozproszonego z użyciem REST API

Opis Projektu
Ten projekt demonstruje komunikację między dwoma niezależnymi mikroserwisami, zaimplementowanymi w Pythonie z użyciem frameworku Flask.
Serwis Produktów (Port 8001): Udostępnia informacje o produktach.
Serwis Magazynowy (Port 8002): Pobiera zapytanie klienta, a następnie sprawdza istnienie produktu poprzez zapytanie do Serwisu Produktów.



Wymagania
Python 3.x
Zainstalowane biblioteki: Flask i requests.
pip install Flask requests



Jak Uruchomić Aplikacje
Aby uruchomić system, należy otworzyć dwa osobne terminale i w każdym z nich uruchomić odpowiedni serwis.

1. Uruchomienie Serwisu Produktów (Terminal 1)
W katalogu projektu: python products_service.py
Serwis powinien zacząć nasłuchiwać na porcie 8001.

2. Uruchomienie Serwisu Magazynowego (Terminal 2)
W drugim, nowym terminalu: python stock_service.py
Serwis powinien zacząć nasłuchiwać na porcie 8002.



Testowanie
Po uruchomieniu obu serwisów możesz użyć Postmana lub narzędzia curl w trzecim terminalu do testowania endpointów.

Scenariusz Sukcesu (Produkt istnieje)
Zapytanie do Serwisu Magazynowego (powoduje komunikację z Serwisem Produktów): curl http://localhost:8002/stock/123
Oczekiwana odpowiedź: Stan magazynowy (Status: 200 OK). Logi powinny pojawić się w obu terminalach.

Scenariusz Błędu (Produkt nie istnieje - 404)
Zapytanie o nieistniejący produkt: curl -i http://localhost:8002/stock/999
Oczekiwana odpowiedź: Błąd 404 Not Found. Logi powinny pojawić się w obu terminalach, dokumentując przekazanie błędu.
