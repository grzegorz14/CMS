# CMS system using Svelte.js and Python Flask server

This is a simple CMS web app with some interesting facts and beautiful images. Loging in as an admin allows us to manipulate the content, links, users and look of the site.    

Admin login and password: admin

## Run locally

Client side - installing node modules.

```bash
  git clone --link--
  cd client
  npm install
  cd ../
```

Server side - installing flask-bs4 package.

```bash
  python -m venv copiedPathToProject\venv
  & copiedPathToProject/venv/Scripts/Activate.ps1
  pip install flask-bs4
  python server.py
```

Open link created by the terminal. 

## Tech Stack

**Client:** Svelte, HTML, CSS, Bootstrap, JavaScript

**Server:** Python, Flask, SQLite

## Tkinter desktop app

Run main.py to test it. This small app allows to edit page settings (which also can be done in web app settings). My teammate was mainly responsible for that part of the project. 
