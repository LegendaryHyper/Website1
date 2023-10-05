import random
from flask import Flask
from facts_list_function import fact_transmission
from head_or_tails import head_or_tails
from pass_gen10 import passgen10
import os

app = Flask(__name__)

@app.route("/")
def main_page():
    return f'<a href="/random-fact">Rastgele bir gerçeği görüntüle!</a>\n<a href="/head-or-tails">Click for head or tails</a>\n<a href="/password-generator-10-digits">Click for a random 10 digit password!</a>\n<a href="/random-goofy-photos">Click for some random photos</a>'



@app.route("/random-fact")
def random_fact():
    return f'<p>{random.choice(fact_transmission())}</p>'

@app.route("/head-or-tails")
def head_or_tails_return():
    return f'<p>{head_or_tails()}</p>'

@app.route("/password-generator-10-digits")
def passgeneration():
    return f'<p>{passgen10()}</p>'

@app.route("/random-goofy-photos")
def random_photo():
    randomnumber = random.randint(1,5)
    address = random.choice(os.listdir("Goofy Photos"))
    return f'<img src = "static/{address}">'



app.run(debug=False)
