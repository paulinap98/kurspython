
from flask import Flask, render_template, request, url_for
import json
import openpyxl

app = Flask(__name__)
app.debug = False

@app.route('/')
def main_page():
    return render_template('main_page.html')

@app.route('/produkty')
def items():
    return render_template('items.html')
    print(url_for('items'))

@app.route('/koszyk')
def cart():
    return "Tutaj będzie koszyk"


app.run()
