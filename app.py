from flask import Flask, render_template, request
import json
import requests
app = Flask(__name__)

@app.route("/")
def index():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    response = requests.get(url)

    data  = response.json() # Dictionary

    data_body = data["data"]
    quote = data_body["content"]
    author = data_body["author"]

    return render_template('index.html', quote=quote, author=author)

if __name__ == "__main__":
    app.run(debug=True)