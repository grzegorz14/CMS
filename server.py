from email.mime import image
from flask import Flask, send_from_directory, request
import random
import glob
import json

app = Flask(__name__)

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    print(path)
    return send_from_directory('client/public', path)


@app.route("/getImagesLength")
def getImagesLength():
    images = [f for f in glob.glob("./client/public/images/*")]
    print(len(images))
    return str(len(images))

@app.route("/getImage")
def getImage():
    id = request.args.get('id')
    images = [f for f in glob.glob("./client/public/images/*")]
    print(len(images))
    if int(id) < len(images):
        return str(images[int(id)])
    return "wrongId"

if __name__ == "__main__":
    app.run(debug=True)
