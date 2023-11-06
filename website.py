from flask import Flask
import random
coinPos=["Heads","Tails"]
app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1><p><a href=/randomcoin>\nToss coin</a>'
@app.route("/randomcoin")
def randomcoin():  
    return f'<p>{random.choice(coinPos)}</p><p><a href=/randomcoin>\nToss another?</a></p>'

app.run(debug=True)
