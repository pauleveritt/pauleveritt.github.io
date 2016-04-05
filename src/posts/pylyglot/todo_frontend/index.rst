======================================
Moving the Frontend Out of the Backend
======================================

- Add flask-cors to requirements.txt

- todo/__init__.py

    - from flask.ext.cors import CORS

    - CORS(app)

- mkdir app

- Drag-drop templates/index.html app

- Drag-drop static/* app

- index.html: Fix jQuery reference to ../node_modules

- todo.js

    - Search & replace /api/ to be full URL http://localhost:5000

- From root: python3 -m http.server 8081

- Visit: http://localhost:8081/app/
