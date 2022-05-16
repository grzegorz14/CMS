# CMS system using Svelte.js + Flask server

Należy otworzyć plik server.py oraz sprawdzić czy moduł flask jest pobrany. 

Jeśli jest pobrany, proszę wykonać poniższe:
- otworzyć terminal i wykonać po kolei polecenia:
   1. cd client
   2. npm install
- otworzyć drugi terminal i wykonać polecenie: python server.py
- wejść w link do strony utworzony w terminalu

Jeśli nie jest pobrany, proszę wykonać poniższe:
- otworzyć terminal i wykonać po kolei polecenia:
   1. cd client
   2. npm install
- otworzyć drugi terminal i wykonać po kolei polecenia:
   1. skopiować ścieżkę do projektu w eksplorerze plików
   2. python -m venv skopiowanaŚcieżka\venv
   3. & skopiowanaŚcieżka/venv/Scripts/Activate.ps1
   4. pip install flask-bs4
   5. python server.py
- wejść w link do strony utworzony w terminalu

Po uruchomieniu aplikacji możemy się zalogować. Po zalogowaniu na stronę w prawym górnym rogu ekranu pojawia się zębatka po naciśnięciu, której przenosi nas na stronę z ustawieniami.  
Istnieją 2 wersje strony:  
- dla administratora w której można edytować wszystko co znajduje się na stronie  
(navbar, kolorystyka, template, slider, artykuły i użytkowników) 
- dla użytkowników w której można dodawać artykuły i swoje konto 

Konto administratora: 
- login: admin 
- hasło: admin 

Tkinter: 
- należy uruchomić plik main.py i zalogować się z użyciem konta administratora. Po zalogowaniu mamy dostęp do edycji ustawień na stronie. 
